import turtle as t

def drawSpiral():
    for x in range(20):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(x)
            t.right(30)

def drawStar():
    t.color('red')
    t.fillcolor('yellow')
    t.begin_fill()
    turn = 160
    angle = abs(180 - turn)
    points = 0
    
    while True:
        points += 1
        t.forward(100)
        t.left(turn)
        if abs(t.pos()) < 1:
            break
    
    t.end_fill()
    return (angle, points)

(angle, points) = drawStar()
t.exitonclick()
print(f"The star had {points} points at an angle of {angle}.")