

class Mistake:
    def __init__(self):
        self.my_list = []

    def input(self):

        while True:
            try:
                value = int(input('Введите данные: '))
                self.my_list.append(value)
                print(f'Список {self.my_list}')
            except:
                print('Не допустимое значение!')
                y_or_n = input('Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                    break


try_except = Mistake()
print(try_except.input())



