from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# Creates the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Moves the snake forwards
go = True
while go:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Collision of snake with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Collision of snake with tail
    no_head = snake.parts[1:len(snake.parts)]
    for part in no_head:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
