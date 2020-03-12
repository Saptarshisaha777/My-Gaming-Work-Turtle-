import turtle
import collections
import queue
import time
from turtle import *

bgcolor("black")
pencolor("white")
title("MICRO MOUSE GAME")
setup(800,800)
up()
pensize()

nums = queue.Queue()
nums.put("")
start_x=0
start_y=0


#pen = turtle.Turtle()
#pen.speed(0)
#pen.hideturtle()
#goto(-400,0)
#pen.down()
#pen.forward(800)
#pen.up()
#goto(0,0)
hideturtle()
speed(20)
up()

####################### SET GUI ##################################


##############################################################################

def clr_screen():
    goto(-175, -310)
    down()
    fillcolor('green')
    begin_fill()
    for i in range(2):
        forward(30)
        left(90)
        forward(350)
        left(90)
    end_fill()
    up()
    return


def set_red(row,column):
    goto((column * 100) - 400, -(row * 100) + 300)
    down()
    fillcolor('red')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    up()
    return

def set_blue(row,column):
    goto((column * 100) - 400, -(row * 100) + 300)
    down()
    fillcolor('blue')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    up()
    return

def set_green(row,column):
    goto((column * 100) - 400, -(row * 100) + 300)
    down()
    fillcolor('green')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    up()
    return

def set_yellow(row,column):
    goto((column * 100) - 400, -(row * 100) + 300)
    down()
    fillcolor('yellow')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    up()
    return

def set_purple(row,column):
    goto((column * 100) - 400, -(row * 100) + 300)
    down()
    fillcolor('purple')
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    up()
    return

#BUTTON
k=0
for j in range(0,800,200):
    goto(-390+j,320)
    k=k+1
    down()
    if k==1:
       fillcolor('red')
    elif k==2:
        fillcolor('blue')
    elif k==3:
        fillcolor('green')
    elif k==4:
        fillcolor('purple')
    begin_fill()
    for i in range(2):
        down()
        forward(80)
        left(90)
        forward(30)
        left(90)
    end_fill()
    up()


goto(-383,326)
down()
write("SET Walls",font=('Arial',12,"normal"))
up()

goto(-183,326)
down()
write("SET Start",font=('Arial',12,"normal"))
up()

goto(17,326)
down()
write("SET Goal",font=('Arial',12,"normal"))
up()

goto(217,326)
down()
write("START",font=('Arial',12,"normal"))
up()


#Horizontal BArs
y=400
while y != 00:
    if y==400:
        goto(-400, y - 400)
        down()
        forward(800)
        up()
        y=y-100
        continue
    else:
       goto(-400,y)
       down()
       forward(800)
       up()
       goto(-400,y-400)
       down()
       forward(800)
       up()
       y=y-100


#VERTICAL BARS
x=400
while x != 00:
    goto(x,300)
    setheading(-90)
    down()
    forward(600)
    up()
    goto(x-400,300)
    down()
    forward(600)
    up()
    x=x-100
    if x == 0:
        goto(- 400, 300)
        down()
        forward(600)
        up()

goto(0,0)

goto(-400, 375)
down()
write("DOUBLE CLICK ON BUTTONS TO ACCESS", font=('Comic Sans', 18, "normal"))
up()

###########################################################################################

###################    SET INPUT    ###########################

grid = [[0 for i in range(8)] for  j in  range(6)]

def set_grid(x,y):
    print("You clicked", int(x), ",", int(y),"in set grid")

    onscreenclick(clicked_grid)
    return


