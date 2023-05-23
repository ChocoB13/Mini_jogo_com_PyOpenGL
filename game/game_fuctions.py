from game.foods import Food
from game.ovo import Ovo
from game.meat import Meat
from game.rolo import RoloMassa
from game.colher import Colher
from random import choice
from math import dist

from light.point import PointLight


def creat_foods(foods, stats, gm_settings):
    if stats.food_number < 16:
        food = Food(choice([Ovo(), Meat()]), gm_settings)
        food.mesh.add(PointLight(color=[0.5, 0.5, 0.5], position=[0, 0, 0], attenuation=[0, 0.1, 0.1]))
        foods.add(food.mesh)
        stats.food_number += 1


def creat_objects(objects, stats, gm_settings):
    if stats.object_number < 10:
        object = Food(choice([RoloMassa(), Colher()]), gm_settings)
        objects.add(object.mesh)
        stats.object_number += 1

def check_colisions_foods(foods, p_obj, pontuation):
    for food in foods.children_list:
        distn = dist([p_obj.global_position[0], p_obj.global_position[-1]], [food.global_position[0], food.global_position[-1]])
        if distn < 0.5 and food.global_position[1] < p_obj.global_position[1]:
            foods.remove(food)
            pontuation.ponto += 1


def remove_olds(foods, objects, stats, life):
    for food in foods.children_list:
        if food.global_position[1] < -3:
            foods.remove(food)
            life_loss(foods, objects, stats, life)
            break
    for object in objects.children_list:
        if object.global_position[1] < -3:
            objects.remove(object)


def life_loss(foods, objects, stats, life):
    if stats.vidas_left > 0:
        stats.vidas_left -= 1
        life.vida += 1
        foods.empty()
        objects.empty()
        foods.set_position([0, 15, 0])
        objects.set_position([0, 15, 0])
        stats.food_number = 0
        stats.object_number = 0
    else:
        foods.empty()
        objects.empty()
        foods.set_position([0, 15, 0])
        objects.set_position([0, 15, 0])
        stats.game_ative = False


def check_colisions_objects(foods, objects, p_obj, stats, life):
    for object in objects.children_list:
        distn = dist([p_obj.global_position[0], p_obj.global_position[-1]], [object.global_position[0], object.global_position[-1]])
        if distn < 0.5 and object.global_position[1] < p_obj.global_position[1]:
            objects.remove(object)
            life_loss(foods, objects, stats, life)


def check_play_button(input_object, play_button, stats, pontuation, life):
    if len(input_object._mouse_position) > 0:
        mpx = input_object._mouse_position[0]
        mpy = (input_object._mouse_position[1] - 600) * (-1)
        distn = dist([mpx, mpy], [play_button.x_pos, play_button.y_pos])
        if distn < 46.0:
            stats.game_ative = True
            stats.reset_stats()
            pontuation.ponto = 0
            life.vida = 0
