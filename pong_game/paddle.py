from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(5, 1)
        self.setposition(self.position)

    def up(self):
        if self.ycor() < 290:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -290:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
