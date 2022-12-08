from turtle import Turtle
MOVE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):

        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)
