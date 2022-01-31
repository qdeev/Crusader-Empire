from CONSTANTS import *
from modifiers import *
from game_features import TaskManager


class Building:

    def __init__(self, game, hp, armor, abilities: List[Ability], modifiers: List[Modifier], race: Race):
        self.game = game
        self.hp = hp
        self.max_hp = hp
        self.armor = armor
        self.abilities = AbilityHandler(self, abilities + [NULL_ABILITY])
        self.task_manager = TaskManager(self)
        self.modifiers = [Modifier("SIEGE", ActionType.ATTACKED, 100)] + modifiers
        self.race = race


class CrusaderBuilding(Building):
    RACE = Race.CRUSADER

    def __init__(self, game, hp, armor, abilities: List[Ability], modifiers: List[Modifier]):
        super().__init__(game, hp, armor, abilities, modifiers, CrusaderBuilding.RACE)


class CrusaderProductionBuilding(CrusaderBuilding):

    def __init__(self, game, hp, armor, abilities: List[Ability], modifiers: List[Modifier]):
        super().__init__(game, hp, armor, abilities + [RALLYPOINT_ABILITY], modifiers)
        self.rallypoint = None

    def set_rallypoint(self, pos: Tuple[int, int]):
        self.rallypoint = pos


class CrusaderFortress(CrusaderProductionBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["fortress"]
        super().__init__(game, STATS["hp"], STATS["armor"], [CREATE_WORKER_ABILITY], [])


class CrusaderBarack(CrusaderProductionBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["barack"]
        super().__init__(game, STATS["hp"], STATS["armor"], [CREATE_SPEARMAN_ABILITY,
                                                             CREATE_SWORDSMAN_ABILITY], [])


class CrusaderTree(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["mine"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class CrusaderMine(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["mine"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class CrusaderTower(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["tower"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])

        self.damage = STATS["damage"]
        self.attack_range = STATS["attack_range"]
        self.attack_speed = STATS["attack_speed"]


class CrusaderSupply(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["supply"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class CrusaderStables(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["stables"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class CrusaderWorkshop(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["workshop"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class CrusaderArsenal(CrusaderBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["crusader"]["arsenal"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabBuilding(Building):
    RACE = Race.ARAB

    def __init__(self, game, hp, armor, abilities: List[Ability], modifiers: List[Modifier]):
        super().__init__(game, hp, armor, abilities, modifiers, ArabBuilding.RACE)


class ArabProductionBuilding(ArabBuilding):

    def __init__(self, game, hp, armor, abilities: List[Ability], modifiers: List[Modifier]):
        super().__init__(game, hp, armor, abilities + [RALLYPOINT_ABILITY], modifiers)
        self.rallypoint = None

    def set_rallypoint(self, pos: Tuple[int, int]):
        self.rallypoint = pos


class ArabPalace(ArabProductionBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["palace"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabBarack(ArabProductionBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["barack"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabMine(ArabBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["mine"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabTower(ArabBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["tower"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])

        self.damage = STATS["damage"]
        self.attack_range = STATS["attack_range"]
        self.attack_range = STATS["attack_speed"]


class ArabSupply(ArabBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["supply"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabStalls(ArabBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["stalls"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabWorkshop(ArabBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["workshop"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])


class ArabArsenal(ArabBuilding):

    def __init__(self, game):
        STATS = BUILDING_STATS["arab"]["arsenal"]
        super().__init__(game, STATS["hp"], STATS["armor"], [], [])
