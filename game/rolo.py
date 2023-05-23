from core_ext.mesh import Mesh
from geometry.myobj import MyObject
from material.phong import PhongMaterial
from core_ext.texture import Texture


class RoloMassa(Mesh):
    def __init__(self):
        geometry = MyObject('obj_files/rolomassa.obj')
        material = PhongMaterial(Texture('texture/plywood_diff_4k.jpg'))
        # Initialize the mesh
        super().__init__(geometry, material)
