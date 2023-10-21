from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "i")
screen.onkey(r_paddle.down, "k")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if (ball.xcor() > 330 and ball.distance(r_paddle) < 50) or (ball.xcor() < -330 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 360:
        scoreboard.point_l()
        ball.reset()
    if ball.xcor() < -360:
        scoreboard.point_r()
        ball.reset()

screen.exitonclick()
