#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
#обмениваются элементы с индексами
#0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().


my_lists = input('Введите цифры: ').split()

for i in range(1, len(my_lists), 2):
    my_lists.insert(i - 1, my_lists.pop(i))
    print(my_lists)
