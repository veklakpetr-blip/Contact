from ursina import *
from ursina.shaders import lit_with_shadows_shader

from modules.controller import Controller
from modules.constants import PLAYER_SPEED, PLAYER_HEIGHT, CAMERA_FOV

app = Ursina()

player = Controller(
    position=(-25, 0, -10),
    rotation=(0, 270, 0),
    height=PLAYER_HEIGHT,
    speed=PLAYER_SPEED
)

texture = load_texture('assets/images/plane.png', filtering='linear')
plane = Entity(
    model='assets/models/plane.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/road.png', filtering='linear')
road = Entity(
    model='assets/models/road.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/house.png', filtering='linear')
house = Entity(
    model='assets/models/house.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/house2.png', filtering='linear')
house2 = Entity(
    model='assets/models/house2.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/house3.png', filtering='linear')
house3 = Entity(
    model='assets/models/house3.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/tree.png', filtering='linear')
tree = Entity(
    model='assets/models/tree.obj',
    texture=texture,
    double_sided=True,
    collider='mesh',
    shader=lit_with_shadows_shader
)

Sky()

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
camera.fov = CAMERA_FOV

app.run()