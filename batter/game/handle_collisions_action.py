from game.action import Action
from game import constants
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        balls = cast["balls"]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        #score = cast["score"][0]

        for ball in balls:
            if self._physics_service.is_collision(ball, paddle):
                dx = ball.get_velocity().get_x()
                dy = ball.get_velocity().get_y()
                dy *= -1
                ball.set_velocity(Point(dx, dy))
                self._audio_service.play_sound(constants.SOUND_BOUNCE)

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                dx = ball.get_velocity().get_x()
                dy = ball.get_velocity().get_y()
                dy *= -1
                ball.set_velocity(Point(dx, dy))
                self._audio_service.play_sound(constants.SOUND_BOUNCE)
                bricks.remove(brick)
                #score += 1
                

        # ball_x = ball.get_position().get_x()
        # ball_y = ball.get_position().get_y()
