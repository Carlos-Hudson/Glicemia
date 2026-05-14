from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from screens.home import HomeScreen
from screens.add import AddScreen
from screens.settings import SettingsScreen

from utils.theme import setup_theme
import os
from database.db import connect
from screens.gerador_path import GeradorPath
from kivymd.toast import toast

class MainApp(MDApp):

    def on_start(self):

        if not os.path.exists("database"):
            os.makedirs("database")

        connect()
        print("Banco de dados criado")

    def salva_relatorio(self):
        exportador = GeradorPath()
        resultado = exportador.exportar()
        toast(resultado)


    def build(self):

        setup_theme(self)

        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/add.kv")
        Builder.load_file("kv/settings.kv")

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(AddScreen(name="add"))
        sm.add_widget(SettingsScreen(name="settings"))

        return sm

if __name__ == "__main__":
    MainApp().run()