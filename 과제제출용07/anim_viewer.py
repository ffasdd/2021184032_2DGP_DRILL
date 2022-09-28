from pico2d import *
open_canvas()
zelda = load_image('zelda.png')
character_run = load_image('run.png')
curbe = load_image('curbe.png')
walk = load_image('walk.png')

def animation1():
    # bottom
    frame_1 = 0
    for x_1 in range(30,728,13):
        clear_canvas()
        zelda.clip_draw(frame_1*96, 0, 96, 104, x_1, 50)
        update_canvas()
        frame_1 = (frame_1+1) % 10
        delay(0.05)
        get_events()
    # right
    frame_1 = 0
    for y_1 in range(30,560,13):
        clear_canvas()
        zelda.clip_draw(frame_1 * 96, 104, 96, 104, 750, y_1)
        update_canvas()
        frame_1 = (frame_1+1) % 10
        delay(0.05)
        get_events()
    # top
    frame_1 = 0
    for x_2 in range(769, 30, -13):
        clear_canvas()
        zelda.clip_draw(frame_1 * 96, 208, 96, 104, x_2, 540)
        update_canvas()
        frame_1 = (frame_1 + 1) % 10
        delay(0.05)
        get_events()
    # left
    frame_1 = 0
    for y_1 in range(560,30,-13):
        clear_canvas()
        zelda.clip_draw(frame_1 * 96, 312, 96, 104, 40, y_1)
        update_canvas()
        frame_1 = (frame_1+1) % 10
        delay(0.05)
        get_events()

def animation2():
    frame_1 = 0
    frame_2 = 0
    x_2 = 0
    # bottom range
    while (x_2<800):
        for num in range(1, 5, 1):
            clear_canvas()
            character_run.clip_draw(frame_1 * 172, 0, 172, 183, x_2, 200)
            update_canvas()
            frame_1 = (frame_1 + 1) % 5
            delay(0.05)
            x_2 += 13
            get_events()
        for num in range(1, 5, 1):
            clear_canvas()
            character_run.clip_draw(frame_2 * 172, 160, 172, 183, x_2, 200)
            update_canvas()
            frame_2 = (frame_2 + 1) % 5
            delay(0.05)
            x_2 += 13
            get_events()

def animation3():
    frame_3 = 0
    for x_3 in range(0, 800, 8):
        clear_canvas()
        curbe.clip_draw(frame_3 * 66, 0, 66, 55, x_3, 50)
        update_canvas()
        frame_3 = (frame_3 + 1) % 8
        delay(0.05)
        get_events()

def animation4():
    # bottom
    frame_4 = 0
    for x_4 in range(0,800,10):
        clear_canvas()
        walk.clip_draw(frame_4 * 64, 64, 64, 64, x_4, 50)
        update_canvas()
        frame_4 = (frame_4 + 1) % 4
        delay(0.05)
        get_events()
    # right
    frame_4 = 0
    for y_4 in range(0,600,10):
        clear_canvas()
        walk.clip_draw(frame_4 *64, 0, 64, 64, 750, y_4)
        update_canvas()
        frame_4 = (frame_4 + 1) % 4
        delay(0.05)
        get_events()
    # top
    frame_4 = 0
    for x_4 in range(800,0,-10):
        clear_canvas()
        walk.clip_draw(frame_4 * 64, 128, 64, 64, x_4, 540)
        update_canvas()
        frame_4 = (frame_4 + 1) % 4
        delay(0.05)
        get_events()
    # left
    frame_4 = 0
    for y_4 in range(600,0,-10):
        clear_canvas()
        walk.clip_draw(frame_4 * 64,192,64,64,30, y_4)
        update_canvas()
        frame_4 = (frame_4 + 1) % 4
        delay(0.05)
        get_events()

while True:
    for x in range(1,3,1):
        animation1()
    for x in range(1, 3, 1):
        animation2()
    for x in range(1, 3, 1):
        animation3()
    for x in range(1, 3, 1):
        animation4()
close_canvas




























