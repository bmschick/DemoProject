# 1-5 Explore the code
'''
#1-2 Students read code and predict output
print("Hello there!") 
# 3 Read and predict assignment and variables use
user_name = "student"
print("Hello", user_name, "welcome to my program.")
# 4 Students modify input question and answer.
user_name = input("What is your name?")
print("Hello", user_name, "welcome to my program.")
'''

# 7-11 Explore commented code
'''
# import the datetime module to get the current date/year
import datetime as dt

# ask user for their name then welcome them
user_name = input("What is your name?")
print("Hello", user_name, "welcome to my program.")

# ask user for their age
age = input("How old are you?") # 7: broken
#age = int(input("How old are you?")) # 10: fixed

# get the current year using the datetime object that resides in the datetime module
curr_year = dt.datetime.now().year

# prepare and display output
birth_year = curr_year - age
print("Hmmm... were you born in", birth_year, ".")
'''

# 12 Starter Code
# Talk about reference docs and 
# the python turtle library
# https://docs.python.org/3/library/turtle.html
# ask about how to find a list of color strings that work
# https://tcl.tk/man/tcl8.6/TkCmd/colors.htm
'''
# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)


# ask user for the radius of a circle


# draw a circle with the radius and line color entered by the user


# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
'''

# 12 Finished Code
'''
############################################################################
#   a112_TR_circle.py
#   Example solution code for drawing a circle 
#   based on user input for color and radius.
############################################################################
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()


############################################################################
#moved screen set-up and resized so it did not cover my VSC
wn = trtl.Screen()
wn.setup(width=200, height=200, startx=0, starty=0)
############################################################################


# ask user for a color (such as red, green, blue, pink, purple)
color = input("Enter a color (such as red, green, blue, pink, purple):")

# ask user for the radius of a circle
radius = int(input("Enter a radius for the circle:"))

# draw a circle with the radius and line color entered by the user
painter.pencolor(color)
painter.circle(radius)

#make the screen persist

wn.mainloop()
'''

# 14 circle() examples
# talk about turtle screen coords
'''
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.pensize(5)

# move turtle without marking a line
painter.penup()
painter.goto(0, -20)
painter.pendown()

# draw a semi-circle
painter.circle(100, 180)

# move turtle without marking a line
painter.penup()
painter.goto(0, 20)
painter.pendown()

# draw a 3-step semi-circle
painter.circle(100, 180, 3)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
'''

# 16 Starter code
'''
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle


# move the turtle to another part of the screen


# add code here for an arc


# move the turtle to another part of the screen


# add code here for an arc that is greater than 90 degrees and has 5 steps


# move the turtle to another part of the screen


# add code here to create a polygon of your choice using the circle method

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
'''

# 16 Example Key
'''
############################################################################
#   a112_TR_arcs_and_polygons.py
#   Example solution code for drawing the arcs and polygons with circle()
############################################################################
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.pensize(5)
# add code here for a circle
painter.circle(20)

# move the turtle to another part of the screen
painter.penup()
painter.goto(50, 50)
painter.pendown()

# add code here for an arc
painter.circle(20, 90)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-50, 50)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(30, 180, 5)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-50, -50)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(30, 360, 8)

# get screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
'''

# 18 Starter code
'''
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle


# move the turtle to another part of the screen


# change both the pen and fill colors
# then draw a polygon of your choice


# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
'''

# 18 Example code

############################################################################
#   a112 pen and fill colors
#   Example solution code for drawing with pen and fill colors
############################################################################
# import turtle module
import turtle as trtl

# create turtle object
drawer = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
drawer.pencolor("magenta")
drawer.fillcolor("turquoise")
drawer.pensize(5)
drawer.begin_fill()
drawer.circle(40)
drawer.end_fill()

# move the turtle to another part of the screen
drawer.penup()
drawer.goto(75, 75)
drawer.pendown()

# change both the pen and fill colors
# then draw a polygon of your choice
drawer.pencolor("cyan")
drawer.fillcolor("violet")
drawer.begin_fill()
drawer.circle(35, 360, 6)
drawer.end_fill()

# get screen object and make it persist
wn = trtl.Screen()
wn.mainloop()

