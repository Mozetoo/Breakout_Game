from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_left(self):
        x = self.xcor()
        if x > -350:
            x -= 60
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        if x < 350:
            x += 60
        self.setx(x)
