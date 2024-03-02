import turtle as t
import random as rand
import math
from tkinter import *

wn = t.Screen()
wn.setup(500,500)

mazePointer, playerPointer = t.Turtle(), t.Turtle()
mazePointer.pensize(8)
mazePointer.speed(0) , playerPointer.speed(0)

powerup_amount = 0

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
    
    

    startingPosition(pointer)

    for i in range(num_of_walls):
        wall(len)
        len-= wall_distance
        pointer.right(90)

class powerup:
    def __init__(self, pointer):
        self.xpos, self.ypos =  rand.randint(-190, 190), rand.randint(-210, 150)
        self.pointer = pointer

    def draw(self):
        self.pointer.penup()
        self.pointer.goto(self.xpos, self.ypos)
        self.pointer.pendown()
        self.pointer.color("red")
        self.pointer.circle(2)
    
    # def capture(self):

def player(pointer):
    movementSpeed = 10

    def startingPosition():
        pointer.penup()
        pointer.goto(0, 200)
        pointer.color("blue")
        pointer.shape('circle')
        pointer.shapesize(0.5, 0.5)
        pointer.pensize(10)
    
    def dist(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
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

        if(dist(pointer.xcor(), pointer.ycor(), powerup1.xpos, powerup1.ypos) < 11):
            print('yes it works')

        wn.ontimer(lambda: update_powerup_label(label2), 100)
    
    wn.onkeypress(lambda: move('w'), 'w')
    wn.onkeypress(lambda: move('a'), 'a')
    wn.onkeypress(lambda: move('s'), 's')
    wn.onkeypress(lambda: move('d'), 'd')
    
    startingPosition()

def powerupWn():
    global label2

    window = Tk()
    window.geometry('200x100+400+400')

    label = Label(window, text='Number of Powerups:', font=('Arial', 15))
    label2 = Label(window, text=str(powerup_amount), font=('Arial', 25))

    label.pack()
    label2.pack()

def update_powerup_label(label):
    label.config(text=str(powerup_amount))

powerup1 = powerup(mazePointer)

drawMaze(mazePointer)
powerup1.draw()
powerupWn()
player(playerPointer)

wn.listen()
wn.mainloop()