import random
age = random.randint(0,90)

if age < 2:
    message = 'You are just a baby!'
elif age < 4:
    message = 'You are a toddler.'
elif age < 13:
    message = 'You are a kid.'
elif age < 20:
    message = 'You are a teenager.'
elif age < 65:
    message = 'You are an adult.'
else:
    message = 'You are an old fart.'

print(f"You are {age} year(s) old. {message}")