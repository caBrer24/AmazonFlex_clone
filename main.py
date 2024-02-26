from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import IconRightWidget
from kivymd.uix.list import MDList
from kivy_garden.mapview import MapView

Window.size = (350, 625)


# •••••••

# TODO start looking into map implementation, camera, etc
# TODO slide button tutorial
# TODO change screen through itinerary
# TODO change screen through itinerary
# TODO change screen through itinerary
# TODO Adjust width of each tab
# If I wanted to reference the address on my stop list, how would I do it??

# Tab class
class Tab(MDFloatLayout, MDTabsBase):
    pass


class LoginWindow(Screen):
    pass


# Screens
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
    def __init__(self, **kw):
        super(MainWindow, self).__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font_size)

    def set_toolbar_font_size(self, *args):
        self.ids.toolbar.ids.label_title.font_size = "14sp"

    def on_pre_enter(self, *args):

        # Definitely not an optimal way to reference my MDList but is the only thing that's worked so far
        md_list = self.ids.main_screens.get_screen("itinerary").children[0].children[1].children[0].children[0].children[0].children[0].children[0]

        for i in range(1, 25):
            line_item = TwoLineIconListItem(text=f"[size=18]{i} Country Place dr[/size]",
                                            secondary_text=f"[size=14]Deliver 1 package[/size]",
                                            on_release=self.change_screen
                                            )

            icon = IconLeftWidget(icon="map-marker-outline")
            md_list.add_widget(line_item)

            line_item.add_widget(icon)

    def change_screen(self, ins):
        self.manager.current = 'in_stop_interface'


class InStopInterface(Screen):
    pass


class StopList(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pos_hint = {"top": 1.02}

        md_list = MDList()
        self.add_widget(md_list)

        for i in range(1, 25):
            line_item = TwoLineIconListItem(text=f"[size=18]{i} Country Place dr[/size]",
                                            secondary_text=f"[size=14]Deliver 1 package[/size]")


            icon = IconLeftWidget(icon="map-marker-outline")

            md_list.add_widget(line_item)
            line_item.add_widget(icon)


class AmazonFlex(MDApp):
    main_orange = "FF9843"
    disabled_orange = "F7B787"
    disabled_text_orange = "EE7214"

    # navigation drawer
    color_scrim = 0.24, 0.23, 0.25, 0.75

    # pop up in settings
    dialog = None

    # canvas color
    bg_col = ListProperty([1, 1, 1, 1])

    def build(self):
        sm = ScreenManager(transition=NoTransition())

        screens = [MainWindow(name='main'), Credentials(name='credentials'), LoginWindow(name='login'),
                   ForgotPass(name='forgot_pass'), ResetPass(name='reset_pass'), CreateAcc(name="create_account"),
                   SettingScreen(name="screen_options"), InStopInterface(name="in_stop_interface")]

        for screen in screens:
            sm.add_widget(screen)

        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"

        return sm

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.root.get_screen('credentials').ids.password_input.password = False
        else:
            self.root.get_screen('credentials').ids.password_input.password = True

    def on_switch_active(self, switch, value):
        if value:
            self.theme_cls.theme_style = "Dark"
            self.bg_col = 0.15, 0.15, 0.15, 1

        else:
            self.theme_cls.theme_style = "Light"
            self.bg_col = 1, 1, 1, 1

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

    def change_background(self, inst, bg_col):
        if self.theme_cls.theme_style == "Dark":
            self.bg_col = 0, 0, 0, 1

        else:
            self.bg_col = 1, 1, 1, 1
if __name__ == "__main__":
    AmazonFlex().run()
