#!/usr/bin/env python3
"""
ИНТЕРПРЕТАТОР ДЛЯ MyLanguage (обновлено под новую BNF грамматику)
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
        self.labels = {}     # метки: имя → контекст оператора

    # ---------- ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ----------
    
    def _get_value(self, var_ctx):
        """Получить значение из variable-контекста (ID, константа или массив)."""
        if var_ctx is None:
            raise ValueError("Пустой контекст переменной")
        return self.visit(var_ctx)

    def _get_variable_value(self, var_name):
        """Получить значение переменной по имени."""
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise ValueError(f"Переменная '{var_name}' не объявлена")

    def _set_variable_value(self, var_name, value):
        """Установить значение переменной."""
        if var_name in self.variables:
            self.variables[var_name] = value
        else:
            # Автоматическое объявление при первом использовании
            self.variables[var_name] = value

    # ---------- ПРОГРАММА И БЛОК ----------
    
    def visitProgram(self, ctx):
        prog_name = ctx.name.text
        print(f"[Программа] {prog_name}")
        return self.visit(ctx.block())

    def visitBlock(self, ctx):
        print("[Блок] Начало")
        print("[ОПИСАНИЯ]")
        self.visit(ctx.descList)
        print("--- Разделитель $ ---")
        print("[ОПЕРАТОРЫ]")
        self.visit(ctx.stmtList)
        print("[Блок] Конец")
        return None

    # ---------- ОПИСАНИЯ ----------
    
    def visitDescriptionList(self, ctx):
        self.visit(ctx.first)
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTail(self, ctx):
        self.visit(ctx.next_)
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTail(self, ctx):
        return None

    def visitSimpleDesc(self, ctx):
        simple_desc = ctx.simpleVarDescription()
        var_type = simple_desc.varType.getText()
        self._current_type = var_type
        self.visit(simple_desc.vars_)
        del self._current_type
        return None

    def visitArrayDesc(self, ctx):
        # Обрабатываем обе формы: typedArray и logicArray
        if isinstance(ctx, MyLanguageParser.TypedArrayContext):
            arr_type = ctx.arrType.getText()
            arr_name = ctx.arrName.text
            bounds_ctx = ctx.range_
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
            idx_ctx = ctx.idx
            # Для logic массива нужно сохранить индекс
            print(f"    logic {arr_name}")

        return None

    def visitIdentifierList(self, ctx):
        var_name = ctx.first.text
        self._declare_variable(var_name)
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailIdContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTailId(self, ctx):
        var_name = ctx.next_.text
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
        self.visit(ctx.next_)
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailStmtContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTailStmt(self, ctx):
        return None

    def visitAssignStmt(self, ctx):
        target = ctx.target
        value = self.visit(ctx.expr)

        # Определяем тип целевой переменной
        if isinstance(target, MyLanguageParser.VarIdContext):
            var_name = target.id_.text
            self._set_variable_value(var_name, value)
            print(f"    {var_name} = {value}")
        elif isinstance(target, MyLanguageParser.VarArrayContext):
            # Для массива нужно получить имя и индекс отдельно
            arr_ctx = target.arr
            arr_name = arr_ctx.arrName.text
            idx_ctx = arr_ctx.idx
            
            if isinstance(idx_ctx, MyLanguageParser.IndexWithVarContext):
                # Есть индекс
                index_val = self._get_value(idx_ctx.element)
                if arr_name in self.arrays:
                    arr = self.arrays[arr_name]
                    pos = index_val - arr['lower']
                    if 0 <= pos < len(arr['data']):
                        arr['data'][pos] = value
                        print(f"    {arr_name}[{index_val}] = {value}")
                    else:
                        print(f"    [WARNING] Индекс {index_val} вне диапазона массива {arr_name}")
                else:
                    print(f"    [WARNING] Массив '{arr_name}' не объявлен")
            else:
                print(f"    [WARNING] Массив '{arr_name}' используется без индекса в присваивании")
        else:
            print("    [WARNING] Недопустимая левая часть присваивания")

        return value

    def visitBlockStmt(self, ctx):
        print("    [Блок] Начало вложенного блока")
        self.visit(ctx.body)
        print("    [Блок] Конец вложенного блока")
        return None

    def visitIfStmt(self, ctx):
        if_stmt = ctx.ifStatement()
        cond = self.visit(if_stmt.cond)
        print(f"    [Условие] {cond}")
        if cond:
            self.visit(if_stmt.thenBranch)
        else:
            self.visit(if_stmt.elseBranch)
        return None

    def visitConditionStmt(self, ctx):
        """Оператор-условие (из BNF: <оператор>::= <условие>)"""
        # В ConditionStmtContext cond - это ConditionContext напрямую
        result = self.visit(ctx.cond)
        print(f"    [Условие как оператор] {result}")
        return result

    def visitOutputStmt(self, ctx):
        out_stmt = ctx.outputStatement()
        self.visit(out_stmt.list_)
        return None

    def visitOutputList(self, ctx):
        val = self._get_value(ctx.first)
        print(f"    [Вывод] {val}")
        self.output_lines.append(str(val))
        if ctx.tail and not isinstance(ctx.tail, MyLanguageParser.EmptyTailOutContext):
            self.visit(ctx.tail)
        return None

    def visitNonEmptyTailOut(self, ctx):
        val = self._get_value(ctx.next_)
        print(f"    [Вывод] {val}")
        self.output_lines.append(str(val))
        if ctx.rest and not isinstance(ctx.rest, MyLanguageParser.EmptyTailOutContext):
            self.visit(ctx.rest)
        return None

    def visitEmptyTailOut(self, ctx):
        return None

    def visitForStmt(self, ctx):
        # В новой грамматике loopVar - это variable, а initVal - это constant
        for_stmt = ctx.forStatement()
        loop_var_ctx = for_stmt.loopVar
        init_val = self.visit(for_stmt.initVal)  # теперь constant, а не expression
        step_op = for_stmt.stepOp.getText()
        condition_ctx = for_stmt.cond
        body_ctx = for_stmt.body

        # Получаем имя переменной цикла
        if isinstance(loop_var_ctx, MyLanguageParser.VarIdContext):
            var_name = loop_var_ctx.id_.text
        else:
            raise ValueError("Переменная цикла должна быть идентификатором")

        self._set_variable_value(var_name, init_val)
        print(f"    [Цикл for] {var_name} = {init_val}, шаг: {step_op}")

        iterations = 0
        max_iter = 1000
        while iterations < max_iter:
            cond_result = self.visit(condition_ctx)
            if not cond_result:
                break
            
            # Обрабатываем тело цикла (может быть оператором или goto)
            self.visit(body_ctx)
            
            if step_op == '++':
                self.variables[var_name] += 1
            elif step_op == '--':
                self.variables[var_name] -= 1
            else:
                break
            iterations += 1

        if iterations >= max_iter:
            print("    [WARNING] Достигнут лимит итераций")
        else:
            print(f"    [Цикл] Завершен ({iterations} итераций)")

        return None

    def visitLoopBodyStmt(self, ctx):
        """Тело цикла - оператор"""
        return self.visit(ctx.stmt)

    def visitLoopBodyGoto(self, ctx):
        """Тело цикла - goto <имя метки>"""
        label_name = ctx.labelName.text
        if label_name in self.labels:
            print(f"    [GOTO] Переход к метке {label_name}")
            self.visit(self.labels[label_name])
        else:
            print(f"    [WARNING] Метка '{label_name}' не найдена")
        return None

    def visitLabelStmt(self, ctx):
        label_name = ctx.labelName.text
        # Сохраняем метку для использования в goto
        self.labels[label_name] = ctx.innerStmt
        print(f"    [Метка] {label_name}")
        return self.visit(ctx.innerStmt)

    # ---------- ПЕРЕМЕННЫЕ И КОНСТАНТЫ ----------
    
    def visitVarId(self, ctx):
        var_name = ctx.id_.text
        # Возвращаем значение переменной, а не имя
        return self._get_variable_value(var_name)

    def visitVarConst(self, ctx):
        return self.visit(ctx.const)

    def visitVarArray(self, ctx):
        return self.visit(ctx.arr)

    def visitArrayVariable(self, ctx):
        arr_name = ctx.arrName.text
        idx_ctx = ctx.idx
        
        if isinstance(idx_ctx, MyLanguageParser.IndexWithVarContext):
            # Индекс есть
            index_val = self._get_value(idx_ctx.element)
            if arr_name in self.arrays:
                arr = self.arrays[arr_name]
                pos = index_val - arr['lower']
                if 0 <= pos < len(arr['data']):
                    return arr['data'][pos]
                else:
                    raise IndexError(f"Индекс {index_val} вне диапазона массива {arr_name}")
            else:
                raise ValueError(f"Массив '{arr_name}' не объявлен")
        else:
            # Индекс пустой - возвращаем имя массива для присваивания
            return arr_name

    def visitIndexWithVar(self, ctx):
        return self._get_value(ctx.element)

    def visitIndexEmpty(self, ctx):
        return None

    def visitConstInt(self, ctx):
        return int(ctx.intVal.text)

    def visitConstReal(self, ctx):
        return float(ctx.realVal.text)

    def visitConstString(self, ctx):
        return ctx.strVal.text[1:-1]  # убираем кавычки

    # ---------- ВЫРАЖЕНИЯ ----------
    
    def visitExpression(self, ctx):
        base_val = self._get_value(ctx.base)
        tail = ctx.tail
        
        if tail and not isinstance(tail, MyLanguageParser.EmptyExprTailContext):
            # Есть операция
            op = tail.op.text
            right_val = self._get_value(tail.right)
            
            # Выполняем операцию
            result = self._apply_operation(op, base_val, right_val)
            
            # Проверяем F_tail (может быть продолжением выражения)
            if hasattr(tail, 'f') and tail.f:
                f_tail = tail.f
                if isinstance(f_tail, MyLanguageParser.FTailExprContext):
                    # Есть продолжение выражения
                    continuation = self.visit(f_tail.continuation)
                    # Применяем операцию к результату и продолжению
                    # Но это зависит от приоритета операций - упростим
                    return continuation
                else:
                    # F_tail пустой
                    return result
            else:
                return result
        
        return base_val

    def _apply_operation(self, op, left, right):
        """Применить операцию к двум операндам."""
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Деление на ноль")
            return left / right
        elif op == '^':
            return left ** right
        elif op == 'or':
            return bool(left) or bool(right)
        elif op == 'and':
            return bool(left) and bool(right)
        elif op == 'not':
            return not bool(right)
        else:
            raise ValueError(f"Неизвестный оператор: {op}")

    def visitEmptyExprTail(self, ctx):
        return None

    def visitBinaryOp(self, ctx):
        # Обрабатывается в visitExpression
        pass

    def visitFTailExpr(self, ctx):
        return self.visit(ctx.continuation)

    def visitFTailEmpty(self, ctx):
        return None

    # ---------- УСЛОВИЯ ----------
    
    def visitCondition(self, ctx):
        left = self._get_value(ctx.left)
        right = self._get_value(ctx.right)
        op = ctx.op.getText()
        
        if op == '=' or op == '==':
            return left == right
        elif op == '>':
            return left > right
        elif op == '<':
            return left < right
        else:
            raise ValueError(f"Неизвестный оператор сравнения: {op}")


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
            print("\n[ERROR] СИНТАКСИЧЕСКИЕ ОШИБКИ:")
            for err in error_listener.errors:
                print(f"  {err}")
            return False

        print("\n[OK] Синтаксический анализ пройден успешно!\n")

        interpreter = MyInterpreter()
        interpreter.visit(tree)

        # Вывод результатов
        print("\n" + "="*50)
        print("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ")
        print("="*50)

        if interpreter.variables:
            print("\n[Переменные]")
            for name, val in interpreter.variables.items():
                print(f"  {name:12} = {val} ({type(val).__name__})")

        if interpreter.arrays:
            print("\n[Массивы]")
            for name, arr in interpreter.arrays.items():
                low = arr['lower']
                high = low + len(arr['data']) - 1
                print(f"  {name}[{low}:{high}] ({arr['type']}) = {arr['data']}")

        if interpreter.output_lines:
            print("\n[Вывод программы]")
            for line in interpreter.output_lines:
                print(f"  {line}")

        return True

    except Exception as e:
        print(f"\n[ERROR] ОШИБКА ВЫПОЛНЕНИЯ: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=" * 60)
    print("ИНТЕРПРЕТАТОР MyLanguage (обновлено под новую BNF)")
    print("=" * 60)

    if not Path("MyLanguageParser.py").exists():
        print("\n[ERROR] Отсутствуют сгенерированные файлы парсера!")
        print("Выполните: java -jar C:\\antlr\\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor MyLanguage.g4")
        return

    example = """MyProgram: begin
    integer x, y, sum;
    array integer _arr[1:5];
    real pi
$
    x = 10;
    y = 20;
    sum = x + y;
    pi = 3.14;
    output("Сумма:", sum);
    output("Pi =", pi);
    for x = 1; ++ until (x > 5) do {
        _arr[x] = x * 10;
        output("Элемент", x, "=", _arr[x])
    };
    if (sum > 15) then
        output("Сумма > 15!")
    else
        output("Сумма <= 15")
end"""

    print("\n[Тестовая программа]")
    print(example)
    print("\n" + "="*60)
    print("[ЗАПУСК]")
    print("="*60)

    success = run_code(example)

    print("\n" + "="*60)
    if success:
        print("[OK] ПРОГРАММА ВЫПОЛНЕНА УСПЕШНО!")
    else:
        print("[ERROR] ВЫПОЛНЕНИЕ ЗАВЕРШЕНО С ОШИБКАМИ!")
    print("="*60)


if __name__ == "__main__":
    main()
