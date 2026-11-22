from ursina import *
from ursina.shaders import lit_with_shadows_shader

from modules.level import *
from modules.controller import Controller
from modules.constants import PLAYER_SPEED, PLAYER_NORMAL_HEIGHT, PLAYER_DRIVE_HEIGHT, CAMERA_FOV, SUPRA_BORDER, SUPRA_STOP_SCALE

supra_x = -34
supra_y = 0
supra_speed = 0.5

in_supra = False

app = Ursina()

player = Controller(
    position=(-25, 0, -10),
    rotation=(0, 270, 0),
    height=PLAYER_NORMAL_HEIGHT,
    speed=PLAYER_SPEED
)

supra = Entity(
    model='assets/models/car.obj',
    position=(supra_x, 0.3, supra_y),
    rotation=(0, 90, 0),
    color=color.black,
    collider='mesh',
    shader=lit_with_shadows_shader
)

Sky()

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
camera.fov = CAMERA_FOV

def input(key):
    if key == 'escape':
        quit()

    if key == 'left mouse down':
        camera_position = player.position + Vec3(0, player.height, 0)
        ray = raycast(camera_position, camera.forward, PLAYER_NORMAL_HEIGHT)
        if ray.entity == supra:
            get_in_car()

def zadacha1_1():
    global supra_x, supra_y, supra_speed
    supra.position -= Vec3(0, 0, supra_speed)

    if supra.position[2] < SUPRA_BORDER:
        supra_speed *= SUPRA_STOP_SCALE

def get_in_car():
    '''Садится в машину'''
    global in_supra
    if not in_supra:
        supra.parent = player
        supra.position = (0, 0, 0)
        supra.rotation = (0, -90, 0)

        player.set_height(PLAYER_DRIVE_HEIGHT)
        in_supra = True

def update():
    zadacha1_1()

app.run()