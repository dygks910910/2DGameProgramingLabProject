import random

from pico2d import *

class Ball:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None;

    def __init__(self):
        self.x, self.y = random.randint(200, 790), 60
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class BigBall(Ball):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = random.randint(50,120)
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')

    # fill here
    def update(self, frame_time):
        #self.y -= frame_time * self.fall_speed
        def clamp(minimum,y,maximum):
            return max(minimum,min(y,maximum))
        speed = Ball.RUN_SPEED_PPS * frame_time
        self.y -= speed

        self.y = clamp(70,self.y,500)

    def stop(self):
        self.fall_speed = 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20