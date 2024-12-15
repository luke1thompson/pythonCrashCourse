def make_pizza(size, *toppings):
    print(f"Alrighty boys we brewing up a {size}-inch pizza complete with:")
    for topping in toppings:
        if topping == toppings[-1]:
            print(f"- and a hearty helping of {topping} on top.")
        else:
            print(f"- {topping},")

  
def big_fat_gratuitous_function(
        parameter_zero, parameter_one, parameter_two, parameter_three,
        parameter_four, parameter_five):
    return 'You fool! You idiotic, dimwitted moron!'