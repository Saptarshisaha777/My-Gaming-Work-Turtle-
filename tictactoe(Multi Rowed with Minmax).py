import turtle
import collections
import queue
import time
import math
from turtle import *

bgcolor("white")
pencolor("black")
title("TIC TAC TOE")
setup(850, 850)
up()
pensize()

# nums = queue.Queue()
# nums.put("")


# pen = turtle.Turtle()
# pen.speed(0)
# pen.hideturtle()
# goto(-400,0)
# pen.down()
# pen.forward(800)
# pen.up()
# goto(0,0)
hideturtle()
speed(20)
up()
next_turn = 0
INFINITY = 10000


####################### SET GUI ##################################


##############################################################################


# BUTTON
def set_X(row, column):
    mycross = turtle.Turtle()
    mycross.hideturtle()
    mycross.speed(20)
    mycross.up()
    mycross.goto((column * width) - 300, -(row * width) + 300)
    mycross.setheading(-45)
    mycross.down()
    mycross.forward(width * math.sqrt(2))
    mycross.up()
    mycross.goto((column * width) - 300, -(row * width) + 300 - width)
    mycross.setheading(45)
    mycross.down()
    mycross.forward(width * math.sqrt(2))
    mycross.up()
    return


def set_O(row, column):
    mycircle = turtle.Turtle()
    mycircle.hideturtle()
    mycircle.speed(20)
    mycircle.up()
    mycircle.setposition(((column * width) - 300) + (width / 2), (-(row * width) + 300) - (width))
    # setheading(-45)
    # forward(int(width*math.sqrt(2)//2))
    mycircle.down()
    mycircle.circle(width / 2)
    mycircle.up()


def clr_screen():
    goto(-175, -310)
    down()
    fillcolor('blue')
    begin_fill()
    for i in range(2):
        forward(30)
        left(90)
        forward(350)
        left(90)
    end_fill()
    up()
    return


def create_ttt(width):
    # Horizontal BArs
    y = 300
    while y >= -300:
        goto(-300, y)
        down()
        forward(600)
        up()
        y = y - width

    # VERTICAL BARS

    x = 300

    while x >= -300:
        goto(x, 300)
        setheading(-90)
        down()
        forward(600)
        up()
        x = x - width


goto(0, 0)

goto(-400, 375)
down()
write("DOUBLE CLICK ON BUTTONS TO ACCESS", font=('Comic Sans', 18, "normal"))
up()


###########################################################################################

###################    SET INPUT    ###########################
def create_grid(grid_size):
    grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
    return grid


def Outcome():
    print(check_board(board),"in Outcome")
    if check_board(board) > 0:

        print("PLAYER 1 WON")

        clr_screen()
        goto(-101, -340)
        down()
        write("PLAYER 1 WINS!!!", font=('Arial', 18, "normal"))
        up()

        print(board)
        return True

    elif check_board(board) < 0:
        print("PLAYER 2 WON")

        clr_screen()
        goto(-101, -340)
        down()
        write("PLAYER 2 C WINS!!!", font=('Arial', 18, "normal"))
        up()

        print(board)
        return True

    elif next_turn == grid_size * grid_size +1:
        print("   TIE   ")

        clr_screen()
        goto(-101, -340)
        down()
        write("          TIE!!!    ", font=('Arial', 18, "normal"))
        up()

        print(board)
        return True

    return False


# def set_grid(x, y):
#    print("You clicked", int(x), ",", int(y), "in set grid")
#
#    onscreenclick(clicked_grid)
#    return
#
#
# def set_start(x, y):
#
#    if x in range(-400, 400) and y in range(-300, 300):
#
#        row = int((300 - y) // 100)
#        column = int((x + 400) // 100)
#        # print("You clicked",row,",",column)
#        grid[row][column] = 'O'
#        start_y = row
#        start_x = column
#
#        prev_y = row
#        prev_x = column
#
#        print(start_x, start_y, "in set start")
#        print(grid)
#
#        set_blue(row, column)
#
#    else:
#        onscreenclick(clicked_button)
#
#
# def set_goal(x, y):
#    if x in range(-400, 400) and y in range(-300, 300):
#        row = int((300 - y) // 100)
#        column = int((x + 400) // 100)
#        # print("You clicked",row,",",column)
#        grid[row][column] = 'X'
#        print(grid)
#
#        set_green(row, column)
#
#
#
#
#    else:
#        onscreenclick(clicked_button)
#

