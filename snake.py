import time
from turtle import Turtle, Screen
from food import Food
import random
from score import Score

screen = Screen()
hunger = Food()
scorecard = Score()


class Snake:

    def __init__(self):

        print("Welcome to the game")
        self.snake = []

        for snake_index in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            self.snake.append(segment)

        x = 0
        y = 0

        for item in self.snake:
            item.goto(x, y)
            x -= 20

    def move(self):

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].position())

        endx = self.snake[0].xcor()
        endy = self.snake[0].ycor()

        if endx >= 350:
            screen.tracer(0)
            self.snake[0].goto(-330, endy)
            time.sleep(0.5)
            screen.update()

        if endx <= -350:
            screen.tracer(0)
            self.snake[0].goto(330, endy)
            time.sleep(0.5)
            screen.update()

        if endy >= 350:
            screen.tracer(0)
            self.snake[0].goto(endx, -330)
            time.sleep(0.01)
            screen.update()

        if endy <= -350:
            screen.tracer(0)
            self.snake[0].goto(endx, 330)
            time.sleep(0.01)
            screen.update()

        self.snake[0].forward(20)

        def turn_east():
            self.snake[0].setheading(0)

        def turn_north():
            self.snake[0].setheading(90)

        def turn_west():
            self.snake[0].setheading(180)

        def turn_south():
            self.snake[0].setheading(270)

        screen.listen()
        screen.onkey(key="Right", fun=turn_east)
        screen.onkey(key="Up", fun=turn_north)
        screen.onkey(key="Left", fun=turn_west)
        screen.onkey(key="Down", fun=turn_south)

    def eat(self):
        if self.snake[0].distance(hunger) < 15:

            screen.tracer(0)

            hunger.clear()
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            self.snake.append(segment)

            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            scorecard.update_score()
            scorecard.calc_score()
            scorecard.update_score()
            hunger.goto(x, y)

            time.sleep(0.01)
            screen.update()




