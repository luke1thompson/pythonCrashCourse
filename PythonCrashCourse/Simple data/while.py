message = input('Tell me things! Enter "no" to quit.\n')

while message != 'no':
    message = input("That's very interesting! Do you have anything else to say?\n")

print('Until next time!')

# Only print odd numbers less than 10
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)