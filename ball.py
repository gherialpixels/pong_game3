

class Ball:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def displayCircleText(self):
        print "Pos. X: ", self.x, ", Pos. Y: ", self.y, ", Size: ", self.size

standardBall = Ball(0, 0, 30)
