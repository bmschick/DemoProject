# 1 and 2 starter code
'''
#   a114_make_it_start.py
#   Make the code draw 5 circles.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.goto(-150,5)
painter.shape("square")
painter.color("salmon")

line = 5 # This is the line you need to change.

while (line < 5): 
  painter.pendown()
  painter.circle(5)
  painter.penup()
  painter.forward(20)
  line = line + 1

wn = trtl.Screen()
wn.mainloop()
'''

#3, 4 skipped & runaway loop examples
'''
#   a114_infinite_loop_1.py
#   This code will run...forever!
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")

line = 6

while (line > 5): # What does this do?
  painter.goto(0,0)
  painter.right(20)
  painter.forward(80)
  painter.pendown()
  painter.circle(10)
  painter.penup()
  line = line + 1 # What does this do?
  if (line % 18 == 0):
    painter.color("navy")
  if (line % 36 == 0):
    painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()
'''

'''
#   a114_infinite_loop_2.py
#   This code will also run forever!
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")

line = 4 # Starting value for line

while (line < 5): # What does this do?
  painter.goto(0,0)
  painter.right(20)
  painter.forward(80)
  painter.pendown()
  painter.circle(10)
  painter.penup()
  line = line - 1 # What does this do?
  if (line % 18 == 0):
    painter.color("navy")
  if (line % 36 == 0):
    painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()
'''

#5 PEMDAS examples
'''
#   a114_order_of_operations_1.py
#   This program uses some arithmetic to move the turtle and draw.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.shape("square")
painter.color("turquoise")

painter.stamp()
#painter.forward(((4-5)+7*(2-(18/4))*2)) # one way
#painter.forward((4-(5+7)*((2-18)/4))*2) # another way

painter.stamp()

wn = trtl.Screen()
wn.mainloop()
'''

#6 user function that
# Ask the user to enter two numbers.
# Determine if the first number is evenly divisible by the second number. Recall that !=  compares for inequality.
# Repeat steps a and b  until the numbers are evenly divisible.

# starter code
'''
#   a114_divisible.py

# get two numbers from user

# loop whle the numbers are not divisible (the remainder is 0)

  # inform user of result 
  
  # gather user input again
  
# inform user of result 
'''

#7, #8, #9 
# Look at code and predict what it does
# run code to see if predicted correctly
# modify the code to change colors periodically and make spiral tighter
'''
#   a114_guess.py
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
painter.pensize(2)

spiral_space = 0

while (spiral_space < 80): 
  painter.goto(0,0)
  painter.right(20)       #9 play with 20, bigger turns
  painter.forward(50+(spiral_space*3)) #9 playwth step and incremet
  painter.pendown()
  painter.circle(10)
  painter.penup()
  spiral_space = spiral_space + 1
  if (spiral_space % 18 == 0):    #9 5
    painter.color("navy")
  if (spiral_space % 36 == 0):    #9 10
    painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()
#'''
# draws a salmon and blue spiral
# by increasing forward distance each time

#10, #11
# look at code and predict behavior
# run code and confirm prediction
'''
#   a114_nested_loops_1.py
j = 0
while (j < 10):
  print ("j: ", j)
  j = j + 1

  i = 0
  while (i < 5):
    print ("  i: ", i)
    i = i + 1
'''

#12 predict and run
#13 add inner loop, predict, run
'''
#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (x < 200): 
  x = x + 50
  y = 200
  painter.goto(x,y)
  painter.color("red")
  painter.stamp()
  #while( y > 0):     #13 added
  #  y=y-50
  #  painter.goto(x,y)
  #  painter.color("blue")
  #  painter.stamp()


wn = trtl.Screen()
wn.mainloop()
'''

#14 Create a stamper program to make the depicted dot matrix

#15, #16, #17, #18, #19
# predict
# Run
# and modify to draw two peaks
# and modify to draw reflection
# and draw forever
# '''
#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.speed(10)
painter.penup()
painter.goto(-200, 0)
painter.pendown()

while(True):         #19 and tab
  x = -200
  y = 0
  painter.penup()     #19
  painter.goto(x,y)
  painter.pendown()
  move_x = 1
  move_y = 1
# while (x < 0):
  while (x < 200):      #17

    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1
  
    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1

  x = -200              #18
  y = 0
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  move_x = 1
  move_y = -1
  while (x < 200):      

    while (y > -100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1
  
    while (y < 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1

wn = trtl.Screen()
wn.mainloop()
#'''

#20, #21, #22
# Flowcharts
#21 which algorithm is this?
#22 draw a flowchart for a loop algorithm