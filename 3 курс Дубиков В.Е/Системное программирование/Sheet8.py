import math
a = int(input('Введите число:'))
class Goal:
    def __init__(self, x):
        self.x = x

    def print(self):
        print('Вы ввели число:', self.x)

calculator = Goal(a)

calculator.print()