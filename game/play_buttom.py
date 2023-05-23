from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial
from extras.text_texture import TextTexture
from core_ext.mesh import Mesh

class Button():
    def __init__(self):
        self.x_pos = 400
        self.y_pos = 300
        but_geo = RectangleGeometry(width=100, height=100, position=[self.x_pos, self.y_pos], alignment=[0.5, 0.5])
        but_mat = TextureMaterial(TextTexture(text="Play",
                                    system_font_name="Arial",
                                    font_size=50, font_color=[255, 255, 255],
                                    background_color=[200, 200, 200], transparent=False,
                                    image_width=150, image_height=150,
                                    align_horizontal=0.5, align_vertical=0.5,
                                    image_border_width=4,
                                    image_border_color=[255, 255, 255]))
        self.mesh = Mesh(but_geo, but_mat)