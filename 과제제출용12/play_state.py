from pico2d import *
import game_framework
import game_world

from grass import Grass_1
from grass import Grass_2
from boy import Boy
from ball_state import Ball


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass_1, grass_2, ball
    ball = Ball()
    boy = Boy()
    grass_1 = Grass_1()
    grass_2 = Grass_2()

    game_world.add_object(grass_1, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(grass_2, 2)
# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # for layer in game_world.objects:
    #     for game_object in layer:
    #         game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
