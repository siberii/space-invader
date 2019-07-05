import turtle

from space_invaders.entity import Entity


class Player(Entity):

    speed = 15

    def __init__(self, shape="space_invaders/images/player.gif", xPos=0, yPos=-250):
        super().__init__("blue", shape)
        self.entity.setposition(xPos, yPos)
        self.entity.setheading(90)

    @staticmethod
    def add_player_shape():
        turtle.register_shape("space_invaders/images/player.gif")

    def move_left(self):
        x = self.entity.xcor()
        x -= self.speed
        if x < -280:
            x = -280
        self.entity.setx(x)

    def move_right(self):
        x = self.entity.xcor()
        x += self.speed
        if x > 280:
            x = 280
        self.entity.setx(x)
