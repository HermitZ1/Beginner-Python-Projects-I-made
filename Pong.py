# Turtle module is an easy way to get graphics running
import turtle

# Create title and background
wn = turtle.Screen()
wn.title("Python Pong")
wn.bgcolor("black")
wn.setup(width=800, height=900)
wn.tracer(0) # wn.tracer stops the window from updating and makes the game run faster

#Code for Paddle 1
pad_one = turtle.Turtle()
pad_one.speed(0) # This sets the speed to the maximum possible speed for the turtle module
pad_one.shape("square")
pad_one.shapesize(stretch_wid=7, stretch_len=1) # stretches the square to fit the classic pong size
pad_one.color("green")
pad_one.penup()
pad_one.goto(-350, 0)

# Code for Paddle 2
pad_two = turtle.Turtle()
pad_two.speed(0) # This sets the speed to the maximum possible speed for the turtle module
pad_two.shape("square")
pad_two.shapesize(stretch_wid=7, stretch_len=1) # stretches the square to fit the classic pong size
pad_two.color("green")
pad_two.penup()
pad_two.goto(350, 0)

# Code for the ball 
ball = turtle.Turtle()
ball.speed(0) # This sets the speed to the maximum possible speed for the turtle module
ball.shape("circle")
ball.shapesize(stretch_wid=2, stretch_len=2) # stretches the square to fit the classic pong size
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Score pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("Pad 1: 0  Pad 2: 0", align="center", font=("Courier", 24, "normal"))

# Score Variables
score_one = 0
score_two = 0

# functions for paddle movement
def pad_1_up():
    y = pad_one.ycor() # .ycor returns the y coordinate 
    y += 40
    pad_one.sety(y)

def pad_1_down():
    y = pad_one.ycor() 
    y -= 40
    pad_one.sety(y)

def pad_2_up():
    y = pad_two.ycor() 
    y += 40
    pad_two.sety(y)

def pad_2_down():
    y = pad_two.ycor()
    y -= 40
    pad_two.sety(y)


# Keyboard inputs
wn.listen()
wn.onkeypress(pad_1_up,"w")
wn.onkeypress(pad_1_down,"s")
wn.onkeypress(pad_2_up,"Up")
wn.onkeypress(pad_2_down,"Down")

# The (main game) loop :o
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
    
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
    
    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write("Pad 1: {}  Pad 2: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -490:
        ball.goto(0, 0)
        score_two += 1
        pen.clear()
        pen.write("Pad 1: {}  Pad 2: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))

    # Colliding with paddle
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < pad_two.ycor() + 50 and ball.ycor() > pad_two.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < pad_one.ycor() + 50 and ball.ycor() > pad_one.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    