import math
import winsound


class CollisionChecker:
    def __init__(self):
        pass

    @staticmethod
    def is_collision(entity1, entity2):
        dist_x = (entity1.entity.xcor()-entity2.entity.xcor())
        dist_y = (entity1.entity.ycor()-entity2.entity.ycor())
        distance = math.sqrt(dist_x**2 + dist_y**2)
        return distance < 25

    @staticmethod
    def invader_hit(missile, invader):
        # Play explosion sound
        winsound.PlaySound("space_invaders/sounds/explosion.wav", winsound.SND_ASYNC)
        # Hide and reset missile position
        missile.hide()
        missile.set_position(0, -400)
        # Reset invader position
        invader.reset_position()

    @staticmethod
    def player_hit(player, missile, invaders):
        # Play explosion sound
        winsound.PlaySound("space_invaders/sounds/explosion.wav", winsound.SND_ASYNC)
        # Hide everything
        player.hide()
        missile.hide()
        for invader in invaders:
            invader.hide()
