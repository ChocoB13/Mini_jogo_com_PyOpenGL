from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class MyObject(Geometry):
    def __init__(self, obj_file):
        super().__init__()
        # Each side consists of two triangles
        position_data, uv_data, normal_data = my_obj_reader(obj_file)
        color_data = [1.0, 0.0, 0.0]
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
        self.add_attribute("vec3", "vertexNormal", normal_data)
        self.add_attribute("vec3", "faceNormal", normal_data)
