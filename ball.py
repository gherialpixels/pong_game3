

class Ball:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def display_circle_text(self):
        print "Pos. X: ", str(self.x), ", Pos. Y: ", str(self.y), ", Size: ", str(self.size)

standardBall = Ball(0, 0, 30)
