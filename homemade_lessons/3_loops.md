# Занятие 3 - Циклы for и while

Рассмотрим блок-схемы двух циклов. Вводятся два числа `x` - основание и `p` - показатель. Цикл возводит `x` в степень `p`.

![loops](https://user-images.githubusercontent.com/33204359/204267617-c8b57410-0dd6-403f-8d0c-fb3f36a42cc9.png)


## For

Цикл `for` применяется чаще применяется в случаях, где точно известно число итераций.

Цикл `for` автоматически проходит по набору значений: списку, диапазону чисел, буквам строки и заканчивает свое выполнения, когда не остается элементов в последовательности, по которой он проходит.

> Часто нужно провести итерацию определенное число раз, но само значение счетчика нам не нужно. Чтобы не создавать лишнюю переменную и упростить понимание кода можно использовать такой виде цикла: `for _ in ...`. Нижнее подчеркивание показывает, что нам не важно куда сохраняется очередное значение итератора.

Взять каждое из чисел диапазона от одного до `n` и вывести его на экран если `n` делится на это число (`i`) без остатка.
```python
n = int(input())

for i in range(1, n):
    if n % i == 0:
        print(n)
```

### Использование функции `range`. 
```python
range(5) #-> [0, 5)
range(2, 5) #-> [2, 5)
range(1, 100, 5) #-> [1, 100) с шагом 5
```


## While

Цикл `while` применяется в случаях, где необходимо продолжать итерации пока соблюдается какое-либо условие.

Условие в `while` проверяется перед каждым очередным запуском цикла. Важно не забывать обновлять переменную, значение которой проверяется в условии в теле цикла.

```python
x = int(input())
p = int(input())
result = 1

while p > 0:
    result *= x  # сокращение от result = result * x
    p -= 1       # сокращение от p = p - 1
```


# Упражнения
1. Программа получает на вход число `n` и выводит все числа от 1 до `n`, которые являются делителями `n`.
2. Программа получает на вход число `n` и выводит числа Фибоначчи от 1 до `n`
3. Программа получает на вход строку и выводит ее задом-наперед
4. [Черепашка от МФТИ](http://cs.mipt.ru/python/lessons/lab2.html#o2-s)
