#!/usr/bin/env python3
"""
ИНТЕРПРЕТАТОР ДЛЯ MyLanguage (полная перезапись под грамматику с метками)
"""

import sys
from pathlib import Path
from antlr4 import *
from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser
from MyLanguageVisitor import MyLanguageVisitor
from antlr4.error.ErrorListener import ErrorListener


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Строка {line}:{column} — {msg}")


class MyInterpreter(MyLanguageVisitor):
    def __init__(self):
        self.variables = {}   # обычные переменные: str → значение
        self.arrays = {}      # массивы: имя → { 'type', 'data': list, 'lower': int }
        self.output_lines = []  # для сбора вывода

    # ---------- ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ----------
    
    def _get_value(self, var_ctx):
        """Получить значение из variable-контекста (ID, константа или массив)."""
        if var_ctx is None:
            raise ValueError("Пустой контекст переменной")

        # Делегируем по типу узла
        return self.visit(var_ctx)

    # ---------- ПРОГРАММА И БЛОК ----------
    
    def visitProgram(self, ctx):
        prog_name = ctx.name.text
        print(f"🚀 Программа: {prog_name}")
        return self.visit(ctx.block())

    def visitBlock(self, ctx):
        print("📦 Начало блока")
        print("📝 ОПИСАНИЯ:")
        self.visit(ctx.descList)
        print("--- Разделитель $ ---")
        print("⚡ ОПЕРАТОРЫ:")
        self.visit(ctx.stmtList)
        print("📦 Конец блока")
        return None

    # ---------- ОПИСАНИЯ ----------
    
    def visitDescriptionList(self, ctx):
        self.visit(ctx.first)
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTail(self, ctx):
        self.visit(ctx.next)
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTail(self, ctx):
        return None

    def visitSimpleDesc(self, ctx):
        var_type = ctx.varType.text
        self._current_type = var_type
        self.visit(ctx.vars)
        del self._current_type
        return None

    def visitArrayDesc(self, ctx):
        # Обрабатываем обе формы: typedArray и logicArray
        if isinstance(ctx, MyLanguageParser.TypedArrayContext):
            arr_type = ctx.arrType.text
            arr_name = ctx.arrName.text
            bounds_ctx = ctx.range  # ← исправлено: range вместо bounds
            lower = int(bounds_ctx.lower.text)
            upper = int(bounds_ctx.upper.text)
            size = upper - lower + 1

            init_val = 0
            if arr_type == 'integer':
                init_val = 0
            elif arr_type == 'real':
                init_val = 0.0
            elif arr_type == 'bool':
                init_val = False
            elif arr_type == 'string':
                init_val = ""

            self.arrays[arr_name] = {
                'type': arr_type,
                'data': [init_val] * size,
                'lower': lower
            }
            print(f"    array {arr_type} {arr_name}[{lower}:{upper}]")

        elif isinstance(ctx, MyLanguageParser.LogicArrayContext):
            arr_name = ctx.logicName.text
            print(f"    logic array {arr_name}")

        return None

    def visitIdentifierList(self, ctx):
        var_name = ctx.first.text
        self._declare_variable(var_name)
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailIdContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTailId(self, ctx):
        var_name = ctx.next.text
        self._declare_variable(var_name)
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailIdContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTailId(self, ctx):
        return None

    def _declare_variable(self, name):
        var_type = getattr(self, '_current_type', 'integer')
        init_val = 0
        if var_type == 'integer':
            init_val = 0
        elif var_type == 'real':
            init_val = 0.0
        elif var_type == 'bool':
            init_val = False
        elif var_type == 'string':
            init_val = ""
        self.variables[name] = init_val
        print(f"    {var_type} {name}")

    # ---------- ОПЕРАТОРЫ ----------
    
    def visitStatementList(self, ctx):
        self.visit(ctx.first)
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailStmtContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTailStmt(self, ctx):
        self.visit(ctx.next)
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailStmtContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTailStmt(self, ctx):
        return None

    def visitAssignStmt(self, ctx):
        target = ctx.target
        value = self.visit(ctx.expr)

        if target.ID() is not None:
            var_name = target.ID().getText()
            if var_name in self.variables:
                self.variables[var_name] = value
                print(f"    {var_name} = {value}")
            else:
                print(f"    ⚠️ Переменная '{var_name}' не объявлена")
        elif target.arr is not None:
            arr_info = self.visit(target.arr)  # (name, index)
            arr_name, idx = arr_info
            if arr_name in self.arrays:
                arr = self.arrays[arr_name]
                pos = idx - arr['lower']
                if 0 <= pos < len(arr['data']):
                    arr['data'][pos] = value
                    print(f"    {arr_name}[{idx}] = {value}")
                else:
                    print(f"    ⚠️ Индекс {idx} вне диапазона массива {arr_name}")
            else:
                print(f"    ⚠️ Массив '{arr_name}' не объявлен")
        else:
            print("    ⚠️ Недопустимая левая часть присваивания")

        return value

    def visitBlockStmt(self, ctx):
        print("    📦 Начало вложенного блока")
        self.visit(ctx.body)
        print("    📦 Конец вложенного блока")
        return None

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.ifStmt.cond)
        print(f"    🎯 Условие: {cond}")
        if cond:
            self.visit(ctx.ifStmt.thenBranch)
        else:
            self.visit(ctx.ifStmt.elseBranch)
        return None

    def visitOutputStmt(self, ctx):
        self.visit(ctx.outStmt.list)
        return None

    def visitOutputList(self, ctx):
        val = self._get_value(ctx.first)
        print(f"    📤 {val}")
        self.output_lines.append(str(val))
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailOutContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTailOut(self, ctx):
        val = self._get_value(ctx.next)
        print(f"    📤 {val}")
        self.output_lines.append(str(val))
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailOutContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTailOut(self, ctx):
        return None

    def visitForStmt(self, ctx):
        var_name = ctx.forLoop.loopVar.text
        init_val = self.visit(ctx.forLoop.initExpr)
        step_op = ctx.forLoop.stepOp.text
        condition_ctx = ctx.forLoop.cond
        body = ctx.forLoop.body

        self.variables[var_name] = init_val
        print(f"    🔄 Цикл for: {var_name} = {init_val}, шаг: {step_op}")

        iterations = 0
        max_iter = 1000
        while iterations < max_iter:
            cond_result = self.visit(condition_ctx)
            if not cond_result:
                break
            self.visit(body)
            if step_op == '++':
                self.variables[var_name] += 1
            elif step_op == '--':
                self.variables[var_name] -= 1
            else:
                break
            iterations += 1

        if iterations >= max_iter:
            print("    ⚠️ Достигнут лимит итераций")
        else:
            print(f"    🔄 Цикл завершён ({iterations} итераций)")

        return None

    def visitLabelStmt(self, ctx):
        return self.visit(ctx.label.innerStmt)

    # ---------- ПЕРЕМЕННЫЕ И КОНСТАНТЫ ----------
    
    def visitVarId(self, ctx):
        return ctx.id.text

    def visitVarConst(self, ctx):
        return self.visit(ctx.const)

    def visitVarArray(self, ctx):
        arr_name = ctx.arr.arrName.text
        if ctx.arr.idx is not None:
            index_val = self._get_value(ctx.arr.idx.element)
            return (arr_name, index_val)
        else:
            return arr_name

    def visitConstInt(self, ctx):
        return int(ctx.intVal.text)

    def visitConstReal(self, ctx):
        return float(ctx.realVal.text)

    def visitConstString(self, ctx):
        return ctx.strVal.text[1:-1]  # убираем кавычки

    def visitConstBool(self, ctx):
        return ctx.boolVal.text == 'true'

    # ---------- ВЫРАЖЕНИЯ ----------
    
    def visitExpression(self, ctx):
        base_val = self._get_value(ctx.base)
        tail = ctx.tail
        if tail and not isinstance(tail, MyLanguageParser.EmptyExprTailContext):
            op = tail.op.text
            right_val = self._get_value(tail.right)
            if hasattr(tail, 'f') and tail.f.continuation is not None:
                # fTail.expression существует — но наша грамматика не поддерживает цепочки
                # Ограничимся одной операцией
                pass
            # Выполняем операцию
            if op == '+':
                return base_val + right_val
            elif op == '-':
                return base_val - right_val
            elif op == '*':
                return base_val * right_val
            elif op == '/':
                if right_val == 0:
                    raise ZeroDivisionError("Деление на ноль")
                return base_val / right_val
            elif op == '^':
                return base_val ** right_val
            elif op == 'or':
                return bool(base_val) or bool(right_val)
            elif op == 'and':
                return bool(base_val) and bool(right_val)
            elif op == 'not':
                return not bool(right_val)
            else:
                raise ValueError(f"Неизвестный оператор: {op}")
        return base_val

    def visitEmptyExprTail(self, ctx):
        return None

    def visitBinaryOp(self, ctx):
        # Не должен вызываться напрямую — обрабатывается в visitExpression
        pass

    # ---------- УСЛОВИЯ ----------
    
    def visitCondition(self, ctx):
        left = self._get_value(ctx.left)
        right = self._get_value(ctx.right)
        op = ctx.op.text
        if op == '=':
            return left == right
        elif op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right
        elif op == '!=':
            return left != right
        return False


