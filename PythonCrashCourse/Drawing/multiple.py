from turtle import Turtle
from random import random

# bob = t()
# bob.screen.title('Please leave me alone')
# bob.screen.bgcolor('light green')
# bob.color('red')
# for i in range(30):
#     steps = int(random()*100)
#     angle = int(random()*30)
#     bob.right(angle)
#     bob.fd(steps)
#     if abs(bob.pos()) > 300:
#         bob.home()
#         print('You strayed too far!')

def randomlist(size):
    randolist = []
    for i in range(size):
        randolist.append(int(random()*90)-45)
    print(randolist)
    return(randolist)

def zigzag(angle, size):
    zlist = [angle]
    pos = False
    for i in range(size):
        if pos:
            zlist.append(angle * 2)
        else:
            zlist.append(angle * -2)
        pos = not pos
    if len(zlist) % 2 == 1:
        zlist.pop()
    return zlist

def downstripes(anglist, number = 3, width = 20):
    colors = ['red', 'blue', 'green', 'orange', 'purple']
    turtles =[]
    for stripes in range(number):
        t = Turtle()
        t.penup()
        t.fd(stripes*width)
        t.rt(90)
        t.color(colors[stripes%5])
        t.pendown()
        for angle in anglist:
            t.rt(angle)
            t.fd(10) 
        turtles.append(t)
    return turtles

def allcircle(tlist):
    for t in tlist:
        for i in range(12):
            t.fd(20)
            t.rt(30)
    t.screen.exitonclick()

mylist = zigzag(50, 10)
turtles = downstripes(mylist, 4)
allcircle(turtles)

