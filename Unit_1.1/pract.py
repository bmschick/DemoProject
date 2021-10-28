import turtle as trtl

pacman = trtl.Turtle()
pacman.speed(0)

pacman.penup()
pacman.goto(-200,42.5)
pacman.fillcolor('yellow')
pacman.setheading(90+45)
pacman.pendown()
pacman.begin_fill()
pacman.circle(60,180)
pacman.end_fill()

pacman.penup()
pacman.goto(-200,-42.5)
pacman.fillcolor('yellow')
pacman.setheading(45)
pacman.pendown()
pacman.begin_fill()
pacman.circle(60,-180)
pacman.end_fill()

pacman.penup()
pacman.goto(-245,40)
pacman.fillcolor('black')
pacman.pendown()
pacman.begin_fill()
pacman.circle(5)
pacman.end_fill()

step=0
for i in range(17):
  pacman.penup()
  pacman.goto(175-step,4)
  pacman.fillcolor('yellow')
  pacman.pendown()
  pacman.begin_fill()
  pacman.circle(8)
  pacman.end_fill()
  step+=25

pacman.penup()
pacman.goto(270,-10)
pacman.fillcolor('red')
pacman.setheading(90)
pacman.pendown()
pacman.begin_fill()
pacman.circle(30,180)
pacman.end_fill()

for i in range(3):
  pacman.begin_fill()
  pacman.circle(10,180)
  pacman.end_fill()
  pacman.setheading(-90)

pacman.penup()
pacman.goto(245,8)
pacman.fillcolor('white')
pacman.pendown()
pacman.begin_fill()
pacman.circle(3)
pacman.end_fill()

pacman.penup()
pacman.goto(230,8)
pacman.fillcolor('white')
pacman.pendown()
pacman.begin_fill()
pacman.circle(3)
pacman.end_fill()


wn = trtl.Screen()
wn.mainloop()