from random import randint

class Die:
    
    def __init__(self, sides=6) -> None:
        self.sides = sides
        
    def roll(self, num = 1):
        total = 0
        for i in range(num):
            total += randint(1, self.sides)
        return total
    