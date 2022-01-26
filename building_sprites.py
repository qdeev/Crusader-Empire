from CONSTANTS import *
import buildings
import physics
import sprites


class CrusaderFortressSprite(buildings.CrusaderFortress, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_FORTRESS_IMAGE, groups)
        buildings.CrusaderFortress.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderBarackSprite(buildings.CrusaderBarack, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_BARACK_IMAGE, groups)
        buildings.CrusaderBarack.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderMineSprite(buildings.CrusaderMine, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_MINE_IMAGE, groups)
        buildings.CrusaderMine.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderTowerSprite(buildings.CrusaderTower, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_TOWER_IMAGE, groups)
        buildings.CrusaderTower.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderSupplySprite(buildings.CrusaderSupply, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_SUPPLY_IMAGE, groups)
        buildings.CrusaderSupply.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderStablesSprite(buildings.CrusaderStables, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_STABLES_IMAGE, groups)
        buildings.CrusaderStables.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderWorkshopSprite(buildings.CrusaderWorkshop, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_WORKSHOP_IMAGE, groups)
        buildings.CrusaderWorkshop.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderArsenalSprite(buildings.CrusaderArsenal, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_ARSENAL_IMAGE, groups)
        buildings.CrusaderArsenal.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabPalaceSprite(buildings.ArabPalace, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_PALACE_IMAGE, groups)
        buildings.ArabPalace.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabBarackSprite(buildings.ArabBarack, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_BARACK_IMAGE, groups)
        buildings.ArabBarack.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabMineSprite(buildings.ArabMine, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_MINE_IMAGE, groups)
        buildings.ArabMine.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabTowerSprite(buildings.ArabTower, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_TOWER_IMAGE, groups)
        buildings.ArabTower.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabSupplySprite(buildings.ArabSupply, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_SUPPLY_IMAGE, groups)
        buildings.ArabSupply.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabStallsSprite(buildings.ArabStalls, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_STALLS_IMAGE, groups)
        buildings.ArabStalls.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabWorkshopSprite(buildings.ArabWorkshop, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_WORKSHOP_IMAGE, groups)
        buildings.ArabWorkshop.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class ArabArsenalSprite(buildings.ArabArsenal, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, ARAB_ARSENAL_IMAGE, groups)
        buildings.ArabArsenal.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)
