# Это нужно чуть отложить

## Настройка окружения разработки

2. Git for windows - https://gitforwindows.org/
3. VS Code - https://code.visualstudio.com/
4. Активируем виртуальное окружение - `source venv/bin/activate`
4. Устанавливаем библиотеки python - `pip install -r requirements.txt`

## Атомарные типы данных, переменные, операторы
Типы данных `int, float, bool, str`

Переменная - ссылка на объект в памяти. В питоне все представлено в виде объектов. Класс можно представлять как тип, объект - как экземпляр типа.

Присваивание: `=`
Математические операторы: `* / + - **`
Операторы сравнения: `> < >= <= == !=`
Арифметика остатков: `// %`
Бинарные операторы: `& | ^`

### Тестирование решений

Работаем в терминале. Создаем папку с решениями:
```bash
mkdir problems
cd problems
touch hello_world.py
```

Пишем тесты для проверки своей первой функции!
```python
def test_hello_world():
    assert hello_world() == "hello, world!"
```

Пишем свою первую функцию и проверяем решение.
```bash
python test_solution.py hello_world
```

