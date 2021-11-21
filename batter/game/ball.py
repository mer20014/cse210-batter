from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    """
    Objects that the player uses to destory the bricks

    Stereotype: Information holder

    Attriubutes: 
    _image (image): The graphic for the brick
    _width (int): The width
    _height (int): The height
    _velocity (Point): The default direction/speed the ball moves
    """
    def __init__(self):
        super().__init__()
        self._width = constants.BALL_WIDTH
        self._height = constants.BALL_HEIGHT
        self._image = constants.IMAGE_BALL
        self._velocity = Point(5,-5)

