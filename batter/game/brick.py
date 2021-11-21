from game.actor import Actor
from game.point import Point
from game import constants

class Brick(Actor):
    """
    Objects that the player must destroy

    Stereotype: Information holder

    Attriubutes: 
    _position (Point): The default position of the brick
    _image (image): The graphic for the brick
    _width (int): The width
    _height (int): The height
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._position = Point(0,0)
        self._image = constants.IMAGE_BRICK_ONE
        self._width = constants.BRICK_WIDTH
        self._height = constants.BRICK_HEIGHT
        