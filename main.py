import time
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = t.Screen()
screen.title("P-P-Pong xD")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))




screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


ball = Ball()
scoreboard = Scoreboard()


game_is_on = True


while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()

    #Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



    #Detect collision with paddle
    if (ball.distance(r_paddle) < 55 and ball.xcor() > 325) or (ball.distance(l_paddle) < 55 and ball.xcor() < -325):
        ball.bounce_paddle()


        #Detect miss paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()