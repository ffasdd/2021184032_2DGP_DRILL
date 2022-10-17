from pico2d import *
import game_framework
import item_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 400), 90
        self.dir=1
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*1
        if self.x > 800:
            self.x=800
            self.dir=-1
        elif self.x<0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir ==1 :
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        if self.dir ==-1 :
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
             if event.key == SDLK_ESCAPE:
                game_framework.quit()
             elif event.key == SDLK_b:
                 game_framework.push_state(item_state)


boy = None #c NULL
grass = None
boy_num=1

# running = True

def draw_world():
    global team
    grass.draw()
    for x in range(0, boy_num, 1):
        boy.draw()

#초기화 함수
def enter():
    global boy, grass, running
    for x in range (0,boy_num,1):
        boy = Boy()
    grass = Grass()
    running = True

#종료
def exit():
    global boy, grass
    del boy
    del grass

#월드에 존재하는 객체들을 업데이트
def update():
    for x in range(0, boy_num, 1):
        boy.update()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass
def resume():
    pass
