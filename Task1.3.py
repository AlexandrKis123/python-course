#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')
nn = int(n + n)
nnn = int(n + n + n)
int_n = int(n)
summa = int(int_n + nn + nnn)
print(summa)