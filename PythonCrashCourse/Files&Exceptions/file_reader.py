from pathlib import Path

# quotepath = Path('C:/Users/Luke1/Documents/Study/PythonCrashCourse/Files&Extensions/reference/quotes.txt')
# print(quotepath.read_text())

# path = Path('../../OdinProj/test.txt')
# print(path.read_text())

# path = Path('pi.txt')
# contents = path.read_text()
# print(contents)

# lines = contents.splitlines()
# pistring = ""
# for line in lines:
#     pistring += line.lstrip()

mypath = Path('reference/pi_million_digits.txt')
try:
    mystring = mypath.read_text()
except FileNotFoundError:
    print('Fuck it didn"t work')

birthday = input("Enter your birthday, in the form: 'mmddyy':")
if birthday in mystring:
    print("Your birthday appears in the first million digits of Pi!")
else:
    print('Looks like you have a loser birthday, loser.')