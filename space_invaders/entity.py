from turtle import Turtle


class Entity:
    def __init__(self, color, shape):
        self.entity = Turtle()
        self.entity.color(color)
        self.entity.shape(shape)
        self.entity.penup()
        self.entity.speed(0)

    def hide(self):
        self.entity.hideturtle()

    def set_position(self, x, y):
        self.entity.setposition(x, y)

    def x_coordinate(self):
        return self.entity.xcor()

    def y_coordinate(self):
        return self.entity.ycor()