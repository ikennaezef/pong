from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.set_position(position)
        self.color("white")

    def set_position(self, position):
        self.goto(position)

    def up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)