import turtle as t
import random as rand
import threading

wn = t.Screen()
wn.setup(500,500)

mazePointer, playerPointer = t.Turtle(), t.Turtle()
mazePointer.pensize(8)
mazePointer.speed(0) , playerPointer.speed(0)


def drawMaze(pointer):
    len = 400
    num_of_walls = 21
    wall_distance = 20

    def startingPosition(turtle):
        pointer.hideturtle()
        pointer.penup()
        pointer.seth(270)
        pointer.goto(200,200)
        pointer.pendown()

    def wall(distance):
        if distance >= 50:
            pathway = rand.randint(10, distance-40)
            if (pathway >= 70):
                wallbefore = rand.randint(0, pathway-10)
                walldistancebefore = pathway - wallbefore
            else:
                walldistancebefore = distance
        
            pointer.fd(walldistancebefore)

            pointer.right(90)
            pointer.fd(40)
            pointer.left(180)
            pointer.fd(40)
            pointer.right(90)

            pointer.fd(pathway-walldistancebefore)

            pointer.penup()
            pointer.fd(30)
            pointer.pendown()

            pointer.fd(len-pathway)
    
    def powerup():
        xpos = rand.randint(-190, 190)
        ypos = rand.randint(-210, 150)
        pointer.penup()
        pointer.goto(xpos, ypos)
        pointer.pendown()
        pointer.color("red")
        pointer.circle(2)

    startingPosition(pointer)

    for i in range(num_of_walls):
        wall(len)
        len-= wall_distance
        pointer.right(90)

    powerup()

def player(pointer):
    movementSpeed = 10

    def startingPosition():
        pointer.hideturtle()
        pointer.penup()
        pointer.goto(0, 200)
        pointer.pendown()
        pointer.color("blue")
        pointer.pensize(10)
        pointer.circle(5)
        
    def move(key):
        if key == 'w':
            pointer.seth(90)
            pointer.fd(movementSpeed)
        if key == 'a':
            pointer.seth(180)
            pointer.fd(movementSpeed)
        if key == 's':
            pointer.seth(270)
            pointer.fd(movementSpeed)
        if key == 'd':
            pointer.seth(0)
            pointer.fd(movementSpeed)
    
    wn.onkey(lambda: move('w'), 'w')
    wn.onkey(lambda: move('a'), 'a')
    wn.onkey(lambda: move('s'), 's')
    wn.onkey(lambda: move('d'), 'd')
    
    
    startingPosition()

drawMaze(mazePointer)
player(playerPointer)

wn.listen()
wn.mainloop()