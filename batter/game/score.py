from game.actor import Actor
from game.point import Point

class Score(Actor):
    """
    Number that tells the player how well they are doing

    Stereotype: Information Holder

    Attributes:
    _text (string): The default text
    _position (Point): The default position
    _velocity (Point): Default movement
    _score (int): The starting score value
    """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()

        self._text = "Score: "
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        self._score = 0

