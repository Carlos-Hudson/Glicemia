from kivymd.uix.screen import MDScreen
from database.db import add_glucose


class AddScreen(MDScreen):

    def save_value(self):

        value = self.ids.glucose_field.text

        if value != "":
            add_glucose(value)

            self.ids.glucose_field.text = ""

            self.manager.current = "home"