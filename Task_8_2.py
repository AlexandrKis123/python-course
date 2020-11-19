

class Divider:

    def __init__(self, number, number2):
        self.number = number
        self.number2 = number2

    @staticmethod
    def divider2(number, number2):
        try:
            return (number / number2)
        except:
            print('Деление на ноль.')


div = Divider(100, 0)
print(div.divider2(10, 0.1))
print(div.divider2(100, 0))

