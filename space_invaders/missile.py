import winsound

from space_invaders.entity import Entity


class Missile(Entity):

    speed = 50

    def __init__(self, player, color, shape, height=0.5, width=0.5, xPos=None, yPos=None):
        super().__init__(color, shape)
        self.entity.setheading(90)
        self.entity.shapesize(height, width)
        self.entity.hideturtle()
        self.player = player
        self.set_position(0, -400)

    def fire_bullet(self):
        if not self.entity.isvisible():
            # Play laser sound
            winsound.PlaySound("space_invaders/sounds/laser.wav", winsound.SND_ASYNC)

            x = self.player.entity.xcor()
            y = self.player.entity.ycor() + 10
            self.entity.setposition(x, y)
            self.entity.showturtle()

    def move(self):
        if self.entity.isvisible():
            y = self.entity.ycor()
            y += self.speed
            self.entity.sety(y)

    def check_bounds(self):
        # Bullet top border collision check
        if self.entity.ycor() > 275:
            self.hide()
