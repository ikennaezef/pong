from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.print_scores()

    def add_l_score(self):
        self.l_score += 1
        self.print_scores()

    def add_r_score(self):
        self.r_score += 1
        self.print_scores()

    def print_scores(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))
