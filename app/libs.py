from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import ModalView
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    CircularElevationBehavior,
)
import os

from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.lang import Builder
from kivymd.toast import toast

for file in os.listdir('app/frontend'):
    Builder.load_file('app/frontend/'+file)

from app.backend.db import database
from app.backend.login import LoginScreen
from app.backend.menu import MenuScreen
