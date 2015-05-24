#!/usr/bin/python

import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.logger import Logger


class MyFirstWidget(BoxLayout):

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.ids.minha_ref.text))


class ButtonsApp(App):

    def build(self):
        return MyFirstWidget()

if __name__ == "__main__":
    __version__ = "0.1.0"
    ButtonsApp().run()
