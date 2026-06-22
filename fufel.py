from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(
    position=(0, 0, 0),
    speed=5,
    model='box'
)

supra = Entity(
    model='assets\car.obj',
    position=(0, 3, 0)
)

# Создаем пол
ground = Entity(
    model='plane',
    scale=(1000, 1, 1000),
    color=color.green,
    texture='white_cube',
    collider='box'
)

Sky()

def input(key):
    if key == "escape":
        quit()

app.run() 