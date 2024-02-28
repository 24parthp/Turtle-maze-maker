import turtle as t
import random as rand

wn = t.Screen()
wn.setup(500,500)

mazePointer = t.Turtle()
mazePointer.pensize(8)
mazePointer.speed(0)

def drawMaze(pointer):
    len = 400
    num_of_walls = 21
    wall_distance = 20

    def startingPosition(turtle):
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

drawMaze(mazePointer)

wn.mainloop()