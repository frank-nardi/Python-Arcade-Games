from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

BG_COLOR = 'black'
SCREEN_TITLE = 'Pong'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = Screen()
screen.bgcolor(BG_COLOR)
screen.title(SCREEN_TITLE)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.x_move = -13
        ball.y_move = 10 * (ball.y_move / ball.y_move)
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.x_move = 13
        ball.y_move = 10 * (ball.y_move / ball.y_move)
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
