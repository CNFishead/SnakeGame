import time
from turtle import Screen
from Classes.Snake import Snake
from Classes.Food import Food


# Screen Setup
screen = Screen()
# Define Borders of the game
screen.setup(width=600, height=600)
# background color
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.tailIncrease()


screen.exitonclick()
