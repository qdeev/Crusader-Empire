from CONSTANTS import *
import physics
import units
from sprites import UnitSprite

from game_features import Task, create_rect
from datetime import datetime, timedelta
import sprites


class CrusaderWorkerSprite(units.CrusaderWorker, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_WORKER_IMAGE, groups)
        units.CrusaderWorker.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)
        self.task_started = None

    def task_gather(self, target):
        self.task_started = datetime.now()
        task = Task(self.gather, 1, target)
        self.task_manager.tasks.append(task)
        return 1

    def gather(self, target):
        logging.info("gathering")
        if datetime.now() - self.task_started >= timedelta(seconds=3):
            if isinstance(target, sprites.TreeSprite):
                self.game.wood += target.get_resources()
            elif isinstance(target, sprites.MineSprite):
                self.game.iron += target.get_resources()
            self.task_started = datetime.now()
            return 1
        return 0

    def create_task_fortress(self, point: Tuple[int, int]):
        if self.game.wood >= 400 and self.game.iron >= 400:
            self.task_started = datetime.now()
            task = Task(self.create_fortress, 1, point)
            self.task_manager.tasks.append(task)
            self.game.wood -= 400
            self.game.iron -= 400
            return 1

    def create_fortress(self, point: Tuple[int, int]):
        from building_sprites import CrusaderFortressSprite
        logging.info("creating_fortress")
        rect = create_rect(point[0], point[1], point[0] + 30, point[1] + 30)
        sprite = sprites.Sprite()
        sprite.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])
        if not pygame.sprite.spritecollide(sprite, self.game.all_sprites_group, dokill=False):
            if datetime.now() - self.task_started >= timedelta(seconds=10):
                CrusaderFortressSprite(self.game, point[0], point[1], [self.game.all_sprites_group])
                self.task_started = datetime.now()
                return 1
        return 0

    def create_task_barack(self, point: Tuple[int, int]):
        if self.game.wood >= 100 and self.game.iron >= 100:
            self.task_started = datetime.now()
            task = Task(self.create_barack, 1, point)
            self.task_manager.tasks.append(task)
            self.game.wood -= 100
            self.game.iron -= 100
            return 1

    def create_barack(self, point: Tuple[int, int]):
        from building_sprites import CrusaderBarackSprite
        logging.info("creating_barack")
        rect = create_rect(point[0], point[1], point[0] + 30, point[1] + 30)
        sprite = sprites.Sprite()
        sprite.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])
        if not pygame.sprite.spritecollide(sprite, self.game.all_sprites_group, dokill=False):
            if datetime.now() - self.task_started >= timedelta(seconds=7):
                CrusaderBarackSprite(self.game, point[0], point[1], [self.game.all_sprites_group])
                self.task_started = datetime.now()
                return 1
        return 0

    def create_task_supply(self, point: Tuple[int, int]):
        if self.game.wood >= 100:
            self.task_started = datetime.now()
            task = Task(self.create_supply, 1, point)
            self.task_manager.tasks.append(task)
            self.game.wood -= 100
            return 1

    def create_supply(self, point: Tuple[int, int]):
        from building_sprites import CrusaderSupplySprite
        logging.info("creating_supply")
        rect = create_rect(point[0], point[1], point[0] + 30, point[1] + 30)
        sprite = sprites.Sprite()
        sprite.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])
        if not pygame.sprite.spritecollide(sprite, self.game.all_sprites_group, dokill=False):
            if datetime.now() - self.task_started >= timedelta(seconds=5):
                CrusaderSupplySprite(self.game, point[0], point[1], [self.game.all_sprites_group])
                self.task_started = datetime.now()
                self.game.max_food += 8
                return 1
        return 0


class CrusaderMilitiaSprite(units.CrusaderMilitia, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_MILITIA_IMAGE, groups)
        units.CrusaderMilitia.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderSwordsmanSprite(units.CrusaderSwordsman, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_SWORDSMAN_IMAGE, groups)
        units.CrusaderSwordsman.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderSpearmanSprite(units.CrusaderSpearman, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_SPEARMAN_IMAGE, groups)
        units.CrusaderSpearman.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderArcherSprite(units.CrusaderArcher, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_ARCHER_IMAGE, groups)
        units.CrusaderArcher.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderGeneralSprite(units.CrusaderGeneral, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_GENERAL_IMAGE, groups)
        units.CrusaderGeneral.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderEquestrianBrothersSprite(units.CrusaderEquestrianBrothers, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_EQUESTRIAN_BROTHERS_IMAGE, groups)
        units.CrusaderEquestrianBrothers.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderOrderKnightsSprite(units.CrusaderOrderKnights, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_ORDER_KNIGHTS_IMAGE, groups)
        units.CrusaderOrderKnights.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderHospitallersSprite(units.CrusaderHospitallers, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_HOSPITALLERS_IMAGE, groups)
        units.CrusaderHospitallers.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderBatteringRamSprite(units.CrusaderBatteringRam, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_BATTERING_RAM, groups)
        units.CrusaderBatteringRam.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class CrusaderCatapultSprite(units.CrusaderCatapult, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_CATAPULT_IMAGE, groups)
        units.CrusaderCatapult.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabWorkerSprite(units.ArabWorker, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_WORKER_IMAGE, groups)
        units.ArabWorker.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabSwordsmanSprite(units.ArabShotelSwordsman, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_SHOTEL_SWORDSMAN_IMAGE, groups)
        units.ArabShotelSwordsman.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabSpearmanSprite(units.ArabSpearman, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_SPEARMAN_IMAGE, groups)
        units.ArabSpearman.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabArcherSprite(units.ArabArcher, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_ARCHER_IMAGE, groups)
        units.ArabArcher.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabHorseArchersSprite(units.ArabHorseArchers, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_HORSE_ARCHERS_IMAGE, groups)
        units.ArabHorseArchers.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabCamelRidersSprite(units.ArabCamelRiders, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_CAMEL_RIDERS_IMAGE, groups)
        units.ArabCamelRiders.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabElephantsSprite(units.ArabElephants, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_ELEPHANTS_IMAGE, groups)
        units.ArabElephants.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabThrowersSprite(units.ArabThrowers, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_THROWERS_IMAGE, groups)
        units.ArabThrowers.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


class ArabAssassinSprite(units.ArabAssassin, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_ASSASSIN_IMAGE, groups)
        units.ArabAssassin.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)
