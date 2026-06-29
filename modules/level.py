from ursina import *
from ursina.shaders import lit_with_shadows_shader

texture = load_texture('assets/images/plane.png', filtering='linear')
Entity(
    model='assets/models/plane.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/road.png', filtering='linear')
Entity(
    model='assets/models/road.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/house.png', filtering='linear')
Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(50, 0, 50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(150, 0, 150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(150, 0, -150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(-50, 0, -150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(-150, 0, -50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(-150, 0, 150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(-50, 0, 50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house.obj',
    texture=texture,
    position=(50, 0, -50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/house2.png', filtering='linear')
Entity(
    model='assets/models/house2.obj',
    texture=texture,
    position=(-50, 0, -50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house2.obj',
    texture=texture,
    position=(-150, 0, 50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house2.obj',
    texture=texture,
    position=(50, 0, -150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house2.obj',
    texture=texture,
    position=(50, 0, 150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house2.obj',
    texture=texture,
    position=(150, 0, 50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/house3.png', filtering='linear')
Entity(
    model='assets/models/house3.obj',
    texture=texture,
    position=(150, 0, -50),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house3.obj',
    texture=texture,
    position=(-50, 0, 150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

Entity(
    model='assets/models/house3.obj',
    texture=texture,
    position=(-150, 0, -150),
    collider='mesh',
    shader=lit_with_shadows_shader
)

texture = load_texture('assets/images/tree.png', filtering='linear')
Entity(
    model='assets/models/tree.obj',
    texture=texture,
    double_sided=True,
    collider='mesh',
    shader=lit_with_shadows_shader
)
texture = load_texture('assets/images/curb.png', filtering='linear')
Entity(
    model='assets/models/curb.obj',
    texture=texture,
    collider='mesh',
    shader=lit_with_shadows_shader
)