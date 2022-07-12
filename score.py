from turtle import Turtle, Screen
screen = Screen()


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.total = 0
        self.high_score = 0
        self.clear()
        self.calc_score()

    def calc_score(self):
        self.total += 1

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.total}  High Score : {self.high_score}", move=False, align='center', font=('Arial', 24, 'normal'))

    def reset_score(self):
        if self.total > self.high_score:
            self.high_score = self.total
        self.total = 0
        self.clear()
        self.update_score()




