

class Road:
    _length = int(input('Введите длину: '))
    _width = int(input('Введите ширину: '))

#    def __init__(self, length, width):
#        self.length = length
#        self.width = width

    weight = 25 #киллограммы
    the_thickness_of_the_fabric = 5 #сантиметры

    # формула вычисления
    summa_asphalt_m2 = float(weight * the_thickness_of_the_fabric) / 1000    #метр квадратный асфальта
    summa = (_length * _width * summa_asphalt_m2)
    print(f'{summa}, тонн')

Road()