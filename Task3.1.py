#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
#выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def dev (a, b):
    try:
        res = a / b
        print(f'Результат: {res}')
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'ZeroDivisionError'

dev(a=int(input('a: ')), b=int(input('b: ')))


def div(*args):

    try:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        res = num_1 // num_2
    except ZeroDivisionError:
        return"Деление на ноль"

    return res


print(div())
"""
#Второй вариант:
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def div(a, b):                                 #Рабочий вариант, но ошибка не работает.
    print(f'Результат: {a / b}')
    except ZeroDivisionError:
    print("Деление на ноль")
div(4,2)
    #except ZeroDivisionError:
#print("Деление на ноль")
"""