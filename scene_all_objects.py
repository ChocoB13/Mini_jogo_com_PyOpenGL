import math
import pathlib
import sys
from pygame import mouse

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[2])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.sphere import SphereGeometry
from extras.movement_rig import MovementRig
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from light.ambient import AmbientLight
from light.directional import DirectionalLight
from game.settings import Settings
from core_ext.group import Group
from game.objetos import Objects
import game.game_fuctions as gf
from game.trophs import Trophs
from game.game_stats import GameStats
from game.play_buttom import Button
from game.lifes import Life
from extras.grid import GridHelper
from material.lambert import LambertMaterial
from material.phong import PhongMaterial


class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add box movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([-0.42, 20, 5.95])
        self.camera.rotate_x(-45)
        self.gm_settings = Settings()


        ambient = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient)
        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 10, 8])
        self.scene.add(self.rig)

        self.pan = Objects('texture/metal_preto.jpg', 'obj_files/fryingPan1.obj')
        self.pan.mesh.set_position([0, 0, 0])
        self.pan.mesh.rotate_y(89.5)
        self.pan.mesh.scale(1.5)
        self.scene.add(self.pan.mesh)

        sky_geometry = SphereGeometry(radius=50)
        sky_material = LambertMaterial(
            texture=Texture(file_name="texture/stars.png"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)

        floor_geometry = RectangleGeometry(width=15, height=15)
        floor_material = PhongMaterial(
            texture=Texture(file_name="texture/floor.jpg"))
        floor = Mesh(floor_geometry, floor_material)
        floor.rotate_x(-math.pi / 2)
        floor.set_position([0, -1, 0])
        self.scene.add(floor)

        grid = GridHelper(
            size=15,
            divisions=3,
            grid_color=[1, 1, 1],
            center_color=[1, 1, 0]
        )
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)


        self.foods = Group()
        self.foods.set_position([0, 20, 0])
        self.objects = Group()
        self.objects.set_position([0, 20, 0])
        self.scene.add(self.foods)
        self.scene.add(self.objects)

        # Add the Heads Up Display (HUD) layer
        self.hud_scene = Scene()
        self.hud_camera = Camera()
        self.hud_camera.set_orthographic(0, 800, 0, 600, 1, -1)

        self.pontuation = Trophs()
        self.hud_scene.add(self.pontuation.pt_mesh)
        self.hud_scene.add(self.pontuation.mesh)
        
        self.life = Life()
        self.hud_scene.add(self.life.vd_mesh)
        self.hud_scene.add(self.life.mesh)

        self.stats = GameStats(self.gm_settings)
        self.play = Button()
        self.hud_scene.add(self.play.mesh)


    def update(self):
        if self.stats.game_ative:
            gf.creat_foods(self.foods, self.stats, self.gm_settings)
            gf.creat_objects(self.objects, self.stats, self.gm_settings)
            self.foods.translate(0, -self.gm_settings.food_speed_factor, 0)
            self.objects.translate(0, -self.gm_settings.object_speed_factor, 0)
            self.pan.update(self.input)
            gf.check_colisions_foods(self.foods, self.pan.mesh, self.pontuation)
            gf.check_colisions_objects(self.foods, self.objects, self.pan.mesh, self.stats, self.life)
            gf.remove_olds(self.foods, self.objects, self.stats, self.life)
            self.pontuation.update()
            self.life.update()
            self.rig.update(self.input, self.delta_time)
            self.play.mesh._visible = False
            mouse.set_visible(False)
        else:
            self.play.mesh._visible = True
            mouse.set_visible(True)
            gf.check_play_button(self.input, self.play, self.stats, self.pontuation, self.life)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hud_scene, self.hud_camera, clear_color=False)
        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
