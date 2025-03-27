import math

class Goal:

    def __init__(self, x):
        self.x = x
    
    def Gooal(self):
        i = 0
        self.x = 0
        while i != 12:
            b = int(input('Введите число'))
            self.x = self.x + b  
            i = i + 1
        return self.x
               
calculator = Goal(0)

print(calculator.Gooal())
