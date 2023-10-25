from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window


class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source='cloud.png').texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

    pass

class MyGameApp(App):
    pass


MyGameApp().run()