import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label

# Main file, where program sure

class PongApp(App):
    def build(self):
        b = Button(text="Hello!")
        l = Label(text="Hello",
                  size=150)
        s = Scatter()
        f = FloatLayout(orientation='vertical',
                        size=(300, 300))

        s.add_widget(l)
        f.add_widget(s)

        return f

if __name__ == '__main__':
    PongApp().run()