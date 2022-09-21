from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
while(True):
    x = 0
    while (x<770):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)
    y = 80
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(770,y)
        y=y+2
        delay(0.01)
    x=800
    while (x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,570)
        x=x-2
        delay(0.01)
    y=600
    while(y>30):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(30,y)
        y=y-2
        delay(0.01)

    x=0
    y=0
    px=0
    py=0
    while (x<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        px=math.cos(x)*300
        py=math.sin(y)*300
        character.draw_now(px+400,py+350)
        x=x+2
        y=y+2
        delay(0.02)

    

close_canvas()
