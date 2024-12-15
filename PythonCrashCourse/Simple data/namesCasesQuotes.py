quote = '"The only way the magic works is by hard work. But hard work can be fun."'
quoter = 'jim henson'

print(f'{quoter.title()} once said: {quote}')

name = '\t\nbigmouthbillybass\n'
name1 = name.lstrip()
name2 = name.rstrip()
name = name.strip()

print(f'name1 is {name1}')
print(f'name2 is {name2}')
# print(f'name3 is {name3}')

print(name.removeprefix('bigmouth'))
print(name.removesuffix('bass'))

DONTCHANGE, x, y = 20, 10, 5

print(DONTCHANGE + x + y)

print(3+5)
print(100-92)
print(2*2*2)
print(32/4)