from CONSTANTS import *
import buildings
import physics

from game_features import Task
from datetime import datetime, timedelta
import sprites


class CrusaderFortressSprite(buildings.CrusaderFortress, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_FORTRESS_IMAGE, groups)
        buildings.CrusaderFortress.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)
        self.task_started = None

    def create_task_worker(self):
        if self.game.wood >= 50 and self.game.max_food - self.game.food >= 1:
            self.task_started = datetime.now()
            task = Task(self.create_worker, 1)
            self.task_manager.tasks.append(task)
            self.game.wood -= 50
            self.game.food += 1
            return 1

    def create_worker(self):
        from unit_sprites import CrusaderWorkerSprite
        if datetime.now() - self.task_started >= timedelta(seconds=3):
            a = CrusaderWorkerSprite(self.game, self.rect.x + 20,
                                     self.rect.y + self.rect.height + 10,
                                     [self.game.all_sprites_group])
            self.task_started = datetime.now()
            if self.rallypoint is not None:
                a.move(self.rallypoint)
            return 1
        return 0


class CrusaderBarackSprite(buildings.CrusaderBarack, sprites.BuildingProductionSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_BARACK_IMAGE, groups)
        buildings.CrusaderBarack.__init__(self, game)
        sprites.BuildingProductionSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)
        self.task_started = None

    def create_task_swordsman(self):
        if self.game.wood >= 50 and self.game.iron >= 50 and self.game.max_food - self.game.food >= 3:
            self.task_started = datetime.now()
            task = Task(self.create_swordsman, 1)
            self.task_manager.tasks.append(task)
            self.game.wood -= 50
            self.game.iron -= 50
            self.game.food += 3
            return 1

    def create_swordsman(self):
        from unit_sprites import CrusaderSwordsmanSprite
        logging.info("creating_swordsman")
        if datetime.now() - self.task_started >= timedelta(seconds=3):
            a = CrusaderSwordsmanSprite(self.game, self.rect.x,
                                        self.rect.y + self.rect.height + 10,
                                        [self.game.all_sprites_group])
            self.task_started = datetime.now()
            if self.rallypoint is not None:
                a.move(self.rallypoint)
            return 1
        return 0

    def create_task_spearman(self):
        if self.game.wood >= 60 and self.game.iron >= 30 and self.game.max_food - self.game.food >= 2:
            self.task_started = datetime.now()
            task = Task(self.create_spearman, 1)
            self.task_manager.tasks.append(task)
            self.game.wood -= 60
            self.game.iron -= 30
            self.game.food += 2
            return 1

    def create_spearman(self):
        from unit_sprites import CrusaderSpearmanSprite
        logging.info("creating_spearman")
        if datetime.now() - self.task_started >= timedelta(seconds=3):
            a = CrusaderSpearmanSprite(self.game, self.rect.x,
                                       self.rect.y + self.rect.height + 10,
                                       [self.game.all_sprites_group])
            self.task_started = datetime.now()
            if self.rallypoint is not None:
                a.move(self.rallypoint)
            return 1
        return 0


class CrusaderMineSprite(buildings.CrusaderMine, sprites.MineSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_MINE_IMAGE, groups)
        buildings.CrusaderMine.__init__(self, game)
        sprites.MineSprite.__init__(self, game)
        physics.Obstacle.__init__(self, game)


class CrusaderTreeSprite(buildings.CrusaderTree, sprites.TreeSprite, physics.Obstacle):

    def __init__(self, game, x, y, groups):
        self.load(x, y, CRUSADER_TREE_IMAGE, groups)
        buildings.CrusaderTree.__init__(self, game)
        sprites.TreeSprite.__init__(self, game)
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
