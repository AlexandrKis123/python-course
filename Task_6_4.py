

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{name}, {color}')
        self.go(20)
        self.turn()
        self.stop(0)

    def go(self, speed):
        print(f'Машина {self.name} поехала со скоростью {self.speed}')

    def turn(self):
        print(f'Машина {self.name} повернула')

    def stop(self, speed):
        print(f'Машина остановилась {self.name}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    show_speed = 60  #штраф в области PoliceCar
    print(f'Машина поехала со скоростью {show_speed}')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    show_speed = 260
    print(f'Машину камеры не видят.')

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    show_speed = 40  #штраф в области PoliceCar
    print(f'Машина поехала со скоростью {show_speed}')

class PoliceCar(Car, TownCar, WorkCar):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

        while True:
            if TownCar.show_speed > 60 or WorkCar.show_speed > 40:
                print(f'Машина привысила скорость, получите штраф!')
            else:
                break
            print(f'Машина не привышает скорость.')


car1 = TownCar(20, 'Белый', 'Nissan', 'True')
car1 = TownCar('Nissan')
car1.TownCar.show_speed(70)
car1 = PoliceCar
car1.SportCar.show_speed(260)
car1.WorkCar.show_speed(50)
car1 = PoliceCar


