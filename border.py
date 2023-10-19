from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.init_pen()
        self.draw_border()

    def init_pen(self):
        self.hideturtle()
        self.color("green")
        self.penup()
        self.goto(-300, -290)
        self.pendown()
        self.pensize(10)

    def draw_border(self):
        for i in range(5):
            self.forward(590)
            self.left(90)

