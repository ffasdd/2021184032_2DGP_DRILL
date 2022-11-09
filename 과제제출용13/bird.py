import random

from pico2d import *

import game_framework
import game_world




PIXEL_PER_METER = (10.0/1.0)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0,500), random.randint(70,110)
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

        self.timer = 100

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame)*229, 337, 229, 168, self.x, self.y, 50,50)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100,3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)

