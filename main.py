from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
from central_line import  CentralLine
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((358, 0))
l_paddle = Paddle((-358, 0))
ball = Ball()
score_board = ScoreBoard()
central_line = CentralLine()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # when the ball hits the upper boundary or lower boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check if the ball hits the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
