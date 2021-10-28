#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.

# modified by Brian Schick to have turtles collide, 
#  turn around, move a short time, turn around and try again. 
# Will have a turtle game. Player turtle moves toward mouse click,
#   avoiding AI turtles which move randomly around, random turns, 
#   when collide, back up, turn, and try again. 
# Want timer as score - how long avoid collisions 
# Similar to Asteroids

# TODOs
# Research callback functions with parameters. Can Turtle do it?
#   so far, timer callback no parameters. 
# Add player turtle and move toward mouse click

import turtle as trtl

def initializeTurtles():
  #create the screen to access screen size
  global wn
  wn = trtl.Screen()
  screenWidth = 400
  screenHeight = 400
  wn.screensize(screenWidth,screenHeight)

  # turtle starting arrangement
  global turtleSpacing
  turtleSpacing = 40
  global turtleSpeed
  turtleSpeed = 2 #pixels per step
  global stepsPerSecond
  stepsPerSecond = 60
  global collideCount
  collideCount = 0
  global collisionDistance
  collisionDistance = 2 #pixels

  # create two empty lists of turtles, adding to them later
  global horiz_turtles
  horiz_turtles = []
  global vert_turtles
  vert_turtles = []

  # and one turtle for the player
  global playerTurtle

  # use interesting shapes and colors
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
  vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

  # set up initial positions
  # there two lines of six turtles each
  # vertical-moving turtles line up on top of the screen
  #    and move down 
  # horizontal-moving turtles line up on the left of the screen 
  #    and move right
  tloc = screenWidth/2 - 3*turtleSpacing # first place in each line
  
  # interate through turtle lists creating turtles and
  #    setting their starting heading and positions
  for s in turtle_shapes:

    # next horizontal-travelling turtle.
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()  # note how colors are thrown away.
    ht.fillcolor(new_color)
    ht.goto(-screenWidth/2 + turtleSpacing, tloc)  # left side of screen (x),
    #                                                 top to bottom (y)
    ht.setheading(0) # head right

    # next vertical-travelling turtle.
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()   # note colors thrown away
    vt.fillcolor(new_color)
    vt.goto( -tloc, screenWidth/2 - turtleSpacing)  # left to right (x),
    #                                                 top of screen (y)
    vt.setheading(270) # head down
  
    tloc -= turtleSpacing
  
  # and set up the player turtle in the middle
  playerTurtle = trtl.Turtle() 
  playerTurtle.setheading(135)   # heading up and left

# TODO: move turtles across and down screen, stopping for collisions
# best done in a callback procedure.
def updateTurtles():
  '''updateTurtles():
      Move all turtles, then 
      check for collisions between line turtles'''
  if(moveTurtles()):   # move the turtles
    wn.ontimer(updateTurtles,int(1000/stepsPerSecond))  # submit next move
  else:
    wn.bye()    # if no turtles move, end the game

  processCollisions()

def processCollisions():
  '''processCollisions
      If a vertical turtle and a horizontal turtle touch
      have them change to a different color and
      reverse direction for a short time'''
  # not fully implemented
  # currently, horizontal turtles turn around when collide.
  # onTimer callback accepts only parameterless function. 
  # TODO: How to pass a function with parameters to a callback?
  global horiz_turtles
  global vert_turtles
  global wn
  global collideCount
  global collisionDistance
  global turtleSpacing

  # check to see if any vertical turtle collides with
  #   this horizontal turtle. 
  # if it does, turn the horizontal turtle to move to the left
  for hTurtle in horiz_turtles:
    for vTurtle in vert_turtles:
      if hTurtle.distance(vTurtle) < collisionDistance:
        collideCount+=1
        print("DEBUG: collided",collideCount)
        # hTurtle.back(turtleSpacing)
        hTurtle.setheading(180)
        # wn.ontimer(hTurtle.heading,0,6)
        # vTurtle.heading(90)
        # wn.onTimer(vTurtle.heading(270),6)

def moveTurtles():
  '''moveTurtles()
     Moves all turtles on screen.
     Does not move turtles off screen.
     Applies a 10 px margin around screen
     
     return: True if any AI turtle moved
             False if no AI turtle moved
  '''
  # globals
  global horiz_turtles
  global vert_turtles
  global playerTurtle
  global turtleSpeed
  global wn

  # initialize values
  screenMargin = 10
  moved = False   # boolean to flag if even one turtle moved.
  # set up 'edges' of the screen, leaving a margin around the edges
  # turtle coords are 0,0 in center of screen
  right, bottom = wn.screensize()
  right/=2
  bottom/=-2
  left = -right
  top = -bottom

  #move turtles until they reach the edge of the screen
  playerTurtle.forward(turtleSpeed)
  for mover in horiz_turtles: # horiz_turtles move to left and right
    if( mover.xcor() < right-screenMargin and mover.xcor() > left+screenMargin ):
      mover.forward(turtleSpeed)
      moved=True
  for mover in vert_turtles: # vert_turtles move to top and bottom
    if( mover.ycor() > bottom+screenMargin and mover.ycor() < top-screenMargin ):
      mover.forward(turtleSpeed)
      moved=True
  return moved

def goHere(x,y):
  '''goHere(x,y)
     x: the x coor of the mouse when clicked
     y: the y coor of the mouse when clicked
     
     sets the heading of the player turtle towards 
       the mouse click
  '''
  global playerTurtle
  playerTurtle.setheading(playerTurtle.towards(x,y))

"""
steps = 0
while steps < 50:
	steps = steps + 1
"""

# here's the main program
initializeTurtles()
wn.ontimer(updateTurtles,int(1000/stepsPerSecond))
wn.onclick(goHere)
wn.mainloop()

print("That's all, folks!")