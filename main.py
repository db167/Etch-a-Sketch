from turtle import Turtle, Screen


david = Turtle()
screen = Screen()
 
def moveForward():
  david.forward(10)

def moveBackward():
	david.back(10)
	

def turnLeft():
	david.left(10)

def turnRight():
	david.right(10)

def reset():
	david.clear()
	david.penup()
	david.home()
	david.pendown()

print ( '''
Forward: space
Turn Right:d
Turn Left: a
Move Backward: s
Reset: c
''')


screen.onkey(reset, "c")

screen.listen()
screen.onkey(moveForward, "space")
screen.onkey(turnRight, "d")
screen.onkey(turnLeft, "a")
screen.onkey(moveBackward, "s")
screen.exitonclick()
