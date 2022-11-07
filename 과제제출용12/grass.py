from pico2d import *
import game_world

class Grass_1:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 40)

    def update(self):
        self.image.draw(400, 40)

class Grass_2:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 10)

    def update(self):
        self.image.draw(400, 10)


