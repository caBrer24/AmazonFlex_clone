from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition

Window.size = (350, 625)


class LoginWindow(Screen):
    main_orange = "FF9843"


class Credentials(Screen):
    pass


class MainWindow(Screen):
    pass


class AmazonFlex(MDApp):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Credentials(name='credentials'))
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(MainWindow(name='main'))

        return sm


if __name__ == "__main__":
    AmazonFlex().run()