from turtle import Screen
from food import Food
import time
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.keep_score()
        snake.add_tail(1)
#detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()
#detect collision with self
    for position in snake.snake[1:]:
        # if position != snake.head: use this if you do not slice it
        if snake.head.distance(position) < 10:
            scoreboard.reset()
            snake.reset_snake()


screen.exitonclick()

