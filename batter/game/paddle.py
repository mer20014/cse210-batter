from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.PADDLE_WIDTH
        self._height = constants.PADDLE_HEIGHT
        self._image = constants.IMAGE_PADDLE
        self._position = Point(300, 500)