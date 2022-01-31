import pygame.sprite

from modifiers import *
from datetime import datetime, timedelta
from game_features import TaskManager, Task


class Unit:

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier], race: Race, soldier: bool, food_cost):
        self.game = game
        self.damage = damage
        self.max_hp = hp
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
        self.food_cost = food_cost


class CrusaderUnit(Unit):
    RACE = Race.CRUSADER

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier], soldier: bool, food_cost: int):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, CrusaderUnit.RACE, soldier, food_cost)


class CrusaderWorker(CrusaderUnit):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["worker"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"], [CREATE_FORTRESS_ABILITY,
                                                                                             CREATE_BARACK_ABILITY,
                                                                                             CREATE_SUPPLY_ABILITY], [],
                         False, STATS["food_cost"])


class CrusaderSoldier(CrusaderUnit):

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier], food_cost):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, True, food_cost)
        self.task_started = None

    def create_task_attack(self, target: pygame.sprite.Sprite):
        self.task_started = datetime.now()

        task = Task(self.attack, 1, target)
        self.task_manager.tasks.append(task)

        return 1

    def attack(self, target):
        logging.info("crusader_attack")
        if datetime.now() - self.task_started >= timedelta(seconds=self.attack_speed):
            target.hp -= self.damage
            self.task_started = datetime.now()
            return 1
        return 0


class CrusaderInfantry(CrusaderSoldier):
    pass


class CrusaderMilitia(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["militia"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"], [], [], STATS["food_cost"])


class CrusaderSpearman(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["spearman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)], STATS["food_cost"])


class CrusaderSwordsman(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["swordsman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("SPEARMAN", ActionType.ATTACK, 10),
                          Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)], STATS["food_cost"])


class CrusaderArcher(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["archer"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("CAVALRY", ActionType.ATTACK, 15),
                          Modifier("SWORDSMAN", ActionType.ATTACK, 15),
                          Modifier("SPEARMAN", ActionType.ATTACK, 15)], STATS["food_cost"])


class CrusaderGeneral(CrusaderInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["general"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],

                         [Ability(pygame.K_e, ""), Ability(pygame.K_f, "")],
                         [], STATS["food_cost"])


class CrusaderCavalry(CrusaderSoldier):
    pass


class CrusaderEquestrianBrothers(CrusaderCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["equestrian_brothers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class CrusaderOrderKnights(CrusaderCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["order_knights"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class CrusaderHospitallers(CrusaderCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["hospitallers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class CrusaderSiegeMachines(CrusaderSoldier):
    pass


class CrusaderBatteringRam(CrusaderSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["ram"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class CrusaderCatapult(CrusaderSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["catapult"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class ArabUnit(Unit):
    RACE = Race.ARAB

    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int,
                 abilities: List[Ability], modifiers: List[Modifier], soldier: bool, food_cost):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, ArabUnit.RACE, soldier, food_cost)


class ArabWorker(ArabUnit):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["worker"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"],
                         STATS["move_speed"], [], [], False, STATS["food_cost"])


class ArabSoldier(ArabUnit):
    def __init__(self, game, damage: int, hp: int, armor: int,
                 attack_range: int, attack_speed: int, move_speed: int, abilities: List[Ability],
                 modifiers: List[Modifier], food_cost):
        super().__init__(game, damage, hp, armor, attack_range,
                         attack_speed, move_speed, abilities, modifiers, True, food_cost)
        self.task_started = None

    def create_task_attack(self, target: pygame.sprite.Sprite):
        self.task_started = datetime.now()

        task = Task(self.attack, 1, target)
        self.task_manager.tasks.append(task)
        return 1

    def attack(self, target):
        logging.info("arabs_attacking")
        if datetime.now() - self.task_started >= timedelta(seconds=self.attack_speed):
            target.hp -= self.damage
            self.task_started = datetime.now()
            return 1
        return 0


class ArabInfantry(ArabSoldier):
    pass


class ArabAssassin(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["crusader"]["assassin"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"], [], [], STATS["food_cost"])


class ArabDesertTribalWarrior(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["desert_tribal_warrior"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)], STATS["food_cost"])


class ArabSpearman(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["spearman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)], STATS["food_cost"])


class ArabShotelSwordsman(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["swordsman"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("SPEARMAN", ActionType.ATTACK, 10),
                          Modifier("LIGHT_CAVALRY", ActionType.ATTACK, 20)], STATS["food_cost"])


class ArabArcher(ArabInfantry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["archer"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("CAVALRY", ActionType.ATTACK, 15),
                          Modifier("SWORDSMAN", ActionType.ATTACK, 15),
                          Modifier("SPEARMAN", ActionType.ATTACK, 15)], STATS["food_cost"])


class ArabCavalry(ArabSoldier):
    pass


class ArabHorseArchers(ArabCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["horse_archers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class ArabCamelRiders(ArabCavalry):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["camel_riders"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class ArabSiegeMachines(ArabSoldier):
    pass


class ArabElephants(ArabSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["elephants"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])


class ArabThrowers(ArabSiegeMachines):

    def __init__(self, game):
        STATS = UNIT_STATS["arab"]["throwers"]
        super().__init__(game, STATS["damage"], STATS["hp"], STATS["armor"],
                         STATS["attack_range"], STATS["attack_speed"], STATS["move_speed"],
                         [],
                         [Modifier("ARCHER", ActionType.ATTACK, 15),
                          Modifier("SIEGE", ActionType.ATTACK, 5)], STATS["food_cost"])