# ---------- ФУНКЦИИ ЗАПУСКА ----------
    
def run_code(source_code: str) -> bool:
    input_stream = InputStream(source_code)
    lexer = MyLanguageLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLanguageParser(token_stream)

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        tree = parser.program()

        if error_listener.errors:
            print("\n❌ СИНТАКСИЧЕСКИЕ ОШИБКИ:")
            for err in error_listener.errors:
                print(f"  {err}")
            return False

        print("\n✅ Синтаксический анализ пройден успешно!\n")

        interpreter = MyInterpreter()
        interpreter.visit(tree)

        # Вывод результатов
        print("\n" + "="*50)
        print("📊 РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ")
        print("="*50)

        if interpreter.variables:
            print("\n📌 Переменные:")
            for name, val in interpreter.variables.items():
                print(f"  {name:12} = {val} ({type(val).__name__})")

        if interpreter.arrays:
            print("\n📌 Массивы:")
            for name, arr in interpreter.arrays.items():
                low = arr['lower']
                high = low + len(arr['data']) - 1
                print(f"  {name}[{low}:{high}] ({arr['type']}) = {arr['data']}")

        if interpreter.output_lines:
            print("\n📤 Вывод программы:")
            for line in interpreter.output_lines:
                print(f"  {line}")

        return True

    except Exception as e:
        print(f"\n💥 ОШИБКА ВЫПОЛНЕНИЯ: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=" * 60)
    print("🎯 ИНТЕРПРЕТАТОР MyLanguage (чистая реализация)")
    print("=" * 60)

    if not Path("MyLanguageParser.py").exists():
        print("\n❌ Отсутствуют сгенерированные файлы парсера!")
        print("Выполните: java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor MyLanguage.g4")
        return

    example = """MyProgram: begin
    integer x, y, sum; array integer _arr[1:5]; real pi; bool flag
$
    x = 10;
    y = 20;
    sum = x + y;
    pi = 3.14;
    flag = true;
    output("Сумма:", sum);
    output("Pi =", pi);
    for i = 1; ++ until (i > 5) do {
        _arr[i] = i * 10;
        output("Элемент", i, "=", _arr[i])
    };
    if (sum > 15) then
        output("Сумма > 15!")
    else
        output("Сумма ≤ 15")
end"""

    print("\n📄 Тестовая программа:")
    print(example)
    print("\n" + "="*60)
    print("🚀 ЗАПУСК")
    print("="*60)

    success = run_code(example)

    print("\n" + "="*60)
    if success:
        print("✅ ПРОГРАММА ВЫПОЛНЕНА УСПЕШНО!")
    else:
        print("❌ ВЫПОЛНЕНИЕ ЗАВЕРШЕНО С ОШИБКАМИ!")
    print("="*60)


if __name__ == "__main__":
    main()