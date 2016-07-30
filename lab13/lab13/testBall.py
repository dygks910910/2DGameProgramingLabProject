class testBall():
    def __init__(self):
        pass
    def draw(self):
        print("ball")






ballList=[]
for i in range(0,100):
    ballList.append(testBall())
for i in range(0,100):
    ballList[i].draw()


