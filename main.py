import os

from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window

Window.size = (411,731)

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "src/screenmanager.kv"),
        os.path.join(os.getcwd(), "src/screens/splashscreen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "src.screenmanager",
        "SplashScreen": "src.screens.splashscreen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):

        return Factory.MainScreenManager()




# finally, run the app
if __name__ == "__main__":
    LiveApp().run()