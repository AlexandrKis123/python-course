#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
#натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них.

my_list = [8, 6, 6, 5, 5, 2]
number = int(input('Введите число: '))
i = 0
for n in my_list:
    if number <= n:
        i += 1
my_list.insert(i, number)
print(my_list)