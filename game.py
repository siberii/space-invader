from space_invaders.invaderList import InvaderList
from space_invaders.missile import Missile
from space_invaders.pen import Pen
from space_invaders.player import Player
from space_invaders.score import Score
from space_invaders.window import Window

# Set up the screen
window = Window("black", "Space Invaders",
                "space_invaders/images/space_invaders_background.gif")
# Draw border
pen = Pen()
pen.draw_border()

# Draw score
score = Score()
pen.draw_score(score)

# Create player
Player.add_player_shape()
player = Player()

# Create the invader
invaders = InvaderList()

# Create player's bullet
missile = Missile(player, "yellow", "triangle")

window.addKeyBindings(player, missile)

# Main game loop
playerHit = False
invaderOutOfBounds = False

while not playerHit and not invaderOutOfBounds:
    invaders.move()

    playerHit = invaders.check_hit(player, missile, score, pen)
    invaderOutOfBounds = invaders.check_bounds(player, missile)

    missile.move()
    missile.check_bounds()
