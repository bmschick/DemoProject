'''Fun With Flowers'''

#1-3 
'''import turtle as trtl

painter = trtl.Turtle()

painter.forward(20)
painter.right(20)
painter.forward(20)
painter.right(20)
painter.forward(20)
painter.right(20)
painter.forward(20)
painter.right(20)
painter.forward(20)
painter.right(20)
painter.forward(20)
painter.right(20)

wn = trtl.Screen()
wn.mainloop()'''

'''Using a While Loop'''
#4 Would loops have made #2 & #3 easier?
#  I think that a loop would have made it a lot easier to type and read

'''Comparing with relational Opperators'''
#5 Prediction: I think that .....
'''
import turtle as trtl

painter = trtl.Turtle()

count = 0
while (count < 3):
  painter.forward(100)
  painter.right(120)
  count = count + 1 # Recall this is incrementing, adding one to  

wn = trtl.Screen()
wn.mainloop()
'''
#6 What happend, was your prediction right? If not explain why...
#  I was correct in my prediction.

#7 Your code part commented below:
'''
count = 0
while (count < 4):
  painter.forward(100)
  painter.right(90)
  count = count + 1
'''
#8 Your code part commented below:
'''
# new starting location so the entire
# octagon is visible
painter.penup()
painter.goto(-50, 150)
painter.pendown()

# Your code here
count = 0
while (count < 8):
  painter.forward(100)
  painter.right(45)
  count = count + 1
'''

'''Drawing with Loops'''
#9 Please respond to the questions in the problem with complete sentences

#10 n/a

#11 Put your final code below, and answers to the questions in the problems

import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(4)#changed

# draw flower
painter.color("darkorchid")
painter.goto(20,180)
petals = 0
while (petals < 12): #changed
  painter.right(30) #changed
  painter.forward(40) #changed
  painter.stamp()
  petals = petals + 1
  
# ring 2 of flower
painter.turtlesize(2) #changed
painter.goto(15,162) #changed
painter.color("blue")
petals = 0
while (petals < 12):
  painter.right(30)
  painter.forward(30)
  painter.stamp()
  petals = petals + 1

# ring 3 of flower (aka number 12)
painter.turtlesize(1) #changed
painter.goto(10,150) #changed
painter.color("red")
petals = 0
while (petals < 18):
  painter.right(20)
  painter.forward(15)
  painter.stamp()
  petals = petals + 1

wn = trtl.Screen()
wn.mainloop()

#answer to questions in complete sentences. I could also say see explination
#in commnets above for the changes

#12 add code to #11, then tell me what lines of code completed the third ring:
# see lines 124 to 136

'''The modulus opperator'''
#13-18 talk about the changes you made to your code & show your teacher 
#      the final results of your flower!

''' A tower of modulus'''
#19-21 Paste final code below (go comment out #11):
'''
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 20
num_buildings = 3
floor = 0
buildings = 0
color_swap = 0

# iterate
while buildings < num_buildings:
  while floor < num_floors:
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    rem = (floor+color_swap) % 6
    if rem < 2:
      painter.color("red")
    elif rem >= 2 and rem < 4:
      painter.color('green')
    else:
      painter.color("black")
    y = y + 5 # location of next floor
    floor = floor + 1
     
    #draw the floor
    painter.pendown()
    painter.forward(50)
  y = -150
  x+=61
  color_swap +=2
  buildings += 1
  floor = 0

wn = trtl.Screen()
wn.mainloop()
'''

'''Decidable or Undecidable?'''
#22

'''Conclusion'''
#1

#2

#3