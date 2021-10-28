# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
tcolor = "blue"
tsize = 2
tshape = "turtle"
score = 0
font_setup = ("Arial", 12, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
game_turtle = trtl.Turtle(tshape)
game_turtle.shapesize(tsize)
game_turtle.fillcolor(tcolor)
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-150, 125)
counter =  trtl.Turtle()
counter.penup()
counter.goto(100, 125)
#-----game functions--------
def spot_click(x,y):
  global timer
  if timer != 0:
    update_score()
    game_turtle.penup()
    game_turtle.hideturtle()
    change_position()
    game_turtle.showturtle()  
    game_turtle.pendown()
  else:
    game_turtle.hideturtle()
  
  

def change_position():
  new_xpos = rand.randint(-100,100)
  new_ypos = rand.randint(-100,100)
  game_turtle.goto(new_xpos, new_ypos)

def update_score():
  global score
  score +=1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------

#game_turtle.onclick(spot_click)

wn = trtl.Screen()
wn.setup (width=450, height=350)
wn.onscreenclick(spot_click)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()