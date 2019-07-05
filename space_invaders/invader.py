import random
import turtle
from space_invaders.entity import Entity


class Invader(Entity):

    speed = 4

    def __init__(self, shape="space_invaders/images/invader.gif", x_min=-200, x_max=200, y_min=200, y_max=250):
        super().__init__("green", shape)
        self.xPos = random.randint(x_min, x_max)
        self.yPos = random.randint(y_min, y_max)
        self.entity.setposition(self.xPos, self.yPos)

    @staticmethod
    def add_invader_shape():
        turtle.register_shape("space_invaders/images/invader.gif")

    def move_sideways(self):
        x = self.entity.xcor()
        x += self.speed
        self.entity.setx(x)

    def move_down(self):
        y = self.entity.ycor()
        y -= 40
        self.entity.sety(y)

    def reset_position(self, x_min=-200, x_max=200, y_min=200, y_max=250):
        self.xPos = random.randint(x_min, x_max)
        self.yPos = random.randint(y_min, y_max)
        self.entity.setposition(self.xPos, self.yPos)
