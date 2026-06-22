from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(
    position=(0, 0, 0),
    speed=7,
    model='box'
)

supra = Entity(
    model='assets/car.obj',
    position=(0, 1, 0)
)

# Создаем пол
ground = Entity(
    model='assets/enviropment.obj',
    texture='white_cube',
    collider='box'
)

Sky()

def input(key):
    if key == "escape":
        quit()

app.run()