class Dog:
    # A simple attempt to model a dog
    
    def __init__(self, name, age, breed):
        # Initialize attributes
        self.name = name.title()
        self.age = age
        self.dogyears = age * 7
        self.breed = breed
        
    def sit(self):
        print(f"{self.name} sat down.")
    
    def come(self):
        if self.age > 10:
            print(f"{self.name} is too old for that!")
        else:
            print(f"{self.name} just came all over the nice carpet.")
            
mydog = Dog('freckles', 20, 'Australian sheppard mix')
yourdog = Dog('jimmy', 3, 'white boi')
print(f"My dog's name is {mydog.name}.")
print(f"He is {mydog.age} years old, which is {mydog.dogyears} in dog years.")
mydog.sit()
yourdog.come()
print(f"Why do you call your dog {yourdog.name}? Is {yourdog.breed} a real breed?")