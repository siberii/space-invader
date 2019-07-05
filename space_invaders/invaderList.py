from space_invaders.invader import Invader
from space_invaders.collisionChecker import CollisionChecker


class InvaderList:
    def __init__(self, n_invaders=5, ):
        self.invaders = []
        self.nInvaders = n_invaders
        Invader.add_invader_shape()
        for i in range(self.nInvaders):
            self.invaders.append(Invader())

    def move(self):
        for invader in self.invaders:
            invader.move_sideways()

            # Move all enemies backwards and downwards
            if invader.entity.xcor() > 280:
                Invader.speed *= -1
                for i in self.invaders:
                    i.move_down()

            if invader.entity.xcor() < -280:
                Invader.speed *= -1
                for i in self.invaders:
                    i.move_down()

    def check_hit(self, player, missile, score, pen):
        hit = CollisionChecker()
        for invader in self.invaders:
            # Check for bullet and enemy collision
            if hit.is_collision(missile, invader):
                hit.invader_hit(missile, invader)
                # Update Score
                score.invader_killed()
                pen.draw_score(score)
            # Check for player and enemy collision
            if hit.is_collision(player, invader):
                hit.player_hit(player, missile, self.invaders)
                print("Invaders won.")
                print("Game Over")
                return True
        return False

    def check_bounds(self, player, missile):
        for invader in self.invaders:
            if invader.entity.ycor() < -250:
                player.hide()
                missile.hide()
                for i in self.invaders:
                    i.hide()
                print("Invaders won.")
                print("Game Over")
                return True
        return False
