from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global dir
    global ydir
    global running
    global x
    global y
    global animation_num
    global move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                animation_num = 1
                if x <1240:
                    dir = 0
                elif x > 1240:
                    dir = 4
                    animation_num = 3
            elif event.key == SDLK_LEFT:
                animation_num = 0
                if x < 0:
                    animation_num = 2
                    dir=4
                elif x > 0:
                    dir = 1
            elif event.key == SDLK_UP:
                if y > 0:
                    dir = 3
                elif y < 0:
                    dir = 4
                    animation_num = 3
            elif event.key == SDLK_DOWN:
                if y > 1024:
                    animation_num = 2
                    dir = 4
                elif y< 1024:
                    dir = 2
        elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1
    pass

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
move = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 4
ydir = 0
animation_num=1
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * animation_num, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if dir == 0:
        x += 5
    elif dir == 1:
        x -= 5
    elif dir == 2:
        y -= 5
    elif dir == 3:
        y += 5
    elif dir == 4:
        y=y
        x=x
    delay(0.01)

close_canvas()