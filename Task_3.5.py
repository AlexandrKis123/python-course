#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
#Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел, то вначале нужно добавить
#сумму этих чисел к полученной ранее сумме и после этого завершить программу.



def sum():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Введите числа в строку или введите "Q" для выхода: ').split()
        res = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res += float(num)
        result += res
    print(f'Сумма чисел: {result}')


sum()

