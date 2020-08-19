from kivymd.app import MDApp
from app.backend.bot import BotApi
from app.libs import *

class telebot(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(LoginScreen(name='login'))
        return self.sm

telebot().run()
