from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

suprax = 100

app = Ursina()

player = FirstPersonController(
    position=(0, 0, -10),
    speed=7,
    model='box'
)

supra = Entity(
    model='assets/car.obj',
    position=(suprax, 0.3, 0),
    rotation=(0, 180, 0),
    color=color.black,
    collider='mesh',
    shader=lit_with_shadows_shader
)

# Создаем пол
ground = Entity(
    model='assets/enviropment.obj',
    collider='mesh',
    shader=lit_with_shadows_shader
)

Sky()

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))

def input(key):
    if key == "escape":
        quit()

def zadacha1():
    global suprax

    if supra.position[0] != 0:
        supra.position -= Vec3(0.5, 0, 0)

def update():
    zadacha1()

app.run()