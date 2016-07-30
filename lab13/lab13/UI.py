from pico2d import *
class UI:
    def __init__(self):
        self.score = 0
        self.font = load_font('ConsolaMalgun.ttf',40)
        self.time = 0.0

    def draw(self):
        self.font.draw(400,550,"SCORE:%d,TIME:%f"%(self.score,self.time))
        print("score %d TIME:%f"%(self.score,self.time))
        pass
    def update(self):
        self.time = get_time()


def test_ui():
    open_canvas()
    ui = UI()
    ui.draw()

    for i in range(0,100):
        ui.score =i
        clear_canvas()
        ui.update()
        ui.draw()
        
        update_canvas()

    delay(0.01)
    close_canvas()

if __name__ == '__main__':
    test_ui()