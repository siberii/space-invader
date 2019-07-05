from turtle import Turtle


class Pen:
    def __init__(self):
        self.borderPen = Turtle()
        self.scorePen = Turtle()

    def draw_border(self):
        self.borderPen.speed(0)
        self.borderPen.color("white")
        self.borderPen.penup()
        self.borderPen.setposition(-300, -300)
        self.borderPen.pendown()
        self.borderPen.pensize(3)
        for side in range(4):
            self.borderPen.fd(600)
            self.borderPen.lt(90)
        self.borderPen.hideturtle()

    def draw_score(self, score):
        self.scorePen.color("white")
        self.scorePen.speed(0)
        self.scorePen.penup()
        self.scorePen.setposition(-290, 280)
        self.scoreString = "Score: %s" % score.points
        self.scorePen.clear()
        self.scorePen.write(self.scoreString, False, align="left",
                            font=("Arial", 14, "normal"))
        self.scorePen.hideturtle()
