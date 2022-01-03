from CONSTANTS import *
from modifiers import *


class Building:

    def __init__(self, hp, armor, abilities: List[Ability], modifiers: List[Modifier], race):
        self.hp = hp
        self.armor = armor
        self.abilities = abilities
        self.modifiers = [Modifier("SIEGE", ActionType.ATTACKED, 100)] + modifiers
        self.race = race


class CrusaderBuilding(Building):
    RACE = Race.CRUSADER

    def __init__(self, hp, armor, abilities: List[Ability], modifiers: List[Modifier]):
        super().__init__(hp, armor, abilities, modifiers, CrusaderBuilding.RACE)


class CrusaderFortress(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["fortress"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class CrusaderBarack(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["barack"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class CrusaderMine(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["mine"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class CrusaderTower(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["tower"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)

        self.damage = STATS["damage"]
        self.attack_range = STATS["attack_range"]
        self.attack_range = STATS["attack_speed"]


class CrusaderSupply(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["supply"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class CrusaderStables(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["stables"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class CrusaderWorkshop(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["workshop"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class CrusaderArsenal(CrusaderBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["crusader"]["arsenal"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabBuilding(Building):
    RACE = Race.ARAB

    def __init__(self, hp, armor, abilities: List[Ability], modifiers: List[Modifier]):
        super().__init__(hp, armor, abilities, modifiers, ArabBuilding.RACE)


class ArabPalace(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["palace"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabBarack(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["barack"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabMine(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["mine"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabTower(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["tower"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)

        self.damage = STATS["damage"]
        self.attack_range = STATS["attack_range"]
        self.attack_range = STATS["attack_speed"]


class ArabSupply(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["supply"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabStalls(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["stalls"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabWorkshop(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["workshop"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)


class ArabArsenal(ArabBuilding):

    def __init__(self, abilities: List[Ability], modifiers: List[Modifier]):
        STATS = BUILDING_STATS["arab"]["arsenal"]
        super().__init__(STATS["hp"], STATS["armor"], abilities, modifiers)
