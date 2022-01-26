from CONSTANTS import *
import physics
import units
from sprites import UnitSprite


class CrusaderWorkerSprite(units.CrusaderWorker, UnitSprite, physics.RigidBody):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_WORKER_IMAGE, groups)
        units.CrusaderWorker.__init__(self, game)
        UnitSprite.__init__(self, game)
        physics.RigidBody.__init__(self, game)


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
