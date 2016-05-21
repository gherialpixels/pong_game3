
from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class ScatterTextWidget(BoxLayout):
    pass

class PingPongApp(App):
    def build(self):
        return ScatterTextWidget()

def foo():
    print "Hello"

foo()

if __name__ == "__main__":
    PingPongApp().run()