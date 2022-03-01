#!/usr/bin/python3
#coding: utf-8

###### KIVY MODULE IMPORT ######
from kivy.app import App 
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

##### FUNCTION MODULE IMPORT ######
import string
import random

# On définit la taille de la fenêtre
Window.size = (310, 520)

class PasswordGenPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.list_chars = string.ascii_letters + string.digits + string.punctuation
        self.password_generate = "Default Password"
        print(type(self.list_chars))

    def Generator(self, nbr, password_field):
        passwd = ""
        for i in range(int(nbr.value)):
            number = random.randint(0, len(self.list_chars)-1)
            passwd += self.list_chars[number]
        
        password_field.text = passwd

    def show(self, number_chars, label_chars):
        label_chars.text = str(int(number_chars.value))
        

# La classe principale
class PasswordGenApp(App):
    def build(self):
        return Builder.load_file('main.kv')


PasswordGenApp().run()