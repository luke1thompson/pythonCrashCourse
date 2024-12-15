pizzas = []
flag1 = True

while flag1:
    name = input("It's pizza time! What is your name?\n")
    name = name.title()
    size = input("Let's start with the size! What'll it be?\n")
    toppings = []
    while True:
        topping = input("Can't forget the toppings! Enter 'done' when you are!\n")
        if topping == 'done':
            break
        toppings.append(topping)
    crust = input(f"Finally, what kind of crust did you want {name}?\n")
    pizza = {'name':name, 'size':size, 'toppings':toppings, 'crust':crust}
    pizzas.append(pizza)
    confirm = input('Would you like to make another Za?\n').lower()
    if confirm == 'no' or confirm == 'nope' or confirm == 'nah':
        flag1 = False
        
print("\n----------------IT'S PRINTING TIME BITCH--------------------\n")
for pizza in pizzas:
    for key, value in pizza.items():
        if type(value) == list:
            print(f"The {key} are:")
            for item in value:
                print(f"-{item}")
        else:
            print(f"The {key} is {value}")