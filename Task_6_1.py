
from time import sleep

class TrafficLight:
    __color = 'Желтый'
    sleep(2)

    def running(self):
        print('Красный')
        sleep(7)

    def running_1(self):
        print('Зеленый')
        sleep(4)


launch = TrafficLight()
launch.running()
print(launch._TrafficLight__color)
print(launch)
launch.running_1()
print(launch.running_1)

"""
Не могу убрать надписи при выводе!!!
Вывод происходит:
Красный
Желтый
<__main__.TrafficLight object at 0x01340FD0>    - вот это
Зеленый
<bound method TrafficLight.running_1 of <__main__.TrafficLight object at 0x01340FD0>>   - и это
"""