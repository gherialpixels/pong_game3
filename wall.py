from kivy.uix.widget import Widget


class Wall(Widget):
    def __init__(self, **kwargs):
        super(Wall, self).__init__(self, **kwargs)
        self.y = -1
        self.x = 0
        self.size[0] = self.get_parent_window().system_size[0]
        self.size[1] = 1

class BounceWall(Wall):
    def __init__(self, **kwargs):
        super(Wall, self).__init__(self, **kwargs)

