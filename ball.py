from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.speed(1)
        self.setheading(45)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.move_speed = 0.1