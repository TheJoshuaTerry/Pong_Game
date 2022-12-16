from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

player_1 = Paddle((-350, 0))
screen.onkeypress(player_1.move_up, 'w')
screen.onkeypress(player_1.move_down, 's')
player_2 = Paddle((350, 0))
screen.onkeypress(player_2.move_up, 'Up')
screen.onkeypress(player_2.move_down, 'Down')

ball = Ball()
score_board = ScoreBoard()
line = Turtle()
line.goto(y=295, x=0)
line.color('white')
line.setheading(270)
line.hideturtle()
line.width(width=5)
for lines in range(20):
    line.fd(15)
    line.color('black')
    line.fd(15)
    line.color('white')

game_is_on = True

while game_is_on:
    screen.update()
    ball.moving()
    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with paddles
    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.reflect()
    # Detect if ball goes out of bounds
    if ball.xcor() > 430:
        ball.reset_position()
        score_board.l_point()
    if ball.xcor() < -430:
        ball.reset_position()
        score_board.r_point()
    time.sleep(.1)

screen.exitonclick()
