from random import choice, randrange


class Food:
    def __init__(self, mesh, gm_settings):
        super().__init__()
        self.gm_settings = gm_settings
        self.mesh = mesh

        positions = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 0), (0, 1),
                     (1, -1), (1, 0), (1, 1)]
        selected_position = choice(positions)

        spacing = 4  # Spacing between grid positions
        x = selected_position[0] * spacing
        z = selected_position[1] * spacing

        self.mesh.set_position([x, randrange(10, 150, 1), z])
        self.mesh.scale(0.5)


    def update(self):
        """move alimento pra baixo"""
        self.mesh.translate(0, -self.gm_settings.food_speed_factor, 0)