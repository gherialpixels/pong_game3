from kivy.event import EventDispatcher

#necessary? Use kivy properties instead?
class ScoreEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_top_scores')
        self.register_event_type('on_bot_scores')
        super(ScoreEventDispatcher, self).__init__(**kwargs)

    def top_scores(self):
        """
        fires the event associated with the top player scoring a
        point.
        :return: None
        """
        self.dispatch('on_top_scores')

    def bot_scores(self):
        """
        fires the event associated with the bottom player scoring
        a point.
        :return: None
        """
        self.dispatch('on_bot_scores')
