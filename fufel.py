from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

player = FirstPersonController(
    position=(0, 0, 0),
    speed=7,
    model='box'
)

supra = Entity(
    model='assets/car.obj',
    position=(100, 0.3, 0),
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

app.run()