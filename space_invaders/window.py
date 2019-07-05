import turtle


class Window:
    def __init__(self, color, title, background):
        self.screen = turtle.Screen()
        self.screen.bgcolor(color)
        self.screen.title(title)
        self.screen.bgpic(background)

    def addKeyBindings(self, player,  missile):
        turtle.listen()
        turtle.onkeypress(player.move_left, "Left")
        turtle.onkeypress(player.move_right, "Right")
        turtle.onkeypress(missile.fire_bullet, "space")
