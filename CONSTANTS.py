import random
from enum import Enum, IntEnum
import sys
from typing import *
import os
import math
from dataclasses import dataclass
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG,
                    filename="log.txt", filemode='a')

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Disables the pygame welcome message
import pygame

pygame.init()


class Race(Enum):
    CRUSADER = 0
    ARAB = 1


class ActionType(Enum):
    NULL = -1
    ATTACK = 0
    ATTACKED = 1
    MOVE = 2
    RALLYPOINT = 3
    CREATE_WORKER = 4
    CREATE_SWORDSMAN = 5
    CREATE_SPEARMAN = 6
    CREATE_FORTRESS = 7
    CREATE_BARACK = 8
    CREATE_SUPPLY = 9


UNIT_STATS = {"crusader": {"worker": {"damage": 0,
                                      "hp": 10,
                                      "armor": 0,
                                      "attack_range": 0,
                                      "attack_speed": 0,
                                      "move_speed": 2,
                                      "food_cost": 1},

                           "militia": {"damage": 5,
                                       "hp": 15,
                                       "armor": 2,
                                       "attack_range": 15,
                                       "attack_speed": 1,
                                       "move_speed": 3,
                                       "food_cost": 1},

                           "spearman": {"damage": 10,
                                        "hp": 15,
                                        "armor": 2,
                                        "attack_range": 30,
                                        "attack_speed": 1,
                                        "move_speed": 2,
                                        "food_cost": 2},

                           "swordsman": {"damage": 10,
                                         "hp": 60,
                                         "armor": 2,
                                         "attack_range": 30,
                                         "attack_speed": 1,
                                         "move_speed": 2,
                                         "food_cost": 3},

                           "archer": {"damage": 10,
                                      "hp": 60,
                                      "armor": 2,
                                      "attack_range": 30,
                                      "attack_speed": 1,
                                      "move_speed": 3,
                                      "food_cost": 1},

                           "equestrian_brothers": {"damage": 10,
                                                   "hp": 60,
                                                   "armor": 2,
                                                   "attack_range": 30,
                                                   "attack_speed": 1,
                                                   "move_speed": 3,
                                                   "food_cost": 1},

                           "order_knights": {"damage": 10,
                                             "hp": 60,
                                             "armor": 2,
                                             "attack_range": 30,
                                             "attack_speed": 1,
                                             "move_speed": 3,
                                             "food_cost": 1},

                           "hospitallers": {"damage": 10,
                                            "hp": 60,
                                            "armor": 2,
                                            "attack_range": 30,
                                            "attack_speed": 1,
                                            "move_speed": 3,
                                            "food_cost": 1},

                           "ram": {"damage": 10,
                                   "hp": 60,
                                   "armor": 2,
                                   "attack_range": 30,
                                   "attack_speed": 1,
                                   "move_speed": 3,
                                   "food_cost": 1},

                           "catapult": {"damage": 10,
                                        "hp": 60,
                                        "armor": 2,
                                        "attack_range": 30,
                                        "attack_speed": 1,
                                        "move_speed": 3,
                                        "food_cost": 1},

                           "general": {"damage": 10,
                                       "hp": 60,
                                       "armor": 2,
                                       "attack_range": 30,
                                       "attack_speed": 1,
                                       "move_speed": 3,
                                       "food_cost": 1}
                           },

              "arab": {"worker": {"damage": 0,
                                  "hp": 10,
                                  "armor": 0,
                                  "attack_range": 0,
                                  "attack_speed": 0,
                                  "move_speed": 0,
                                  "food_cost": 1},

                       "desert_tribal_warrior": {"damage": 5,
                                                 "hp": 15,
                                                 "armor": 2,
                                                 "attack_range": 30,
                                                 "attack_speed": 1,
                                                 "move_speed": 3,
                                                 "food_cost": 1},

                       "spearman": {"damage": 10,
                                    "hp": 60,
                                    "armor": 2,
                                    "attack_range": 30,
                                    "attack_speed": 1,
                                    "move_speed": 2,
                                    "food_cost": 1},

                       "swordsman": {"damage": 10,
                                     "hp": 60,
                                     "armor": 2,
                                     "attack_range": 30,
                                     "attack_speed": 1,
                                     "move_speed": 2,
                                     "food_cost": 1},

                       "archer": {"damage": 10,
                                  "hp": 60,
                                  "armor": 2,
                                  "attack_range": 30,
                                  "attack_speed": 1,
                                  "move_speed": 3,
                                  "food_cost": 1},

                       "horse_archers": {"damage": 10,
                                         "hp": 60,
                                         "armor": 2,
                                         "attack_range": 30,
                                         "attack_speed": 1,
                                         "move_speed": 3,
                                         "food_cost": 1},

                       "camel_riders": {"damage": 10,
                                        "hp": 60,
                                        "armor": 2,
                                        "attack_range": 30,
                                        "attack_speed": 1,
                                        "move_speed": 3,
                                        "food_cost": 1},

                       "elephants": {"damage": 10,
                                     "hp": 60,
                                     "armor": 2,
                                     "attack_range": 30,
                                     "attack_speed": 1,
                                     "move_speed": 3,
                                     "food_cost": 1},

                       "throwers": {"damage": 10,
                                    "hp": 60,
                                    "armor": 2,
                                    "attack_range": 30,
                                    "attack_speed": 1,
                                    "move_speed": 3,
                                    "food_cost": 1},

                       "assassin": {"damage": 10,
                                    "hp": 60,
                                    "armor": 2,
                                    "attack_range": 30,
                                    "attack_speed": 1,
                                    "move_speed": 3,
                                    "food_cost": 1}
                       }
              }

