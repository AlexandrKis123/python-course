#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
#проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


lists = ['name', 123, 2.2, True]
for el in lists:
    print(type(el))