from game.action import Action
from game.score import Score
import raylibpy

class HandleLevelAction(Action):
    def __init__(self, output_service):
        super().__init__()
        self._output_service = output_service
        self.score = Score()

    def execute(self, cast):
        score = 0
        # self._text = f"Score: {score}"
        brick_count = len(cast["bricks"])
        
        score = 64 - brick_count
        
        raylibpy.draw_text(f"Score: {score}", 0, 550, 15, raylibpy.WHITE)
