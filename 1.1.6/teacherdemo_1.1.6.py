# student names:

'''Buggy Image'''

'''Understand Your Code'''

#1 Trace table
# Statement   spider   Y
# spider=8             
# leg_length=40/spider          
# spider=10            

#2, print leg_length

#3, write a trace table

#4, print leg_length

#5, #6, #7 
#5 be sure to copy this code

# #   a116_buggy_image.py
# import turtle as trtl
# # instead of a descriptive name of the turtle such as painter,
# # a less useful variable name x is used
# x = trtl.Turtle()
# x.pensize(40)
# x.circle(20)
# w = 6
# y = 70
# z = 380 / w
# x.pensize(5)
# n = 0
# while (n < w):
#   x.goto(0,0)
#   x.setheading(z*n)
#   x.forward(y)
#   n = n + 1
# x.hideturtle()
# wn = trtl.Screen()
# wn.mainloop()

'''Investigate with Block Strings'''
# answer:

#8, #9, #10, #11 Modify and Test
#8, #9
# x should be:
#10, can use repl.it's rename symbol instead 
# to change all x's (select, <F2>, type new name)
# but beware, changes all selected var, even if in comments
#     and cannot be <ctrl>+Z undone
#11, test new code.

'''Improve Your Code'''
'''Variable Names'''
#12, #13, #14 Investigate w
#13 rename all w's: 
#14, test new code

#15, #16 Investigate and rename y and test

#17, #18 Investigate and rename z and test
#17 Investigate z with print statements

#19, #20 Investigate n with a trace table

# #19 Trace table for n:
# num_legs == 6
# leg_angle == 63.33
# Loop         n   n<num_legs   n*leg_angle   n=n+1
# 0            0   T            0.0           1
# 1            1   T            63.3          2
# 2            2   T            126.7         3
# 3            3   T            190.0         4
# 4            4   T            253.3         5
# 5            5   T            316.7         6
# 6            6   F

#20 Rename and test

#for these tests, it's a good idea to put a "DBG: " in the print
# and them comment them away later.

# #   a116_buggy_image.py
# import turtle as trtl
# # instead of a descriptive name of the turtle such as painter,
# # a less useful variable name spider is used
# spider = trtl.Turtle()
# spider.pensize(40)
# spider.circle(20)
# num_legs = 6
# leg_length = 70
# leg_angle = 380 / num_legs
# spider.pensize(5)
# leg_counter = 0
# while (leg_counter < num_legs):
#   spider.goto(0,0)
#   # print("DBG: z: ",leg_angle,", z*n: ",leg_angle*leg_counter)
#   spider.setheading(leg_angle*leg_counter)
#   spider.forward(leg_length)
#   leg_counter = leg_counter + 1
# spider.hideturtle()
# wn = trtl.Screen()
# wn.mainloop()

'''PLTW COMPUTER SCIENCE NOTEBOOK'''

#21 Save version to Git
'''Readability'''
#22, #23 Add comments and whitespace, test
#24 Use Git to save new version
# Be sure to add short description

# #   a116_buggy_image.py
# import turtle as trtl

# spider = trtl.Turtle()

# # create the spider body
# spider.pensize(40)
# spider.circle(20)

# # configure the spider legs
# num_legs = 6
# leg_length = 70
# leg_angle = 380 / num_legs
# spider.pensize(5)

# # draw legs
# leg_counter = 0
# while (leg_counter < num_legs):
#   spider.goto(0,0)
#   # print("DBG: z: ",leg_angle,", z*n: ",leg_angle*leg_counter)
#   spider.setheading(leg_angle*leg_counter)
#   spider.forward(leg_length)
#   leg_counter = leg_counter + 1

# spider.hideturtle()
# wn = trtl.Screen()
# wn.mainloop()

'''Variable Values'''
#25, #26, #27 - Make changes to the legs
# placement, number, angle
#28 Save Version to Git

#   a116_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()

# create the spider body
spider.pensize(40)
spider.circle(20)

# configure the spider legs
num_legs = 8
leg_length = 70
leg_angle = 360 / num_legs
spider.pensize(5)

# draw legs
leg_counter = 0
while (leg_counter < num_legs):
  spider.goto(0,20)
  # print("DBG: z: ",leg_angle,", z*n: ",leg_angle*leg_counter)
  spider.setheading(leg_angle*leg_counter)
  spider.forward(leg_length)
  leg_counter = leg_counter + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()