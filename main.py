import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(fun=player_1.up, key="Up")
screen.onkey(fun=player_1.down, key="Down")
screen.onkey(fun=player_2.up, key="w")
screen.onkey(fun=player_2.down, key="s")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    ball_position = ball.pos()
    print(ball.distance(player_1))
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(player_1) < 50 and ball.xcor() > 330 or ball.distance(player_2) < 50 and ball.xcor() < -330:
        ball.hit()

    if ball.xcor() > 390:
        scoreboard.add_l_score()
        ball.reset()
        ball.hit()

    if ball.xcor() < -390:
        scoreboard.add_r_score()
        ball.reset()
        ball.hit()

    screen.update()



screen.exitonclick()