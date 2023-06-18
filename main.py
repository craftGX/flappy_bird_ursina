from ursina import *
import random as r

app = Ursina()
Sky()
pipes = []
pipe = Entity(model='quad', color=color.green, texture="white_cube", position=(20, 10), scale=(3, 15, 1),
              collider='box')
player = Entity(model='cube', color=color.red, scale=(2, 2, 2), y=5, collider='box')

camera.orthographic = True
camera.fov = 20


def update():
    player.y -= 4 * time.dt
    for p in pipes:
        p.x -= 2 * time.dt


def input(key):
    if key == 'space':
        player.y += 3


def newPipe():
    y = r.randint(4, 12)
    new1 = duplicate(pipe, y=y)
    new2 = duplicate(pipe, y=y - 22)
    pipes.extend((new1, new2))
    invoke(newPipe, delay=5)


newPipe()

app.run()
