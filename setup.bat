@echo off
echo ========================================
echo ГЕНЕРАЦИЯ ПАРСЕРА ANTLR
echo ========================================

echo 1. Проверяем установку ANTLR...
where antlr4 >nul 2>nul
if %errorlevel% neq 0 (
    echo Ошибка: ANTLR4 не найден!
    echo Установите:
    echo 1. Скачайте antlr-4.13.0-complete.jar с https://www.antlr.org/download.html
    echo 2. Поместите в C:\antlr\antlr-4.13.0-complete.jar
    echo 3. Добавьте в PATH
    pause
    exit /b 1
)

echo 2. Генерируем парсер...
antlr4 -Dlanguage=Python3 -visitor MyLanguage.g4

echo 3. Проверяем созданные файлы...
if exist MyLanguageLexer.py (
    echo ✅ MyLanguageLexer.py создан
) else (
    echo ❌ MyLanguageLexer.py не создан
)

if exist MyLanguageParser.py (
    echo ✅ MyLanguageParser.py создан
) else (
    echo ❌ MyLanguageParser.py не создан
)

if exist MyLanguageVisitor.py (
    echo ✅ MyLanguageVisitor.py создан
) else (
    echo ❌ MyLanguageVisitor.py не создан
)

if exist MyLanguageListener.py (
    echo ✅ MyLanguageListener.py создан
) else (
    echo ❌ MyLanguageListener.py не создан
)

echo.
echo ========================================
echo Сгенерированные файлы:
dir *.py | findstr "MyLanguage"
echo ========================================

echo.
echo Готово! Теперь запускайте: python main.py
pause