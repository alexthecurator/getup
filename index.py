from kivy.lang import Builder
from kivy.properties import StringProperty
from kaki.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import Label
from kivymd.uix.textfield import TextInput
from kivymd.uix.button import Button

#Screen size
from kivy.core.window import Window
Window.size = (600, 900)
#Initializing Screens
sm = ScreenManager()

# including screens
from src import splash

class Getup(App):        
    #Build screens
    def build(self):
        sm.add_widget(Splashscreen(name='splash'))
        # sm.add_widget(MainScreen(name='main'))
        # sm.add_widget(LoginScreen(name='login'))
        # sm.add_widget(Signup(name='signup'))
        # sm.add_widget(HomeScreen(name='home'))

        sm.current = 'main'
        
        return sm

##executing
Getup = Getup()
Getup.run()