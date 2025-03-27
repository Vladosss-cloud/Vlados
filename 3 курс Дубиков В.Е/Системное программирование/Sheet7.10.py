import math

class Goal:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Gooal(self):
        i = 0
        while i != 5:
            b = int(input('Введите результаты для первого спортсмена'))
            self.x = self.x + b  
            i = i + 1 
        i = 0
        while i != 5:
            c = int(input('Введите результаты для второго спортсмена'))
            self.y = self.y + c
            i = i + 1 
        return self.x, self.y
        
               
calculator = Goal(0,0)

print('Результаты первого и второго = ', calculator.Gooal())
