from CONSTANTS import *
from modifiers import *
from game_features import TaskManager


class Unit:

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier], race: Race, soldier: bool):
        self.game = game
        self.damage = damage
        self.hp = hp
        self.armor = armor
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.move_speed = move_speed
        self.abilities = AbilityHandler(self, abilities + [NULL_ABILITY, MOVE_ABILITY])
        self.task_manager = TaskManager(self)
        self.modifiers = modifiers
        self.race = race
        self.soldier = soldier


class CrusaderUnit(Unit):
    RACE = Race.CRUSADER

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier], soldier: bool):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, CrusaderUnit.RACE, soldier)


class CrusaderWorker(CrusaderUnit):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["worker"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"], [], [], False)


class CrusaderSoldier(CrusaderUnit):

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier]):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, True)


class CrusaderInfantry(CrusaderSoldier):
    pass


class CrusaderMilitia(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["militia"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"], [], [])


class CrusaderSpearman(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["spearman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)])


class CrusaderSwordsman(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["swordsman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("SPEARMAN", ActionType.ATTACK, 10),
                          Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)])


class CrusaderArcher(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["archer"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("CAVALRY", ActionType.ATTACK, 15),
                          Modifier("SWORDSMAN", ActionType.ATTACK, 15),
                          Modifier("SPEARMAN", ActionType.ATTACK, 15)])


class CrusaderGeneral(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["general"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],

                         [Ability(pygame.K_e, "НЕ ЗАБЫТЬ"), Ability(pygame.K_f, "НЕ ЗАБЫТЬ")],
                         [])


class CrusaderCavalry(CrusaderSoldier):
    pass


class CrusaderEquestrianBrothers(CrusaderCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["equestrian_brothers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class CrusaderOrderKnights(CrusaderCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["order_knights"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class CrusaderHospitallers(CrusaderCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["hospitallers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class CrusaderSiegeMachines(CrusaderSoldier):
    pass


class CrusaderBatteringRam(CrusaderSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["ram"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class CrusaderCatapult(CrusaderSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["catapult"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class ArabUnit(Unit):
    RACE = Race.ARAB

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int,
                 abilities: List[Ability], modifiers: List[Modifier], soldier: bool):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, ArabUnit.RACE, soldier)


class ArabWorker(ArabUnit):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["worker"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"], [], [], False)


class ArabSoldier(ArabUnit):
    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier]):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, True)


class ArabInfantry(ArabSoldier):
    pass


class ArabAssassin(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["assassin"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],

                         [Ability(pygame.K_e, "НЕ ЗАБЫТЬ"), Ability(pygame.K_f, "НЕ ЗАБЫТЬ")],
                         [])


class ArabDesertTribalWarrior(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["desert_tribal_warrior"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)])


class ArabSpearman(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["spearman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)])


class ArabShotelSwordsman(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["swordsman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("SPEARMAN", ActionType.ATTACK, 10),
                          Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)])


class ArabArcher(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["archer"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("CAVALRY", ActionType.ATTACK, 15),
                          Modifier("SWORDSMAN", ActionType.ATTACK, 15),
                          Modifier("SPEARMAN", ActionType.ATTACK, 15)])


class ArabCavalry(ArabSoldier):
    pass


class ArabHorseArchers(ArabCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["horse_archers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class ArabCamelRiders(ArabCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["camel_riders"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class ArabSiegeMachines(ArabSoldier):
    pass


class ArabElephants(ArabSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["elephants"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])


class ArabThrowers(ArabSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["throwers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)])
