from geometry.myobj import MyObject
from material.texture import TextureMaterial
from core_ext.texture import Texture
from core_ext.mesh import Mesh
from material.phong import PhongMaterial
from material.flat import FlatMaterial
from math import pi


class Objects:
    def __init__(self, mat_file, obj_file=None, geometry=None):
        if geometry is not None:
            obj = geometry
        else:
            obj = MyObject(obj_file)
        mat = PhongMaterial(Texture(mat_file))
        self.mesh = Mesh(obj, mat)

    
    def update(self, input_object):
        # Initialize key state dictionary
        key_state = {
            'k': False,
            'j': False,
            'i': False,
            'l': False,
        }

        for key in input_object.key_down_list:
            if key == 'k' and self.mesh.global_position[2] < 4:
                new_position = [self.mesh.global_position[0], 0, self.mesh.global_position[2] + 4]
                self.mesh.set_position(new_position)
                key_state['k'] = True

            elif key == 'j' and self.mesh.global_position[0] > -4:
                new_position = [self.mesh.global_position[0] - 4, 0, self.mesh.global_position[2]]
                self.mesh.set_position(new_position)
                key_state['j'] = True

            elif key == 'i' and self.mesh.global_position[2] > -4:
                new_position = [self.mesh.global_position[0], 0, self.mesh.global_position[2] - 4]
                self.mesh.set_position(new_position)
                key_state['i'] = True

            elif key == 'l' and self.mesh.global_position[0] < 4:
                new_position = [self.mesh.global_position[0] + 4, 0, self.mesh.global_position[2]]
                self.mesh.set_position(new_position)
                key_state['l'] = True

        for key in input_object.key_up_list:
            if key == 'k':
                key_state['k'] = False

            elif key == 'j':
                key_state['j'] = False

            elif key == 'i':
                key_state['i'] = False

            elif key == 'l':
                key_state['l'] = False
