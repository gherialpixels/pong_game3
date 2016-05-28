import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
kivy.require('1.9.1')


# Main file, where program starts

FRAME_RATE = 60.0

class ScatterTextWidget(BoxLayout):
    pass

class PongApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == '__main__':
    PongApp().run()