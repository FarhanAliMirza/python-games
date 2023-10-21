from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.x_move += (self.x_move/abs(self.x_move)*0.02)
        self.y_move += (self.y_move/abs(self.y_move)*0.02)
        print(f"{self.x_move}   {self.y_move}")

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
