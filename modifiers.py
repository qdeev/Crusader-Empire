import pygame.key

from CONSTANTS import *


class Modifier:

    def __init__(self, target_type: str, action: ActionType, arg: int):
        self.target_type = target_type
        self.action = action
        self.arg = arg


class Ability:

    def __init__(self, bind_key, action):
        self.bind_key = bind_key
        self.action = action

    def cast(self):
        pass
