from pico2d import *
import game_world

class Grass():
    def __init__(self):
        self.image = load_image('grass.png')
        self.y = 0

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        self.image.draw(400, self.y)


