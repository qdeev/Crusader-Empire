import game_features
import units
from CONSTANTS import *
from game_features import Task


class Sprite(pygame.sprite.Sprite):

    def load(self, x: int, y: int, image: pygame.Surface, groups: List[pygame.sprite.AbstractGroup]):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass


class GameSprite(Sprite):

    def __init__(self, game):
        super().__init__()
        self.highlighted = False
        self.game = game

    def __str__(self):
        return f'{self.rect.center[0]} {self.rect.center[1]}'

    def update(self, *args: Any, **kwargs: Any) -> None:
        if not args:
            return
        if args[0] == "call":
            if kwargs["function"] in ("highlight", "unhighlight"):
                exec(f"self.{kwargs['function']}()")
            elif kwargs["function"] == "ability_cast":
                exec(f"self.{kwargs['function']}({kwargs['key']}, {str(kwargs['args']['args'])})")

    def highlight(self):
        self.highlighted = True

    def unhighlight(self):
        self.highlighted = False

    def ability_cast(self, key, args):
        self.abilities.cast_ability(key, {"args": args})


class ResourceSprite(GameSprite):

    def __init__(self, game):
        super().__init__(game)

    def get_resources(self):
        pass


class TreeSprite(ResourceSprite):

    def __init__(self, game):
        super().__init__(game)

    def get_resources(self):
        return 50


class MineSprite(ResourceSprite):

    def __init__(self, game):
        super().__init__(game)

    def get_resources(self):
        return 50


class UnitSprite(GameSprite):

    def __init__(self, game):
        super().__init__(game)

    def move(self, args: Tuple[int, int]):
        """adding gathering for workers and fighting for soldiers"""

        self.task_manager.empty()

        if isinstance(self, units.CrusaderWorker):
            rect = game_features.create_rect(args[0], args[1],
                                             args[0] + 1, args[1] + 1)
            sprite = Sprite()
            sprite.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])
            selected = list(filter(lambda x: isinstance(x, ResourceSprite),
                                   pygame.sprite.spritecollide(sprite,
                                                               self.game.all_sprites_group, dokill=False)))
            if selected:
                self.task_manager.tasks.append(Task(self.process_physics, 1, args))
                self.task_gather(selected[0])
            else:
                self.task_manager.tasks.append(Task(self.process_physics, 1, args))
        elif isinstance(self, units.CrusaderSoldier) or isinstance(self, units.ArabSoldier):
            rect = game_features.create_rect(args[0], args[1],
                                             args[0] + 1, args[1] + 1)
            sprite = Sprite()
            sprite.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])
            selected = list(filter(lambda x: x != self,
                                   pygame.sprite.spritecollide(sprite,
                                                               self.game.all_sprites_group, dokill=False)))
            if selected:
                self.task_manager.tasks.append(Task(self.process_physics, 1, args))
                if not isinstance(self, units.ArabSoldier):
                    self.create_task_attack(selected[0])
            else:
                self.task_manager.tasks.append(Task(self.process_physics, 1, args))
        else:
            self.task_manager.tasks.append(Task(self.process_physics, 1, args))


class BuildingSprite(GameSprite):

    def __init__(self, game):
        super().__init__(game)


class BuildingProductionSprite(BuildingSprite):

    def __init__(self, game):
        super().__init__(game)

    def rallypoint(self, args: Tuple[int, int]):
        self.set_rallypoint(args)
