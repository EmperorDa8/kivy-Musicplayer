import kivy
from kivy.uix import widget
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation

Window.size = (320, 600)


class MusicScreen(Screen):
    pass


class SongCover(MDBoxLayout):
    angle = NumericProperty()
    anim = Animation(angle=360, d=4, t="linear")
    anim += Animation(angle=0, d=0, t="linear")
    sprogress = Animation(value=80, d=100, t="linear")
    anim.repeat = True

    def rotate(self, anin=None):
        
        if self.anim.have_properties_to_animate(self):
            self.anim.stop(self)
            self.sprogress.stop(self)
        else:
            self.anim.start(self)

    def play(self,widget):
        self.sprogress.start(widget)
        self.sprogress.stop(self)
        self.rotate()


class MusicApp(MDApp):
    def build(self):
        return MusicScreen()


MusicApp().run()
