# credits: Margarida Moura, CGr 2022
#
"""Read vertices from OBJ file"""
from typing import List
def my_obj_reader(filename :str) -> List:
	"""Get the vertices from the file"""
	position_list = list()
	texture_list = list()
	normal_list = list()
	vertices = list()
	textures = list()
	normal = list()

	with open(filename, 'r') as in_file:
		lines = in_file.readline()
		while lines:
			line = lines.strip().split()
			if line[0] == 'v':
				point = [float(value) for value in line[1:]]
				vertices.append(point)
			elif line[0] == 'vt':
				point = [float(value) for value in line[1:]]
				textures.append(point)
			elif line[0] == 'vn':
				point = [float(value) for value in line[1:]]
				normal.append(point)
			elif line[0] == 'f':
				face_description = []
				text_description = []
				norm_description = []
				for v in line[1:4]:
					w = v.split('/')
					face_description.append(int(w[0]) - 1)
					text_description.append(int(w[1]) - 1)
					norm_description.append(int(w[2]) - 1)
				for elem in face_description:
					position_list.append(vertices[elem])
				for elem in text_description:
					texture_list.append(textures[elem])
				for elem in norm_description:
					normal_list.append(normal[elem])
			lines = in_file.readline()
	return position_list, texture_list, normal_list

if __name__ == '__main__':
	f_in = input("File? ")
	result = my_obj_reader(f_in)
	print(result)