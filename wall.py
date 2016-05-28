from kivy.uix.widget import Widget
from kivy.clock import Clock
import pong


class Wall(Widget):
    def on_ball_contact(self):
        """
        This method is called when the ball touches the wall.
        It should be overridden.
        :return: None
        """
        pass

    def __init__(self, **kwargs):
        super(Wall, self).__init__(self, **kwargs)
        Clock.schedule_interval(self.on_ball_contact,
                                1/pong.FRAME_RATE)



class BounceWall(Wall):
    def __init__(self, **kwargs):
        super(Wall, self).__init__(self, **kwargs)


class ScoreWall(Wall):
    def __init__(self, **kwargs):
        super(Wall, self).__init__(self, **kwargs)