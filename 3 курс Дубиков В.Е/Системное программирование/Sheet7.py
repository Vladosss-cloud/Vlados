import math

class Goal:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(f"{self.x:.2}")

calculator = Goal(math.e)

calculator.print()