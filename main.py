from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from random import choice


# ball characteristics
def move():
    # moves the ball
    ball.move()
    # Detect collision with walls
    if ball.new_x > 390 or ball.new_x < -390:
        ball.bounce_x()
    if ball.new_y > 290:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.new_y < -240:
        ball.bounce_y()
    # Detect paddle misses and reset the ball v
    if ball.new_y < -380:
        ball.reset_position()


color_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "white"]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Paddle
paddle = Paddle((0, -250))
# Creates a Wall
wall = []
brick_width = 70
brick_height = 20
brick_y = 250
for row in range(5):
    brick_y -= brick_height + 10
    brick_x = -360
    for col in range(10):
        brick = Turtle()
        brick.shape("square")
        brick.color(choice(color_list))
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(brick_x, brick_y)
        wall.append(brick)
        brick_x += brick_width + 10
# Ball
ball = Ball()

# Paddle Control
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# Game loop
delay = 0.001
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(delay)
    move()

    # Detect collision with wall
    for brick in wall:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)  # Move brick out of sight
            ball.bounce_y()

screen.exitonclick()
