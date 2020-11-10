

class Worker:
    name = 'Иван'
    surname = 'Иванов'
    position = 'Директор'

    def part(self, name, surname, position, wage, bonus, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

class Position (Worker):
    def part(self, name, surname, position, wage, bonus, __income):

        self.get_full_name = name, surname
        self.get_total_income = __income

Work = Worker()
print(Work)
Posit = Position
print()
