import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

display_message = Turtle()
display_message.hideturtle()
display_message.color("white")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game by Tehaam")

snake_list = []

mySnake = Snake()
score_card = Score()
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    mySnake.move()
    mySnake.eat()

    if mySnake.snake[0].xcor() > 290 or mySnake.snake[0].xcor() < -290 or mySnake.snake[0].ycor() > 290 or mySnake.snake[0].ycor() < -290:
        score_card.reset_score()

    for i in range(1, len(mySnake.snake)):
        if mySnake.snake[0].distance(mySnake.snake[i]) < 10:
            score_card.reset_score()


if not game_is_on:
    display_message.write(arg=f"GAME OVER", move=False, align='center', font=('Arial', 24, 'normal'))

print("GAME OVER")
screen.exitonclick()



