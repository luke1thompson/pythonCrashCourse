from turtle import Turtle
import random

# turtle = {'turt': Turtle(), 'id':0, 'pos':0, 'color':'green', 'ai':'s&s'}

def race(turtlist):
    winner = False
    rivalpos = 0
    print(f"The race begins with {len(turtlist)}!")
    for i in range(len(turtlist)):
        myturt = turtlist[i]['turt']
        myturt.color(turtlist[i]['color'])
        myturt.home()
        myturt.fd(i*20)
        myturt.rt(90)
    while not winner:
        for turtle in turtlist:
            move = whatdo(turtle['ai'], turtle['pos'], rivalpos)
            turtle['pos'] += move
            turtle['turt'].fd(move)
            if turtle['pos'] > 200:
                winner = turtle['ai']
                break
            rivalpos = turtle['pos']
    turtlist[0]['turt'].screen.exitonclick()
            
    print(f'The winner is {winner}!')
            
def whatdo(ai, pos, rivalpos):
    match ai:
        case 'smart':
            if rivalpos > pos:
                return 6
            else:
                return random.randint(2,4)
        case 's&s':
            if pos < 50:
                return 2
            elif pos < 120:
                return 4
            else:
                return 6
        case _:
            return 3
        
def turtlelist(size):
    turtlist = []
    i = 0
    while i < size:
        j = Turtle()
        myturt = {'turt':j, 'id':i, 'pos':0}
        if i%2 == 0:
            myturt['color'] = 'green'
            myturt['ai'] = 'smart'
        else:
            myturt['color'] = 'blue'
            myturt['ai'] = 's&s'
        turtlist.append(myturt)
        i += 1
    return turtlist

mylist = turtlelist(4)
# print(mylist)
race(mylist)
print('complete')