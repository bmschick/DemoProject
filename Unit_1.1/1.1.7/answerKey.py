# student names:

### Note for the assignment, and all future assignments. When you give a predition, I want to know if you were actually correct, if not what did you learn from your original understanding. ###

'''Lists & List Method'''
# 0 What is the difference between a list and array?

# 1 Prediction:


# 2 
new_list = ["dog", "cat", "mouse", "bird", "monkey"]
print(new_list)

'''College Board
Tip: When answering college board topics, try to ask yourself How is it similar/different to python?

'''

# 3 
new_list = ["dog", "cat", "mouse", "bird", "monkey"]
new_list.append("lion") 
print("list now is", new_list)

'''College Board'''

# 4
#   a117_pop_list.py
new_list = ["dog", "cat", "mouse", "bird", "monkey"]
item = new_list.pop()
print("popped ", item)
print("list now is", new_list)

# What is the difference between pop and append?

'''The for Loop'''
# 5 Prediction:
#   a117_forloop.py
new_list = ["dog", "cat", "mouse", "bird", "monkey"]
for animal in new_list: 
  print("next animal:")
  print(animal)
  

# 6 Did the Prediction Match PERFECTLY (all spaces, brackets, commas, syntax etc.)? 

#  a.
#  b.
#  c.
 


'''College Board'''

# 7 & 8 Add comments to above code
 



'''Looping with Lists of Turtles'''

# # 9 - 11
# import turtle as trtl
# # create an empty list of turtles
# my_turtles = []
# # use interesting shapes and colors
# turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
# turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
# for s in turtle_shapes:
#   t = trtl.Turtle(shape=s)
#   my_turtles.append(t)
# #  
# startx = 0
# starty = 0
# #
# for t in my_turtles:
#   t.goto(startx, starty)
#   t.right(45)     
#   t.forward(50)
# #	
#   startx = startx + 50
#   starty = starty + 50
# wn = trtl.Screen()
# wn.mainloop()
 
'''It’s Your Turn'''
# 12 - 18 Copy and paste the final code from #11 and complete 12-18. Make sure to comment your code!
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic",
"arrow", "turtle", "circle", "square", "triangle", "classic",
"arrow", "turtle", "circle", "square", "triangle", "classic"
]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold",
"red", "blue", "green", "orange", "purple", "gold",
"red", "blue", "green", "orange", "purple", "gold",
]

# initialize myturtles list, turtles with different shapes and colors
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color) 
  t.pencolor(new_color)
  t.penup()

# draw all turtles in a spiral shape, spiral grows on every iteration
start_x = 0
start_y = 0
direction = 0
grow = 30
for t in my_turtles:
  t.goto(start_x, start_y)
  t.setheading(direction)
  t.pendown()
  t.right(45)     
  t.forward(grow)
  direction = t.heading()
  start_x = t.xcor() 
  start_y = t.ycor()
  grow = grow + 10

wn = trtl.Screen()
wn.mainloop()


# Quiz Results:

 
'''Conclusion'''
# 1

# 2
 
 


 