BUILDING_STATS = {"crusader": {"fortress": {"hp": 100,
                                            "armor": 1},

                               "barack": {"hp": 1000,
                                          "armor": 0},

                               "tower": {"damage": 20,
                                         "hp": 700,
                                         "armor": 0,
                                         "attack_range": 30,
                                         "attack_speed": 1},

                               "mine": {"hp": 300,
                                        "armor": 0},

                               "tree": {"hp": 300,
                                        "armor": 0},

                               "supply": {"hp": 400,
                                          "armor": 0},

                               "workshop": {"hp": 900,
                                            "armor": 0},

                               "stables": {"hp": 800,
                                           "armor": 0},

                               "arsenal": {"hp": 800,
                                           "armor": 0},
                               },

                  "arab": {"palace": {"hp": 100,
                                      "armor": 1},

                           "barack": {"hp": 1000,
                                      "armor": 0},

                           "tower": {"damage": 20,
                                     "hp": 700,
                                     "armor": 0,
                                     "attack_range": 30,
                                     "attack_speed": 1},

                           "mine": {"hp": 300,
                                    "armor": 0},

                           "supply": {"hp": 400,
                                      "armor": 0},

                           "workshop": {"hp": 900,
                                        "armor": 0},

                           "stalls": {"hp": 800,
                                      "armor": 0},

                           "arsenal": {"hp": 800,
                                       "armor": 0},

                           }

                  }

DEBUG = False
FPS = 100
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1024

BLACK = pygame.Color("black")

screen = pygame.display.set_mode(SCREEN_SIZE)


def load_image(name, folder="assets", colorkey=None):
    fullname = os.path.join(rf'data\{"demo_" if DEBUG else ""}{folder}\textures', name)
    if not os.path.isfile(fullname):
        raise FileNotFoundError(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


"""loading images"""
RALLYPOINTFLAG_IMAGE = load_image("Fireplace.png")

CRUSADER_WORKER_IMAGE = load_image("crusader_worker_full.xcf", colorkey="white")
CRUSADER_MILITIA_IMAGE = load_image("arab_militia_full.xcf", colorkey="white")
CRUSADER_SWORDSMAN_IMAGE = load_image("crusader_swordman_full.xcf", colorkey="white")
CRUSADER_SPEARMAN_IMAGE = load_image("crusader_spearman_full.xcf", colorkey="white")
CRUSADER_ARCHER_IMAGE = load_image("crusader_archer_full.xcf", colorkey="white")
CRUSADER_GENERAL_IMAGE = load_image("crusader_general_full.xcf", colorkey="white")
CRUSADER_EQUESTRIAN_BROTHERS_IMAGE = load_image("crusader_equestrian_brothers_full.xcf", colorkey="white")
CRUSADER_ORDER_KNIGHTS_IMAGE = load_image("crusader_order_knights.xcf", colorkey="white")
CRUSADER_HOSPITALLERS_IMAGE = load_image("crusader_hospitaller_full.xcf", colorkey="white")
CRUSADER_BATTERING_RAM = load_image("ram_full.xcf", colorkey="white")
CRUSADER_CATAPULT_IMAGE = load_image("catapult_full.xcf", colorkey="white")

ARAB_WORKER_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_SPEARMAN_IMAGE = load_image("arab_spearman_full.xcf", colorkey="white")
ARAB_SHOTEL_SWORDSMAN_IMAGE = load_image("arab_swordman_full.xcf", colorkey="white")
ARAB_ARCHER_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_HORSE_ARCHERS_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_CAMEL_RIDERS_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_ELEPHANTS_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_THROWERS_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_ASSASSIN_IMAGE = load_image("Tree.png", colorkey="white")

CRUSADER_FORTRESS_IMAGE = load_image("crusaders_castle_full.xcf", colorkey="white")
CRUSADER_FORTRESS_ANIMATION = [load_image("crusaders_castle/crusaders_castle_1.xcf", colorkey="white"),
                               load_image("crusaders_castle/crusaders_castle_2.xcf", colorkey="white")]
CRUSADER_FORTRESS_DICT = {"idle": CRUSADER_FORTRESS_ANIMATION}

CRUSADER_BARACK_IMAGE = load_image("barack_full.xcf", colorkey="white")
CRUSADER_TOWER_IMAGE = load_image("Tree.png", colorkey="white")

CRUSADER_MINE_IMAGE = load_image("mine/mine_1.xcf", colorkey="white")
CRUSADER_MINE_ANIMATION = [load_image("mine/mine_1.xcf", colorkey="white"),
                           load_image("mine/mine_2.xcf", colorkey="white"),
                           load_image("mine/mine_3.xcf", colorkey="white")]
CRUSADER_MINE_DICT = {"idle": CRUSADER_MINE_ANIMATION}

CRUSADER_TREE_IMAGE = load_image("Tree.png", colorkey="black")
CRUSADER_SUPPLY_IMAGE = load_image("ambar_full.xcf", colorkey="white")
CRUSADER_WORKSHOP_IMAGE = load_image("Tree.png", colorkey="white")
CRUSADER_STABLES_IMAGE = load_image("Tree.png", colorkey="white")
CRUSADER_ARSENAL_IMAGE = load_image("Tree.png", colorkey="white")

ARAB_PALACE_IMAGE = load_image("arabs_castle_full.xcf", colorkey="white")
ARAB_BARACK_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_TOWER_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_MINE_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_SUPPLY_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_WORKSHOP_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_STALLS_IMAGE = load_image("Tree.png", colorkey="white")
ARAB_ARSENAL_IMAGE = load_image("Tree.png", colorkey="white")

MAP_IMAGE = load_image("Map_Level_1.png")
