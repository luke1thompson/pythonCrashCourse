from pathlib import Path

# print("Please input two numbers, one at a time.")
# print("Enter 'q' to quit.")

while True:
    first = input("Please enter the first number:")
    if first == 'q':
        break
    second = input("Please enter the second number:")
    if second == 'q':
        break
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("That's not an integer!")
    else:
        print(answer)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You stuttering moron, you can"t divide by zero!')