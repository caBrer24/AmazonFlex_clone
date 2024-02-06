from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition

Window.size = (350, 625)


# •••••••
# TODO main window
# TODO figure out navigation drawer and tool bar
# TODO ScrollView, AppTopBar

class LoginWindow(Screen):
    pass


class Credentials(Screen):
    pass


class CreateAcc(Screen):
    pass


class ForgotPass(Screen):
    pass


class ResetPass(Screen):
    pass


class MainWindow(Screen):
    pass


class AmazonFlex(MDApp):

    main_orange = "FF9843"
    disabled_orange = "F7B787"
    disabled_text_orange = "EE7214"
    color_scrim = 0.24, 0.23, 0.25, 0.35
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(Credentials(name='credentials'))
        sm.add_widget(ForgotPass(name='forgot_pass'))
        sm.add_widget(ResetPass(name='reset_pass'))
        sm.add_widget(CreateAcc(name="create_account"))

        self.theme_cls.primary_palette = "Orange"

        return sm

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.root.get_screen('credentials').ids.password_input.password = False
        else:
            self.root.get_screen('credentials').ids.password_input.password = True

    def signin_disable(self):
        passw = self.root.get_screen('credentials').ids.password_input.text
        email = self.root.get_screen('credentials').ids.email.text
        if passw == "" and email == "":
            self.root.get_screen('credentials').ids.sign_in_button.disabled = True


if __name__ == "__main__":
    AmazonFlex().run()
