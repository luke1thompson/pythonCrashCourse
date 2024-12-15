from random import randint
from random import choice

class User:
    
    def __init__(self, last, first) -> None:
        self.lastname = last.title()
        self.firstname = first.title()
        self.id = randint(10000,99999)
        
    def describe_user(self):
        message = (
            f"This user is: {self.firstname} {self.lastname}. Their id #"
            f" is {self.id}. I hear they are a nice guy."
        )
        print(message)
        
    def greet_user(self):
        print(f"Hello {self.firstname}, welcome online.")
        

class Admin(User):
    
    def __init__(self, last, first) -> None:
        super().__init__(last, first)
        self.privileges = Privileges()
    
            
class Privileges:
    
    def __init__(self) -> None:
        self.privileges = [
            'create posts',
            'delete posts',
            'ban users'
        ]

    def show_privileges(self):
        for thing in self.privileges:
            print(f"This user can {thing}")
        
    
class Dice:
    
    def __init__(self, sides) -> None:
        self.sides = sides
        
    def roll(self):
        print(f"You rolled a {randint(1,self.sides)}!")
        
class Lottery:
    def __init__(self) -> None:
        self.lotlist = ['a', 'b', 'c', 'd', 'e']
        for i in range(10):
            self.lotlist.append(i)
        self.draw = []
    
    def seelist(self):
        print(self.lotlist)
        
    def drawing(self):
        drawlist = []
        while len(drawlist) < 4:
            drawing = choice(self.lotlist)
            if drawing not in drawlist:
                drawlist.append(drawing)
        self.draw = drawlist
        print(self.draw)

        
    def tickettest(self, a, b):
        count = 1
        while True:
            self.drawing()
            if a in self.draw and b in self.draw:
                print(f'Winner Winner Chicken Dinner! It only took you {count} tries!')
                break
            count += 1
            if count > 100:
                print('Program has looped unsuccessfully 100 times. Process terminated.')
                break
            
mylott = Lottery()
mylott.tickettest(1, 6)