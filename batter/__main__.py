import random

import raylibpy
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.score import Score
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.handle_level_action import HandleLevelAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["bricks"] = []
    bricks = []
    brick = Brick()

    x = brick.get_position().get_x()
    y = brick.get_position().get_y()    

    for y in range(0, constants.MAX_Y - 400, 50):
        for x in range(0, constants.MAX_X, 50):
            brick = Brick()
            position = Point(x, y)
            brick.set_position(position)
            brick.set_height(brick._height)
            brick.set_width(brick._width)
            brick.set_image(brick._image)
            bricks.append(brick)

    cast["bricks"] = bricks

    cast["balls"] = []
    # TODO: Create a ball here and add it to the list

    balls = []
    ball = Ball()

    position = Point(200,400)
    ball.set_position(position)
    balls.append(ball)

    cast["balls"] = balls


    cast["paddle"] = []
    paddles = []
    
    paddle = Paddle()
    paddle.set_height(paddle._height)
    paddle.set_width(paddle._width)
    paddle.set_image(paddle._image)
    x = paddle.get_position().get_x()
    y = paddle.get_position().get_y()
    paddle.set_position(Point(x,y))
    paddles.append(paddle)

    cast["paddle"] = paddles

    # score = Score()
    # score.set_position(Point(constants.MAX_X, 0))
    # score.set_text(f"Score: {score._score}")
    
    

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction(audio_service)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)
    handle_level_action = HandleLevelAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action, handle_level_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    if ball.get_velocity() is Point(0,0):      
        audio_service.play_sound(constants.SOUND_OVER)

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
