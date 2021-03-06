﻿from pico2d import *

import game_framework


from boy import FreeBoy as Boy # import Boy class from boy.py
from background import FixedBackground as Background
import UI

name = "scroll_state"

boy = None
background = None
ui = None

def create_world():
    global boy, background,ui
    ui = UI.UI()
    boy = Boy()
    background = Background()
    background.set_center_object(boy)
    boy.set_background(background)


def destroy_world():
    global boy, background
    del(boy)
    del(background)


def enter():
    open_canvas(800, 600)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)
                background.handle_event(event)



def update(frame_time):
    boy.update(frame_time)
    background.update(frame_time)
    ui.update()


def draw(frame_time):
    clear_canvas()
    background.draw()
    boy.draw()
    ui.draw()
    update_canvas()






