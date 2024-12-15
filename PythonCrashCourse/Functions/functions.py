def friendly_greeting(name=None, weakness='stupid', secret='gay'):
    if name:
        name = name.title()
    print(f"Hey {name}! Yeah I'm talking to you, don't pretend you can't hear me!")
    print(f"Fuck you {name}, everyone knows that you're really just a {weakness}, {secret} person!")

# friendly_greeting('jimbo joseph jones')
# friendly_greeting()
# friendly_greeting('Ronald', 'drug-addicted', 'small penis'

upcoming = ['buy butter', 'kill dad', 'invade pakistan']
complete = ['consume tomato', 'deny god', 'let em rip']
inprogress = ['8/14/2024', 'prove innocence', 'probe uranus']

def shuffle(list, newitem=None):
    if not newitem:
        temp = list.pop()
    else:
        temp = list[-1]
        x = len(list) - 1
        while x > 0:
            print(list[x])
            list[x] = list[x-1]
            x -= 1
        list[0] = newitem
        
    return temp

def dowork(upcoming, inprogress, complete):
    temp = shuffle(upcoming)
    temp = shuffle(inprogress, temp)
    temp = shuffle(complete, temp)
    complete.append(temp)
    
def tasklist(a, b, c):
    print('\nYour tasks are:')
    print(f"Upcoming:{a}\nIn Progress:{b}\nComplete:{c}\n")
    
def addthings (list, *things):
    for item in things:
        list.append(item)

# print(inprogress)
# print(shuffle(inprogress, 'stop being so dumb'))
# print(inprogress)

# tasklist(upcoming, inprogress, complete)
# dowork(upcoming, inprogress, complete)
# tasklist(upcoming, inprogress, complete)

print(upcoming)
addthings(upcoming, 'worship the sun', 'make poopies', 'build communism')
print(upcoming)