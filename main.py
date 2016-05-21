import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label



class Pong(App):
    def build(self):
        self.load_kv(filename="main.kv")

if __name__ == '__main__':
    Pong().run()