from kivy.uix.widget import Widget


class Wall(Widget):
    def __init__(self, **kwargs):
        super(Wall, self).__init__(self, **kwargs)
        self.y = -1
        self.x = 0
        self.size_hint_x = self.get_root_window().system_size #works?

