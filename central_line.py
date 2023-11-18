from turtle import Turtle


class CentralLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.goto(0, 300)
        self.goto(0, -300)
