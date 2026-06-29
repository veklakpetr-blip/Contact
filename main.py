from ursina import *

import modules.level
from modules.controller import Controller
from modules.constants import PLAYER_SPEED, PLAYER_HEIGHT, CAMERA_FOV

app = Ursina()

player = Controller(
    position=(-25, 0, -10),
    rotation=(0, 270, 0),
    height=PLAYER_HEIGHT,
    speed=PLAYER_SPEED
)

Sky()

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
camera.fov = CAMERA_FOV

app.run()