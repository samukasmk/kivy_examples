#!/usr/bin/python

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger

class SimpleWidget(BoxLayout):

    # def __init__(self, **kwargs):
    #     super(SimpleWidget, self).__init__(**kwargs)

    def on_text_update(self, new_text):
        Logger.info("Received updates of on_text event: " + new_text)


class SimpleApp(App):

    def build(self):
        return SimpleWidget()

if __name__ == "__main__":
    SimpleApp().run()
