import turtle
import winsound
# creating a window
win = turtle.Screen()
win.title("Pong Game")  # window title
win.bgcolor("#0c264f")  # b ackground color
win.setup(width=800, height=600)  # window dimensions
win.tracer(delay=0)  # no animation delay

left_score = 0
right_score = 0

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.speed(0)  # maximum speed for the movement of left paddle
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1) # width of pedal is 100 px
                                                    # length of pedal is 20 px
left_paddle.penup()  # no tailing coordinate
left_paddle.goto(-350, 0)
# total width is 800, so 350 to left and 350 to right have some space unused.

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1) 
right_paddle.speed(0)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(350, 0)  # on the other side of the screen

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2 # movement of ball right by 2 px
ball.dy = 2

# Pen (score-board)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(0,0), align="center", font=("Comic Sans MS", 24, "bold italic" ))

'''
Movement of left and right paddles up and down.
'''
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20 # move paddle up by 20 units
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Keyboard Input 
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("edge_sound.wav", winsound.SND_ASYNC)
    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("edge_sound.wav", winsound.SND_ASYNC)
    if(ball.xcor() > 390):
        winsound.PlaySound("edge_sound.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        left_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(left_score, right_score), align="center", font=("Comic Sans MS", 24, "bold italic"))
    if(ball.xcor() < -390):
        winsound.PlaySound("edge_sound.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        right_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(left_score, right_score),
        align="center", font=("Comic Sans MS", 24, "bold italic"))

    # pedal borders
    if(right_paddle.ycor() > 250):
        right_paddle.sety(250)
    if(right_paddle.ycor() < -250):
        right_paddle.sety(-250)
    if(left_paddle.ycor() > 250):
        left_paddle.sety(250)
    if(left_paddle.ycor() < -250):
        left_paddle.sety(-250)
    
    # ball and pedal collision
    if(ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        winsound.PlaySound("collision_sound.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1
    if(ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() -40):
        winsound.PlaySound("collision_sound.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1




