from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class LoginWindow(Screen):
    pass


class MainWindow(Screen):
    pass


class AmazonClone(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(LoginWindow(name='login'))

        return sm
