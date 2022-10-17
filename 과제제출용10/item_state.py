from pico2d import *
import game_framework
import play_state

# fill here
# running=True
image = None

def enter():
    # fill here
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def update():

    pass

def draw():
    # fill here
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type ==SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state() #이전상태인 play_state로 복귀
                case pico2d.SDLK_k:
                    play_state.boy_num +=1
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    if play_state.boy_num>1:
                        play_state.boy_num -= 1
                    game_framework.pop_state()
