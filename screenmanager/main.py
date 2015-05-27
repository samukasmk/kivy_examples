# references:

# http://kivy.org/docs/api-kivy.uix.screenmanager.html
# https://www.youtube.com/watch?v=xx-NLOg6x8o
# https://github.com/inclement/kivycrashcourse/blob/master/video14-using_a_screenmanager/after.py

import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<MyScreenManager>:
    transition: FadeTransition()
    MenuScreen:
    SettingsScreen:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_release: root.on_quit_event()

<SettingsScreen>:
    name: 'settings'
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

""")

# Declare both screens
class MenuScreen(Screen):
    def on_quit_event(self):
        sys.exit(0)


class SettingsScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

# # Create the screen manager
# sm = ScreenManager()
# sm.add_widget(MenuScreen())
# sm.add_widget(SettingsScreen())

class TestApp(App):

    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    TestApp().run()
