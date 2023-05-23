from core_ext.mesh import Mesh
from geometry.myobj import MyObject
from material.phong import PhongMaterial
from core_ext.texture import Texture


class Ovo(Mesh):
    def __init__(self):
        geometry = MyObject('obj_files/ovo.obj')
        material = PhongMaterial(Texture('texture/ovo.jpg'))
        # Initialize the mesh
        super().__init__(geometry, material)
