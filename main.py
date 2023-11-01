from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window


from ground import Ground

class Background(Widget):
    cloud_texture = ObjectProperty(None)
    ground_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source='cloud.png').texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.ground_texture = Image(source ="floating_ground.png").texture
        self.ground_texture.wrap = 'repeat'
        self.ground_texture.uvsize = (Window.width / self.ground_texture.width, -1)
    def scroll_textures(self, time_passed):
        self.cloud_texture.uvpos = ( (self.cloud_texture.uvpos[0] - time_passed/2.0)%Window.width,self.cloud_texture.uvpos[1])
        self.ground_texture.uvpos = ( (self.ground_texture.uvpos[0] - time_passed) % Window.width, self.ground_texture.uvpos[1])

        texture = self.property('cloud_texture')
        texture.dispatch(self)

        texture = self.property('ground_texture')
        texture.dispatch(self)

    pass

from kivy.clock import Clock
class MyGameApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/100.)
    pass


MyGameApp().run()
