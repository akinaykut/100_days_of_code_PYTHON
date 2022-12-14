from turtle import Turtle, Screen
from racket import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.start_again()
    elif ball.xcor() < -400:
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.start_again()

    if scoreboard.r_score > 10:
        print("Game over")
        game_is_on = False
    elif scoreboard.l_score > 10:
        print("Game over")
        game_is_on = False

screen.exitonclick()