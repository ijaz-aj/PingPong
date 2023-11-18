from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_moves = 10
        self.y_moves = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_moves
        new_y = self.ycor() + self.y_moves
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_moves *= -1

    def bounce_x(self):
        self.x_moves *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()











