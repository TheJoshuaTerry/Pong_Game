from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.starting_point(position)

    def starting_point(self, position):
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 250:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -225:
            self.goto(self.xcor(), new_y)