# SET GRID OBSTACLES
def clicked_grid(x, y):
    global next_turn
    if next_turn == 0:
        next_turn = next_turn + 1
    print(next_turn)
    print("You clicked", int(x), ",", int(y), "in clicked grid")

    if x in range(-300, 300) and y in range(-300, 300):
        row = int((300 - y) // width)
        column = int((x + 300) // width)
        # print("You clicked",row,",",column)

        if board[row][column] == 0:
            if (next_turn) % 2:
                board[row][column] = 'X'
                print(board)

                clr_screen()
                goto(-101, -340)
                down()
                write("PLAYER 2's TURN", font=('Arial', 18, "normal"))
                up()

                set_X(row, column)
                next_turn = next_turn + 1

            if next_turn == grid_size * grid_size:
                print("GA/mE END")

            Outcome()
            maze = board

    else:
        print("WRONG TILE")
        next_turn = next_turn - 1

    cell = best_move()
    print(cell ,"in clicked grid")
    if cell != (0, 0) and  next_turn != grid_size*grid_size:
        board[cell[0]][cell[1]] = 'O'
        set_O(cell[0], cell[1])
    print(board)

    if not Outcome() and next_turn != grid_size * grid_size :
        clr_screen()
        goto(-101, -340)
        down()
        write("PLAYER 1's TURN", font=('Arial', 18, "normal"))
        up()


    next_turn = next_turn + 1
    if next_turn == grid_size * grid_size + 1:
        print("GA/mE END")


    onscreenclick(clicked_grid)


####################################################################
# maze = grid

print()


def check_board(board):
    # HORIZONTAL
    for i in range(grid_size):
        for j in range(grid_size - 1):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                if j + 2 == grid_size:
                    if board[i][j] == 'X':
                        return 10
                    else:
                        return -10
                continue
            else:
                break

    # VERTICAL
    for i in range(grid_size):
        for j in range(grid_size - 1):
            if board[j][i] == board[j + 1][i] and board[j][i] != 0:
                if j + 2 == grid_size:
                    if board[j][i] == 'X':
                        return 10
                    else:
                        return -10
                continue
            else:
                break
        # if j+2==grid_size:
        #    return True

    # DIAGONAL U TO D
    for i in range(grid_size - 1):
        if board[i][i] == board[i + 1][i + 1] and board[i][i] != 0:
            if i + 2 == grid_size:
                if board[i][i] == 'X':
                    return 10
                else:
                    return -10
            continue
        else:
            break

    # DIAGONAL D TO U
    for i in range(grid_size - 1):

        if board[i][(grid_size - 1) - i] == board[i + 1][(grid_size - 1) - (i + 1)] and board[i][
            (grid_size - 1) - i] != 0:

            if i + 2 == grid_size:
                if board[i][(grid_size - 1) - i] == 'X':
                    return 10
                else:
                    return -10
            continue
        else:
            break

    return 0


def empty_cells(maze):
    cells = []
    for i in range(grid_size):
        for j in range(grid_size):
            if maze[i][j] == 0:
                cells.append([i, j])
    return cells


def valid(x, y, maze):
    if [x, y] in empty_cells(maze):
        return True
    else:
        return False


# MAIN ALGORITHM
score = 0
def minimax(maze, depth, player):
    global score
    if depth==0:
        score=0
    #print(check_board(maze))
    score = score + check_board(maze) - depth
    print(score , " in minimax")
    if score >= 1:
        return (score)
    if score <= -1:
        return (score)
    if len(empty_cells(maze)) == 0:
        return 0

    if player:
        bestval = -INFINITY
        for cell in empty_cells(maze):
            x, y = cell[0], cell[1]
            maze[x][y] = 'O'
            val = minimax(maze, depth + 1, False)
            bestval = max(bestval, val)
            print(bestval,x,y,player)
            maze[x][y] = 0
        return bestval
    else:
        bestval = +INFINITY
        for cell in empty_cells(maze):
            x, y = cell[0], cell[1]
            maze[x][y] = 'X'
            val = minimax(maze, depth + 1, True)
            bestval = min(bestval, val)
            print(bestval, x, y,player)
            maze[x][y] = 0
        return bestval


def best_move():
    maze = board
    best_val = -INFINITY
    x, y = 0, 0
    for cell in empty_cells(maze):
        row, column = cell[0], cell[1]
        print(cell[0], cell[1], "in best move")
        maze[row][column] = 'X'
        move_val = minimax(maze, 0, False)
        maze[row][column] = 0

        if (move_val > best_val):
            x, y = row, column
            best_val = move_val
    return (x, y)


####################################################################
def clicked_button(x, y):
    print("You clicked", int(x), ",", int(y), "in clicked button")
    x = int(x)
    y = int(y)
    # set_grid(x,y)
    # Game_end=False
    # while not Game_end :
    if x in range(-391, -300) and y in range(320, 350):
        pass


    else:
        onscreenclick(clicked_button)
    return


####################################################################

grid_size = int(input("Enter the grid size 2~10:"))
width = 600 / (grid_size)
print(width)
create_ttt(width)
board = create_grid(grid_size)
print(board)

clr_screen()
goto(-101, -340)
down()
write("PLAYER 1's TURN", font=('Arial', 18, "normal"))
up()

onscreenclick(clicked_grid)

mainloop()