#7 Starter code:
'''
import turtle as trtl

painter = trtl.Turtle()
painter.turtlesize(3) # number 8
painter.pensize(5) # number 9
painter.forward(100)
painter.right(90)
 
wn = trtl.Screen()
wn.mainloop()
'''

# Note:
# too convert multiple
# line into 
# single line comments on a mac is
# command + / (PC chould be ctrl + /)
# try that out now


#12 Pasted Starter code:
'''import turtle as trtl

painter = trtl.Turtle()
painter.speed(3)
painter.turtlesize(3) # number 8
painter.pensize(5) # number 9
painter.forward(100)
painter.right(90)
painter.forward(100) # number 13 all lines below
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)



wn = trtl.Screen()
wn.mainloop()
'''

# numbers 15 to 18
import turtle as trtl

painter = trtl.Turtle()
painter.speed(3)
painter.turtlesize(3)
painter.pensize(5)

painter.penup()
painter.goto(100,100)
painter.pendown()
painter.setheading(45)
painter.circle(25,360,4)
painter.goto(125,100)

painter.circle(25,360,4)

painter.penup()
painter.goto(-100,100)
painter.pendown()
painter.setheading(45)
painter.circle(25,360,3)

wn = trtl.Screen()
wn.mainloop()