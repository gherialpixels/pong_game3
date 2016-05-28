import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Button

#Main file, where program sure

class PongApp(App):
    pass
        #self.load_kv(filename="pong.kv") The filename is implicitely deduced from the class name.

if __name__ == '__main__':
    PongApp().run()