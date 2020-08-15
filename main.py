from kivymd.app import MDApp
from backend.bot import BotApi
from kivy.uix.button import Button
from backend.login import LoginScreen
from kivy.lang import Builder

Builder.load_file('frontend/LoginScreen.kv')

class telebot(MDApp):
    def build(self):
        return LoginScreen()

    # def press(self,widget):
    #     widget.text = 'is run'
    #     BotApi().run()

telebot().run()
