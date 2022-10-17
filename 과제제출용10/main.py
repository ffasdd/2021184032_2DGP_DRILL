import game_framework
from pico2d import *
import play_state

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.clear_canvas()