# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
# screen
global wn

def configure_screen():
  global wn
  wn = trtl.Screen() 
  screen_width = 400
  screen_height = 300
  wn.setup(width=screen_width,height=screen_height) # window size
  wn.screensize(screen_width,screen_height)        # canvas size
  wn.colormode(255)
  pass

# spot
global spot_color
global spot_shape
global spot_size
global spot_maxSize
global spot_margin

def configure_spot():
  global spot_color
  global spot_shape
  global spot_size
  global spot_maxSize
  global spot_margin
  spot_color = "brown"
  spot_shape = "circle"
  spot_size = 2
  spot_maxSize = 5
  spot_margin = 20
  pass

# score
global score
global scoreWriterX
global scoreWriterY
global score_margin

def configure_score():
  global score
  global scoreWriterX
  global scoreWriterY
  global score_margin
  score = 0
  score_margin = 30
  width, height = wn.screensize() 
  scoreWriterX = -width/2 + score_margin
  scoreWriterY = height/2 - score_margin
  pass

# writers
global font_setup

def configure_writers():
  global font_setup
  font_setup = ("Arial", 20, "normal")
  pass

# countdown timer 
global timer 
global timerInterval
global timerUp
global countWriterX
global countWriterY

def configure_timer():
  global timer 
  global timerInterval
  global timerUp
  global countWriterX
  global countWriterY
  global score_margin
  timer = 5
  timerInterval = 1000
  timerUp = False
  width, height = wn.screensize()
  count_margin = 75
  countWriterX = width/2 - count_margin
  countWriterY = height/2 - score_margin
  pass

#-----initialize turtles-----
# spot
global spot

def initialize_spot():
  global spot
  global spot_shape
  global spot_color
  global spot_size
  spot = trtl.Turtle() 
  spot.shape(spot_shape)
  spot.fillcolor(spot_color)
  spot.shapesize(spot_size)
  spot.penup()
  pass

# score_writer
global score_writer

def initialize_score():
  global score_writer
  global scoreWriterX
  global scoreWriterY
  score_writer = trtl.Turtle() 
  score_writer.penup()
  score_writer.goto(scoreWriterX,scoreWriterY)
  score_writer.hideturtle()
  pass

# countdown_writer
global count_writer

def initialize_timer():
  global count_writer
  global countWriterX
  global countWriterY
  global timer
  count_writer = trtl.Turtle() 
  count_writer.penup()
  count_writer.hideturtle()
  count_writer.goto(countWriterX, countWriterY)
  count_writer.clear()
  count_writer.write("Time " + str(timer),font_setup)
  pass

#-----game functions--------

def start_game():
  ''' start-game()
      initializes the screen
      initializes the game 
      instantiates the turtles
      '''
  configure_screen()
  configure_spot()
  configure_writers()
  configure_score()
  configure_timer()
  initialize_spot()
  initialize_score()
  initialize_timer()
  pass

def spot_clicked(x,y):
  global spot
  global timerUp
  # print("clicked ",x,y)
  if( not timerUp ):
    update_score()
    stamp_turtle()
    change_size()
    change_position()
  else:
    spot.hideturtle()
  pass

def change_size():
  global spot
  global spot_size
  global spot_maxSize
  spot_size = rand.random()*spot_maxSize
  spot.turtlesize(spot_size)
  pass

def stamp_turtle():
  ''' picks a random color 
      and stamps it'''
  global spot
  oldColor = spot.fillcolor()
  # print(oldColor)
  newColor = rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)
  spot.color(newColor)
  spot.stamp()
  spot.color(oldColor)
  pass

def change_position():
  global wn
  global spot
  global spot_margin
  width, height = wn.screensize()
  newX = -width/2 + rand.randint(spot_margin,width-spot_margin)
  newY = -height/2 + rand.randint(spot_margin,height-spot_margin)
  spot.hideturtle()
  spot.goto(newX,newY)
  spot.showturtle()
  pass

def update_score():
  global score
  global score_writer
  global font_setup
  global scoreWriterX
  global scoreWriterY
  score += 1
  # print("Score",score)
  score_writer.goto(scoreWriterX, scoreWriterY)
  score_writer.clear()
  score_writer.write("Score " + str(score), font_setup)
  pass

def countdown():
  global timer
  global timerInterval
  global timerUp
  global count_writer
  global countWriterX
  global countWriterY
  global font_setup
  global wn
  global spot
  # decrement counter 
  timer -= 1
  # write count 
  count_writer.goto(countWriterX, countWriterY)
  count_writer.clear()
  count_writer.write("Time " + str(timer),font_setup)

  #   if timeout, 
  #     end game 
  if( timer <= 0):
    count_writer.goto(countWriterX, countWriterY - 20)
    count_writer.write("Timer Up!")
    spot.hideturtle()
    timerUp = True
  #   else 
  #     next timer
  else:
    wn.ontimer(countdown,timerInterval)

#-----events----------------
start_game()
spot.onclick(spot_clicked)
wn.ontimer(countdown,timerInterval)
wn.bgcolor("light cyan")
wn.mainloop() 
