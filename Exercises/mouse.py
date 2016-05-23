import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label


class MouseText(Label):

    def on_touch_down(self, touch):
        self.text = "Down"
        return True

    def on_touch_move(self,touch):
        self.text = "Move"
        return True

    def on_touch_up(self, touch):
        self.text = "Up"
        return True


class MouseApp(App):

    def build(self):
        return MouseText(text="Click to begin")

if __name__ == "__main__":
    MouseApp().run()
