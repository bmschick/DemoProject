# student names:

'''Conditionals & The if statement'''
# 1. Prediction:


# 2. Did the program work exactly like you thought it would? 

# 3


'''Nested Conditionals''' 
# 4.

# 5. 

# 6.

# 7.
 
'''The elif Statement'''
# 8 & 9.


# 10 & 11.



'''College Board'''

'''Nested for loop Iteration'''
# 12-14. 
# Prediction:



# Did the program work exactly like you thought it would? 

 

'''Nested Loops and Conditionals'''

# 15 through 17. Program & Test your code for a couple examples in the terminal then summerize your results: 

'''Turtles Stop!'''
# 18 through 20 use the code below (made changes from the original so it would fit in replt.

# # a118_turtles_in_traffic.py
# # Move turtles horizontally and vertically across screen.
# # Stopping turtles when they collide.
# import turtle as trtl

# # create two empty lists of turtles, adding to them later
# horiz_turtles = []
# vert_turtles = []

# # use interesting shapes and colors
# turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
# horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
# vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

# tloc = -95
# for s in turtle_shapes:

#   ht = trtl.Turtle(shape=s)
#   ht.turtlesize(.5)
#   #ht.speed(2)
#   horiz_turtles.append(ht)
#   ht.penup()
#   new_color = horiz_colors.pop()
#   ht.fillcolor(new_color)
#   ht.goto(-115, tloc)
#   ht.setheading(0)

#   vt = trtl.Turtle(shape=s)
#   vt.turtlesize(.5)
#   #vt.speed(2)
#   vert_turtles.append(vt)
#   vt.penup()
#   new_color = vert_colors.pop()
#   vt.fillcolor(new_color)
#   vt.goto( -tloc, 115)
#   vt.setheading(270)
  
#   tloc += 35
# #ToDo Answer below:
# steps = 0
# pixel_size = 20
# distance = 3
# while steps < 30:
#   steps = steps + 1
#   for ht in horiz_turtles:
#     for vt in vert_turtles:
#       ht.forward(distance)
#       vt.forward(distance)
#       # collision occurs if too close
#       if (abs(ht.xcor() - vt.xcor()) < pixel_size):
#         if (abs(ht.ycor() - vt.ycor()) < pixel_size):
#           # change color and remove from list so it no longer will move
#           ht.fillcolor("gray")
#           horiz_turtles.remove(ht)
#           vt.fillcolor("gray")
#           vert_turtles.remove(vt)

# wn = trtl.Screen()
# wn.mainloop()

'''It’s Your Turn'''
# 21 through 22 copy and paste the completed code from the above section and make all the modifications you can.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = -95
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  ht.turtlesize(.5)
  #ht.speed(2)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-115, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vt.turtlesize(.5)
  #vt.speed(2)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 115)
  vt.setheading(270)
  
  tloc += 35
# move turtles on screen, stopping if a collision occurs
steps = 0
pixel_size = 28
distance = 2
while steps < 10:
  steps = steps + 1

  #speed up and then slow down
  distance = 2
  distance = distance + 2
  if (distance > 10):
    distance = 1

  for ht in horiz_turtles:
    for vt in vert_turtles:
      # move 
      ht.forward(distance)
      vt.forward(distance)
      # collision occurs if too close
      if (abs(ht.xcor() - vt.xcor()) < pixel_size):
        if (abs(ht.ycor() - vt.ycor()) < pixel_size):
          # remember color and shape of turtles
          orig_ht_color = ht.fillcolor()
          orig_ht_shape = ht.shape()
          orig_vt_color = vt.fillcolor()
          orig_vt_shape = vt.shape()
          # change color and shape to indicate collision
          # then back up a bit and recover
          vt.fillcolor("gray")
          vt.shape("circle")
          vt.back(2)
          ht.fillcolor("gray")
          ht.shape("circle")
          ht.back(6)

          # restore orig shape and color
          ht.shape(orig_ht_shape)
          ht.fillcolor(orig_ht_color)
          vt.shape(orig_vt_shape)
          vt.fillcolor(orig_vt_color)

for ht in horiz_turtles:
  ht.fillcolor("gray")
for vt in vert_turtles:
  vt.fillcolor("gray")

wn = trtl.Screen()
wn.mainloop()


# Explain the changes you made:


# Explain the changes you attempted but could not get to work (if any)


# Quiz:


# Skip AP review section
 
'''Conclusion'''
# 1.
 
 
