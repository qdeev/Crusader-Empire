from enum import Enum
import sys
from typing import *
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Disables the pygame welcome message
import pygame

pygame.init()
pygame.display.set_caption('Crusader Empire')


class Race(Enum):
    CRUSADER = 0
    ARAB = 1


class ActionType(Enum):
    ATTACK = 0
    ATTACKED = 1


UNIT_STATS = {"crusader": {"worker": {"damage": 0,
                                      "hp": 10,
                                      "armor": 0,
                                      "attack_range": 0,
                                      "attack_speed": 0,
                                      "move_speed": 0},

                           "militia": {"damage": 5,
                                       "hp": 15,
                                       "armor": 2,
                                       "attack_range": 30,
                                       "attack_speed": 1,
                                       "move_speed": 3},

                           "spearman": {"damage": 10,
                                        "hp": 60,
                                        "armor": 2,
                                        "attack_range": 30,
                                        "attack_speed": 1,
                                        "move_speed": 3},

                           "swordsman": {"damage": 10,
                                         "hp": 60,
                                         "armor": 2,
                                         "attack_range": 30,
                                         "attack_speed": 1,
                                         "move_speed": 3},

                           "archer": {"damage": 10,
                                      "hp": 60,
                                      "armor": 2,
                                      "attack_range": 30,
                                      "attack_speed": 1,
                                      "move_speed": 3},

                           "equestrian_brothers": {"damage": 10,
                                                   "hp": 60,
                                                   "armor": 2,
                                                   "attack_range": 30,
                                                   "attack_speed": 1,
                                                   "move_speed": 3},

                           "order_knights": {"damage": 10,
                                             "hp": 60,
                                             "armor": 2,
                                             "attack_range": 30,
                                             "attack_speed": 1,
                                             "move_speed": 3},

                           "hospitallers": {"damage": 10,
                                            "hp": 60,
                                            "armor": 2,
                                            "attack_range": 30,
                                            "attack_speed": 1,
                                            "move_speed": 3},

                           "ram": {"damage": 10,
                                   "hp": 60,
                                   "armor": 2,
                                   "attack_range": 30,
                                   "attack_speed": 1,
                                   "move_speed": 3},

                           "catapult": {"damage": 10,
                                        "hp": 60,
                                        "armor": 2,
                                        "attack_range": 30,
                                        "attack_speed": 1,
                                        "move_speed": 3},

                           "general": {"damage": 10,
                                       "hp": 60,
                                       "armor": 2,
                                       "attack_range": 30,
                                       "attack_speed": 1,
                                       "move_speed": 3}
                           },

              "arabs": {"worker": {"damage": 0,
                                   "hp": 10,
                                   "armor": 0,
                                   "attack_range": 0,
                                   "attack_speed": 0,
                                   "move_speed": 0},

                        "desert tribal warriors": {"damage": 5,
                                                   "hp": 15,
                                                   "armor": 2,
                                                   "attack_range": 30,
                                                   "attack_speed": 1,
                                                   "move_speed": 3},

                        "spearman": {"damage": 10,
                                     "hp": 60,
                                     "armor": 2,
                                     "attack_range": 30,
                                     "attack_speed": 1,
                                     "move_speed": 3},

                        "swordsman": {"damage": 10,
                                      "hp": 60,
                                      "armor": 2,
                                      "attack_range": 30,
                                      "attack_speed": 1,
                                      "move_speed": 3},

                        "archer": {"damage": 10,
                                   "hp": 60,
                                   "armor": 2,
                                   "attack_range": 30,
                                   "attack_speed": 1,
                                   "move_speed": 3},

                        "equestrian_brothers": {"damage": 10,
                                                "hp": 60,
                                                "armor": 2,
                                                "attack_range": 30,
                                                "attack_speed": 1,
                                                "move_speed": 3},

                        "order_knights": {"damage": 10,
                                          "hp": 60,
                                          "armor": 2,
                                          "attack_range": 30,
                                          "attack_speed": 1,
                                          "move_speed": 3},

                        "hospitallers": {"damage": 10,
                                         "hp": 60,
                                         "armor": 2,
                                         "attack_range": 30,
                                         "attack_speed": 1,
                                         "move_speed": 3},

                        "ram": {"damage": 10,
                                "hp": 60,
                                "armor": 2,
                                "attack_range": 30,
                                "attack_speed": 1,
                                "move_speed": 3},

                        "catapult": {"damage": 10,
                                     "hp": 60,
                                     "armor": 2,
                                     "attack_range": 30,
                                     "attack_speed": 1,
                                     "move_speed": 3},

                        "general": {"damage": 10,
                                    "hp": 60,
                                    "armor": 2,
                                    "attack_range": 30,
                                    "attack_speed": 1,
                                    "move_speed": 3}
                        }
              }

BUILDING_STATS = {"crusader": {"fortress": {"hp": 2000,
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

                               "stables": {"hp": 800,
                                           "armor": 0},

                               "arsenal": {"hp": 800,
                                           "armor": 0},
                               },

                  "arab": {"palace": {"hp": 2000,
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

FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 820
BLACK = pygame.Color("black")
