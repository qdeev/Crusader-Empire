from CONSTANTS import *


class Modifier:

    def __init__(self, target_type: str, action: ActionType, arg: int):
        self.target_type = target_type
        self.action = action
        self.arg = arg


class Ability:

    def __init__(self, bind_key, action_type: ActionType):
        self.bind_key = bind_key
        self.action_type = action_type

    def cast(self, target, args: Dict):
        if self.action_type == ActionType.NULL:
            pass
        elif self.action_type == ActionType.MOVE:
            target.move(args["args"])
        elif self.action_type == ActionType.RALLYPOINT:
            target.set_rallypoint(args["args"])
        elif self.action_type == ActionType.CREATE_WORKER:
            target.create_task_worker()
        elif self.action_type == ActionType.CREATE_SPEARMAN:
            target.create_task_spearman()
        elif self.action_type == ActionType.CREATE_SWORDSMAN:
            target.create_task_swordsman()
        elif self.action_type == ActionType.CREATE_FORTRESS:
            target.create_task_fortress(args["args"])
        elif self.action_type == ActionType.CREATE_BARACK:
            target.create_task_barack(args["args"])
        elif self.action_type == ActionType.CREATE_SUPPLY:
            target.create_task_supply(args["args"])


class AbilityHandler:

    def __init__(self, unit, abilities: List[Ability]):
        self.unit = unit
        self.abilities = abilities

    def get_ability(self, key):
        for ability in self.abilities:
            if ability.bind_key == key:
                return ability
        return NULL_ABILITY

    def cast_ability(self, key, args: Dict):
        self.get_ability(key).cast(self.unit, args)


"""naming the abilities"""
NULL_ABILITY = Ability(pygame.K_ESCAPE, ActionType.NULL)
MOVE_ABILITY = Ability(pygame.BUTTON_RIGHT, ActionType.MOVE)
RALLYPOINT_ABILITY = Ability(pygame.BUTTON_RIGHT, ActionType.RALLYPOINT)
CREATE_WORKER_ABILITY = Ability(pygame.K_w, ActionType.CREATE_WORKER)
CREATE_SWORDSMAN_ABILITY = Ability(pygame.K_s, ActionType.CREATE_SWORDSMAN)
CREATE_SPEARMAN_ABILITY = Ability(pygame.K_d, ActionType.CREATE_SPEARMAN)
CREATE_FORTRESS_ABILITY = Ability(pygame.K_f, ActionType.CREATE_FORTRESS)
CREATE_BARACK_ABILITY = Ability(pygame.K_b, ActionType.CREATE_BARACK)
CREATE_SUPPLY_ABILITY = Ability(pygame.K_v, ActionType.CREATE_SUPPLY)
