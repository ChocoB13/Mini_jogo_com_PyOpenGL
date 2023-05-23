from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial
from material.sprite import SpriteMaterial
from extras.text_texture import TextTexture
from core_ext.texture import Texture
from core_ext.mesh import Mesh

class Life():
    def __init__(self):
        self.vida = 0
        self.pont_geo = RectangleGeometry(width=120, height=80, position=[0, 600], alignment=[0,1])
        self.pont_mat = TextureMaterial(TextTexture(text=f"Vidas:",
                                    system_font_name="Times New Roman",
                                    font_size=40, font_color=[0, 0, 0],
                                    transparent=True,
                                    image_width=220, image_height=128,
                                    align_horizontal=0.5, align_vertical=0.1,
                                    image_border_width=1,
                                    image_border_color=[0, 0, 0]))
        self.vd_mesh = Mesh(self.pont_geo, self.pont_mat)
        sprite_geometry = RectangleGeometry(width=120, height=80, position=[0, 600], alignment=[0,1])
        sprite_material = SpriteMaterial(Texture("images/vidas.png"), {
            "billboard" : 1, 
            "tileCount" : [3, 3],
            "tileNumber" : 0
        })
        self.mesh = Mesh(sprite_geometry, sprite_material)

    
    def update(self):
        self.mesh.material.uniform_dict["tileNumber"].data = self.vida
            