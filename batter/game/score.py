from game.actor import Actor
from game.point import Point

class Score(Actor):
    def __init__(self):
        super().__init__()

        self._text = "Score: "
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        self._score = 0

