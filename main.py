import random

from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
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
# TODO Adjust width of each tab?
# TODO reference info menu in the correct way
# TODO implement info menu and swipeTofinish button

# Tab class
class Tab(MDFloatLayout, MDTabsBase):
    pass


class Box(MDBoxLayout):
    """ Used for MDCard information purposes"""


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

    packages = random.randint(10, 355)

    def __init__(self, **kw):
        super(MainWindow, self).__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font_size)

    def set_toolbar_font_size(self, *args):
        self.ids.toolbar.ids.label_title.font_size = "14sp"

    def on_pre_enter(self, *args):

        # Definitely not an optimal way to reference my MDList
        # but is the only thing that's worked so far (nested children)
        # Did not need to access my second screen('itinerary') or ScreenManager
        md_list = self.manager.current_screen.ids.container  # Access all ids from my current screen

        for i in range(1, 25):
            line_item = TwoLineIconListItem(text=f"[size=18]{i} Country Place dr[/size]",
                                            secondary_text=f"[size=14]Deliver 1 package[/size]",
                                            on_release=self.change_screen
                                            )

            icon = IconLeftWidget(icon="map-marker-outline")
            md_list.add_widget(line_item)

            line_item.add_widget(icon)

    def change_screen(self, ins):
        self.manager.current = "in_stop_interface"


class InStopInterface(Screen):
    pass


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
        sm = ScreenManager(transition=FadeTransition(duration=0.1))

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

    def on_inf_icon(self):
        self.is_expanded = not self.is_expanded

        card_layout = self.root.ids.card
        canvas = self.root.ids.box_canvas

        if card_layout.md_bg_color[-1] == 0:
            card_layout.md_bg_color[-1] = 1
            canvas.color_scrim = (0, 0, 0, 0.25)

        else:
            card_layout.md_bg_color[-1] = 0
            canvas.color_scrim = (0, 0, 0, 0)

        if self.is_expanded:
            item = Box()

            # initialze Label with 0 height and font_size
            inside_layout = MDFloatLayout()
            header = Label(text="About stops and locations", bold=True, color=(0, 0, 0, 1),
                           font_size=0, size_hint=(1, None), pos_hint={"center_y": 1, "center_x": 0.35})
            x_icon = MDIconButton(icon='close', pos_hint={"center_y": 1, "center_x": 0.95}, size_hint=(1, None),
                                  _no_ripple_effect=True, on_press=self.close_card)

            inside_layout.add_widget(x_icon)
            inside_layout.add_widget(header)

            l = Label(text="Stops are where you park your vehicle.\nLocations are where you deliver packages.\n\n"
                           "The number may change if you're unable to\n"
                           "deliver to certain locations, such as a locker, and\n"
                           "need to deliver somewhere else, such as customer\n"
                           "doorsteps. This has already been factored into\n"
                           "your route time.",
                      color=(0, 0, 0, 1),
                      font_size=0,
                      size_hint=(1, None),
                      height=0)

            item.add_widget(inside_layout)
            item.add_widget(l)
            card_layout.add_widget(item)

            self.animate_labels(l, header)


        else:
            card_layout.remove_widget(card_layout.children[0])

    def animate_labels(self, l, h):

        duration = 0.02
        height = 210

        anim_header = Animation(height=height, font_size=20, duration=duration)
        anim_header.start(h)

        anim_label = Animation(height=height, font_size=16, duration=duration)  # animate height and font_size
        anim_label.start(l)  # start animations

    def close_card(self, ins):

        card_layout = self.root.ids.card
        self.is_expanded = False

        if self.is_expanded == False:
            card_layout.remove_widget(card_layout.children[0])
            card_layout.md_bg_color[-1] = 0


if __name__ == "__main__":
    AmazonFlex().run()
