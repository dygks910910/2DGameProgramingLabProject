from pico2d import *

class TUI:
    def __init__(self):
        self.font = load_font("ConsolaMalgun.ttf",40)
        self.time = get_time()
    def draw(self):
        self.font.draw(400,300,'TIME:%f'%self.time)
        print("TIME:%f"%(self.time))
    def update(self):
        self.time = get_time()

def test_ui():
    open_canvas()
    ui = TUI()
    ui.draw()
    for i in range(0,100):
        ui.update()
        ui.draw()
        update_canvas()
    delay(0.01)
    close_canvas()


if __name__ == '__main__':
    test_ui()