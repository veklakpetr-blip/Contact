from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

from modules.constants import PLAYER_SPEED, PLAYER_FOV, SUPRA_BORDER, SUPRA_STOP_SCALE

supra_x = -34
supra_y = 0
supra_speed = 0.5

app = Ursina()

player = FirstPersonController(
    position=(-25, 0, -10),
    rotation=(0, 270, 0),
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

ground = Entity(
    scale=10,
    model='assets/models/enviropment.obj',
    collider='mesh',
    shader=lit_with_shadows_shader
)

road = Entity(
    color=color.black,
    scale=10,
    model='assets/models/road.obj',
    collider='mesh',
    shader=lit_with_shadows_shader
)

Sky()

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
camera.fov = PLAYER_FOV

def input(key):
    if key == 'escape':
        quit()
    if held_keys['right mouse']:
        print('ddd')

def zadacha1_1():
    player.enabled = True
    global supra_x, supra_y, supra_speed
    supra.position -= Vec3(0, 0, supra_speed)

    if supra.position[2] < SUPRA_BORDER:
        supra_speed *= SUPRA_STOP_SCALE

def update():
    zadacha1_1()

app.run()