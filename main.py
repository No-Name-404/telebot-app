from kivymd.app import MDApp
from bidi.algorithm import get_display
import arabic_reshaper
from app.libs import *

from kivy.base import ExceptionHandler, ExceptionManager

class E(ExceptionHandler):
    def handle_exception(self, inst):
        return ExceptionManager.PASS

class telebot(MDApp):
    def __init__(self,*args, **kwargs):
        super(telebot,self).__init__(*args, **kwargs)
        ExceptionManager.add_handler(E())
        self.font = 'app/fonts/Ubuntu-Kurdish-Kurdfont.ttf'
        self.database = database('app-data')
        self.set_language = database('app-data').read()['settings']['language']
        self.language = database('app-data').read()['language'][self.set_language]

    def ar(self,text):
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(MenuScreen(name='menu'))
        return self.sm

if __name__ == '__main__':
    telebot().run()
