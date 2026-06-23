from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

from modules.constants import PLAYER_SPEED, PLAYER_FOV, SUPRA_BORDER, SUPRA_STOP_SCALE

supra_x = 100
supra_speed = 0.2

app = Ursina(fullscreen=True, borderless=True)

player = FirstPersonController(
    position=(0, 0, -10),
    speed=PLAYER_SPEED
)

supra = Entity(
    model='assets/models/car.obj',
    position=(supra_x, 0.3, 0),
    rotation=(0, 180, 0),
    color=color.black,
    collider='mesh',
    shader=lit_with_shadows_shader
)

ground = Entity(
    model='assets/models/enviropment.obj',
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

def zadacha1():
    global supra_x, supra_speed
    supra.position -= Vec3(supra_speed, 0, 0)

    if supra.position[0] < SUPRA_BORDER:
        supra_speed *= SUPRA_STOP_SCALE

def update():
    zadacha1()

app.run()