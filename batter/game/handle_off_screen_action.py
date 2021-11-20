from game.action import Action
from game.point import Point
from game import constants

class HandleOffScreenAction(Action):
    def __init__(self, sound_service):
        super().__init__()
        self._sound_service = sound_service

    def execute(self, cast):
        ball = cast["balls"][0]
        x = ball.get_position().get_x()
        y = ball.get_position().get_y() 
        dx = ball.get_velocity().get_x()
        dy = ball.get_velocity().get_y()
        if x >= constants.MAX_X - 20 or x <= 0:
            dx *= -1
            ball.set_velocity(Point(dx, dy))
        elif y <= 0:
            dy *= -1
            ball.set_velocity(Point(dx, dy))

        elif y >= constants.MAX_Y - 20:
            ball.set_velocity(Point(0,0))
            # cast["balls"].remove(ball)