def set_start(x,y):
    global start_y,start_x
    if x in range(-400,400) and y in range(-300,300):
      row = int((300 - y) // 100)
      column = int((x + 400) // 100)
      # print("You clicked",row,",",column)
      grid[row][column] = 'O'
      start_y=row
      start_x=column
      print(start_x,start_y,"in set start")
      print(grid)

      set_blue(row,column)

    else:
        onscreenclick(clicked_button)


def set_goal(x,y):
    if x in range(-400,400) and y in range(-300,300):
       row = int((300 - y) // 100)
       column = int((x + 400) // 100)
       # print("You clicked",row,",",column)
       grid[row][column] = 'X'
       print(grid)

       set_green(row,column)




    else:
        onscreenclick(clicked_button)


#SET GRID OBSTACLES
def clicked_grid(x,y):
    print("You clicked",int(x),",",int(y),"in clicked grid")
    if x in range(-400,400) and y in range(-300,300):
        row = int((300 - y) // 100)
        column = int((x + 400) // 100)
        # print("You clicked",row,",",column)
        grid[row][column] = '#'
        print(grid)

        set_red(row,column)

        onscreenclick(clicked_grid)
    else:

        onscreenclick(clicked_button)
    

####################################################################
maze=grid

print()


#def printMaze(maze,path=""):
#    #for y in range(6):
#    # for x in range(8):
#    #    if maze[y][x] == "O":
#    #        start = x
#    #        start_y=y
#            #print(start)
#            #print(maze)
#
#    i = start_x
#    j = start_y
#    pos = set()
#    for move in path:
#        if move == "L":
#            i -= 1
#
#        elif move == "R":
#            i += 1
#
#        elif move == "U":
#            j -= 1
#
#        elif move == "D":
#            j += 1
#        pos.add((j, i))
#
#    for j, row in enumerate(maze):
#        for i, col in enumerate(row):
#            if (j, i) in pos:
#                #set_yellow(j,i)
#                print("+   ", end="")
#            else:
#                print(col, "  ", end="")
#        print()
#
#    while len(pos):
#        (x,y)=pos.pop()
#        set_yellow(x,y)
#
#
#def valid(maze, moves):
#    #for y in range(6):
#    # for x in range(8):
#    #    if maze[y][x] == "O":
#    #        start = x
#    #        start_y=y
#            #print(start)
#            #print(maze)
#
#    i = start_x
#    j = start_y
#    for move in moves:
#        if move == "L":
#            i -= 1
#
#        elif move == "R":
#            i += 1
#
#        elif move == "U":
#            j -= 1
#
#        elif move == "D":
#            j += 1
#
#        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
#            return False
#        elif (maze[j][i] == "#"):
#            return False
#
#    return True
#
#
#def findEnd(maze, moves):
#    #for y in range(6):
#    # for x in range(8):
#    #    if maze[y][x] == "O":
#    #        start = x
#    #        start_y=y
#    print("WAIT..")
#            #print(maze)
#
#    i = start_x
#    j = start_y
#    for move in moves:
#        if move == "L":
#            i -= 1
#
#        elif move == "R":
#            i += 1
#
#        elif move == "U":
#            j -= 1
#
#        elif move == "D":
#            j += 1
#
#    if maze[j][i] == "X":
#        print("Found: " + moves)
#        printMaze(maze, moves)
#        return True
#
#    return False
#
#
# MAIN ALGORITHM
def strt():
    #for y in range(6):
    # for x in range(8):
    #    if maze[y][x] == "O":
    #        strt_x = x
    #        strt_y=y
    #        print(strt_x,strt_y,"in loop")
    #k=0
    #add = ""
    #while  findEnd(maze, add)!= True:
    #    k+=1
    #    add = nums.get()
    #    # print(add)
    #    for j in ["L", "R", "U", "D"]:
    #        put = add + j
    #        if valid(maze, put):
    #            nums.put(put)
    #   if k > 10000000:
    #       print("Cannot Find")
    #       exit()

    start = (start_x,start_y)
    print(start,"in dfs")
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x,y = path[-1]
        print(x,y)
        if maze[y][x] == 'X':
            print(path)
            length=len(path)
            for i in range(0,length-2):
                    (y_in,x_in)=path.pop(1)
                    set_yellow(x_in,y_in)
            return path
        for x2, y2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= x2 < 8 and 0 <= y2 < 6 and maze[y2][x2] != '#' and (x2,y2) not in seen:
                queue.append(path + [(x2,y2)])
                if maze[y2][x2]!='X':
                    set_purple(y2,x2)
                seen.add((x2,y2))


####################################################################
def clicked_button(x,y):
    print("You clicked",int(x),",",int(y),"in clicked button")
    x=int(x)
    y=int(y)
    #set_grid(x,y)
    #Game_end=False
   #while not Game_end :
    if x in range(-391,-300)  and y in range(320,350):
        clr_screen()
        goto(-101, -340)
        down()
        write("SET THE WALLS", font=('Arial', 18, "normal"))
        up()
        set_grid(x,y)

    elif x in range(-190,-100)  and y in range(320,350):
        #time.sleep(10)
        clr_screen()
        goto(-101, -340)
        down()
        write("SET THE START", font=('Arial', 18, "normal"))
        up()
        onscreenclick(set_start)

    elif x in range(10,100)  and y in range(320,350):
        clr_screen()
        goto(-101, -340)
        down()
        write("SET THE GOAL", font=('Arial', 18, "normal"))
        up()
        onscreenclick(set_goal)

    elif x in range(210,300)  and y in range(320,350):
        print("Start")
        strt()
        clr_screen()
        goto(-150, -340)
        down()
        write("THANK YOU FOR PLAYING", font=('Arial', 17, "normal"))
        up()
        #exit()

    else:
        onscreenclick(clicked_button)
    return 


onscreenclick(clicked_button)


mainloop()
