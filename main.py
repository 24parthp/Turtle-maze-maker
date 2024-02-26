import turtle as t

wn = t.Screen()
wn.setup(500,500)

mazePointer = t.Turtle()
mazePointer.pensize(8)

def startingPosition(pointer):
    pointer.penup()
    pointer.seth(270)
    pointer.goto(200,200)
    pointer.pendown()

def drawMaze(pointer):
    len = 400
    num_of_walls = 21
    wall_distance = 20

    def wall(distance):
        pointer.fd(distance)

    for i in range(num_of_walls):
        wall(len)
        len-= wall_distance
        pointer.right(90)

startingPosition(mazePointer)
drawMaze(mazePointer)

wn.mainloop()