# Практика к занятию 1. Ввод и вывод данных. 
Пока что мы будем работать в `IDLE`

## Ввод, вывод
Мы упоминали стандартный ввод и вывод. В питоне для работы с ними используются две функции: `input()` - считывает значения из ввода, а `print()` - выводит значения.

У функции `print()` может быть сколько угодно аргументов, она выведет их в стандартный вывод, ставя между ними разделитель (по умолчанию - пробел).

**Упражнение 1.** Выведи строчку `"Hello, world"` с помощью функции `print()`.
  
**Упражнение 2.** Вывод функции `print()` каждый раз начинается с новой строки. Попробуй вывести названия дней недели - каждое на отдельной строке.
  
**Упражнение 3.** Функция `print()` может принимать несколько аргументов, по умолчанию она выведет их через пробел. Например программа:
```python
print("Первый", "Второй", "Третий") # Аргументы функции при записи разделяются запятой.
```
Выведет в Python Shell:
```bash
Первый Второй Третий
```
Измени свой код так, чтобы он выводил названия дней недели через пробел. 

**Упражнение 4.** Пробел - разделитель по умолчанию в функции `print()`. Чтобы изменить разделитель на любое другое значение, например на двоеточие `:`, мы можем указать дополнительный аргумент для функции `print()`, вот так:
```python
print("Первый", "Второй", "Третий", sep=":")
```
Выведет в Python Shell:
```bash
Первый:Второй:Третий
```
Такие аргументы называются **keyword arguments**, или сокращенно **kwargs**, так как мы не просто приводим очередной аргумент через запятую, а указываем имя конкретного аргумента. В данном примере мы говорим, что в функции `print()` аргумент разделитель (separator) с именем `sep` равен символу двоеточия.

Попробуй изменить свой код, чтобы дни недели выводились через запятую, вот так: `Понедельник, Вторник, Среда, ...` и так далее.

**Упражнение 5.** Есть специальный символ переноса строки - `"\n"`, сокращение от newline. Перед буквой `n` стоит обратный слэш - так называемый escape symbol. Он показывает, что следующий за ним знак должен быть воспринят программой не буквально (как буква `n`), а как специальный символ - перенос строки. Также заметь, что этот символ взят в кавычки: важно, что он может находится только внутри строки (либо как отдельная строка из одного символа, в собственных кавычках), иначе он просто не будет распознан. Попробуй использовать этот символ как разделитель в своем коде из упражнения четыре, как теперь выводятся дни недели?

**Упражнение 6.** Символ переноса строки является значением по умолчанию для ключевого аргумента `end` в функции `print()`. Как думаешь, почему? Аргумент принимает значение по умолчанию, если мы не присваиваем ему значение в коде. Ключевой аргумент `end` хранит строку (один или несколько символов), которые добавляются в самом конце вывода функции `print()`. Попробуй изменить параметр `end` в коде предыдущих упражнений (например `end="; "`), что изменилось в результатах выполнения программы?

**Упражнение 7.** Наконец вспомним и про ввод. Функция `input()` считывает строчку текста, введенную пользователем (ввод с клавиатуры производится в окно Python Shell, после запуска программы). `input()` возвращает строчку, которую ввел пользователь, мы можем сохранить ее в переменную, чтобы потом использовать. Для присвоения значения переменной используется оператор `=`, вот так:
```python
# Считываем строчку введенную пользователем и сохраняем ее в переменную name
name = input()
# Можем по имени переменной получить ее значение и вывести на экран 
print(name)
```
Теперь мы можем обратиться к имени пользователя из другой части нашей программы по имени переменной `name`. Напиши программу, которая считывает введенное имя и приветствует пользователя таким образом: `Привет, Егор, осталось всего одно упражнение.`

**Упражнение 8.** Наконец попробуй считать имя и возраст пользователя, и изменить приведенный ниже код, чтобы результат выводился на четырех отдельных строчках:
```python
print("Твое имя:", name, "Твой возраст:", age)
```
```bash
Твое имя:
Валя
Твой возраст:
22
```

