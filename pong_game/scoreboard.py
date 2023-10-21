from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def point_l(self,):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def point_r(self,):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-100, 200)
        self.write(f"{self.score_l}", align=ALIGNMENT, font=FONT)
        self.setposition(100, 200)
        self.write(f"{self.score_r}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
