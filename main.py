from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition

Window.size = (350, 625)


# •••••••
# TODO screens for everything else


class LoginWindow(Screen):
    main_orange = "FF9843"


class Credentials(Screen):
    pass


class CreateAcc(Screen):
    pass


class MainWindow(Screen):
    pass


class AmazonFlex(MDApp):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Credentials(name='credentials'))
        sm.add_widget(CreateAcc(name="create_account"))
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(MainWindow(name='main'))
        self.theme_cls.primary_palette = "Orange"

        return sm

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.root.get_screen('credentials').ids.password_input.password = False
        else:
            self.root.get_screen('credentials').ids.password_input.password = True


if __name__ == "__main__":
    AmazonFlex().run()
