from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import ModalView
from kivymd.uix.floatlayout import MDFloatLayout
import os

for file in os.listdir('app/frontend'):
    Builder.load_file('app/frontend/'+file)

from app.backend.login import LoginScreen
from app.backend.menu import MenuScreen
