# Maze 1 ########################
'''
import turtle as trtl

#------ robot algorithms
def move():
  robot.dot(10)
  robot.forward(50)

def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.right(90)
  robot.speed(2)
  
#----- roboto starting location
startx = -100
starty = -100

#----- init screen
wn = trtl.Screen()
wn.setup(width=400, height=420)

#----- init robot
robot_image = "1.1.5/robot.gif"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO 1: change maze here
wn.bgpic("1.1.5/maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO 2: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
i = 0
while (i < 4): # forward 4
  i += 1
  move()

j = 0
turn_right()
while (j < 4): # forward 4
  j += 1
  move()


#---- end robot movement 

wn.mainloop()
'''

# Maze 2 ####################################
'''
import turtle as trtl
#------ robot algorithms ----------
def move():
  robot.dot(10)
  robot.forward(50)
def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)
def turn_right():
  robot.speed(0)
  robot.right(90)
  robot.speed(2) 
#----- roboto starting location ------
startx = -100
starty = -100
#----- init screen -----------------
wn = trtl.Screen()
wn.setup(width=400, height=420)
#----- init robot ------------------
robot_image = "1.1.5/robot.gif"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()
#---- TODO 1: change maze here -------
wn.bgpic("1.1.5/maze2.png") # other file names should be maze2.png, maze3.png
#---- TODO 2: begin robot movement here ---------
i = 0
while (i < 3): # forward 4
  i += 1
  move()
  if i == 3:
    j = 0
    turn_right()
    while (j < 2): # forward 4
      j += 1
      move()
#################################################
# Route 2: Did not have to add a new variable, could have done with for and range or no nesting at all
################################################
robot.goto(startx,starty)
i = 0
while (i < 3): # forward 4
  i += 1
  move()
  if i == 3:
    turn_left()
    while (i < 6): # forward 4
      i += 1
      move()
    if i == 6:
      turn_left()
      while (i < 7): # forward 4
        i += 1
        move()
#---- end robot movement 
wn.mainloop()
'''
# Maze 3 ##################################
import turtle as trtl
#------ robot algorithms ----------------
def move():
  robot.dot(10)
  robot.forward(50)
def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)
def turn_right():
  robot.speed(0)
  robot.right(90)
  robot.speed(2) 
#----- roboto starting location ---------------
startx = -100
starty = -100
#----- init screen ------------------------
wn = trtl.Screen()
wn.setup(width=400, height=420)
#----- init robot --------------------
robot_image = "1.1.5/robot.gif"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()
#---- TODO 1: change maze here ------
wn.bgpic("1.1.5/maze3.png") # other file names should be maze2.png, maze3.png
#---- TODO 2: begin robot movement here --------
i = 0
while (i < 2): # forward 4
    i += 1
    j = 0
    while j < 1:
      move()
      j+= 1
    turn_right()
    while j < 2:
      move()
      j+= 1
    turn_left()
    while j < 3:
      move()
      j+= 1
    turn_right()
    while j < 4:
      move()
      j+= 1
    turn_left()
    robot.pencolor("blue")
#---- end robot movement 

wn.mainloop()

