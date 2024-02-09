from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = (350, 625)


# •••••••
# TODO add functionality to settings
# TODO during weekend, align everything, figure out color problems
# TODO due to theme switching
# TODO start looking into map implementation, camera, etc
# TODO slide button tutorial

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


class SettingScreen(Screen):
    pass

class MainWindow(Screen):
    pass




class AmazonFlex(MDApp):

    main_orange = "FF9843"
    disabled_orange = "F7B787"
    disabled_text_orange = "EE7214"
    color_scrim = 0.24, 0.23, 0.25, 0.35

    dialog = None

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(Credentials(name='credentials'))
        sm.add_widget(ForgotPass(name='forgot_pass'))
        sm.add_widget(ResetPass(name='reset_pass'))
        sm.add_widget(CreateAcc(name="create_account"))
        sm.add_widget(SettingScreen(name="screen_options"))




        return sm

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.root.get_screen('credentials').ids.password_input.password = False
        else:
            self.root.get_screen('credentials').ids.password_input.password = True

    def on_switch_active(self, switch, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


    def signin_disable(self):
        passw = self.root.get_screen('credentials').ids.password_input.text
        email = self.root.get_screen('credentials').ids.email.text
        if passw == "" and email == "":
            self.root.get_screen('credentials').ids.sign_in_button.disabled = True

    def app_theme(self):
        self.theme_cls.primary_palette = "Orange"

    def checking_updates(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Your version is up to date.",
                type="simple",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.main_orange,
                        on_release=lambda _: self.dialog.dismiss()

                    )
                ],
            )

        self.dialog.open()




if __name__ == "__main__":
    AmazonFlex().run()
