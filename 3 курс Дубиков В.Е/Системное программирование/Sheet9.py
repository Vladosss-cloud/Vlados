import math
class Goal:
    def __init__(self, x):
        self.x = x

    def Goal(self):
        y = 17 * self.x**2 - 6*self.x + 13
        print(y)
        
calculator = Goal(5)

calculator.Goal()

