#4. Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y. Задание необходимо
#реализовать в виде функции my_func(x, y). При решении задания необходимо
#обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами.
#Первый — возведение в степень с помощью оператора **.
#Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func (x, y):
    res = 1
    for _ in range(abs(y)):
        res *= 1 / x
    return (f'Результат: {round(res, 6)}')

x=float(input('Введите положительное число: '))
y=int(input('Введите отрицательное число: '))

print(my_func(x, y))

"""Вариант 2"""
def my_func (x, y):
    res = x ** y                    #   res = pow(x, y)
    print(f'Результат: {res}')

my_func(x=int(input('Введите положительное число: ')),
        y=int(input('Введите отрицательное число: ')))



