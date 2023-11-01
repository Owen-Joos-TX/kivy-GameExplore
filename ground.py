from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image

class Ground(Widget):
    GROUND_SIZE = NumericProperty(45)
    ground_center_mass = NumericProperty(0)


    #texture
    ground_body_texture = ObjectProperty(None)
    lower_ground_tex_coords = ListProperty((0,0,1,0,1,1,0,1))
    top_ground_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ground_body_texture = Image(source="floating_ground.png").texture
        self.ground_body_texture.wrap = 'repeat'
