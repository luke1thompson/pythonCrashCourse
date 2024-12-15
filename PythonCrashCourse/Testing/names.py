from name_func import get_formatted

print("Enter 'q' at any time to quit.")
while True:
    first = input('Give me a first name bitch.\t')
    if first == 'q':
        break
    last = input('Give me a last name bitch.\t')
    if last == 'q':
        break

    formatted = get_formatted(first, last)
    print(f"Here you go, bitch: {formatted}")
