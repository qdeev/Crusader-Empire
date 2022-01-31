from CONSTANTS import *


@dataclass
class Cursor:
    x0: int = -1
    y0: int = -1
    x1: int = -1
    y1: int = -1
    button_down: bool = False


class Camera:
    """is going to added in the future"""
    SPEED = 1

    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply_ip(self, rect: pygame.Rect):
        rect.move_ip(self.dx, self.dy)

    def apply(self, rect: pygame.Rect):
        return rect.move(self.dx, self.dy)

    def update(self, target: pygame.Rect):
        self.dx = -(target.x + target.w // 2 - SCREEN_WIDTH // 2)
        self.dy = -(target.y + target.h // 2 - SCREEN_HEIGHT // 2)


class SelectionGroup(pygame.sprite.Group):

    def __str__(self):
        return str(self.sprites())

    def __getitem__(self, index: int):
        return self.sprites()[index]

    def __init__(self, *sprites: Union[pygame.sprite.Sprite, Sequence[pygame.sprite.Sprite]]):
        super().__init__(*sprites)

    def empty(self) -> None:
        self.update("call", function="unhighlight")
        super().empty()


class Task:

    def __init__(self, function, condition, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.condition = condition
        self.is_active = True

    def __repr__(self):
        return self.function.__name__

    def perform(self):
        if self.is_active:
            if self.function(*self.args, **self.kwargs) == self.condition:
                self.is_active = False


class TaskManager:

    def __init__(self, unit):
        self.unit = unit
        self.tasks: List[Task] = []

    def process(self):
        if self.tasks:
            self.tasks[0].perform()
            if not self.tasks[0].is_active:
                self.tasks.pop(0)

    def empty(self):
        self.tasks = []


def create_rect(x0: int, y0: int, x1: int, y1: int):
    x, y = x0, y0
    w, h = x1 - x0, y1 - y0
    if w < 0 and h < 0:
        x, y = x1, y1
    elif w < 0:
        x, y = x1, y0
    elif h < 0:
        x, y = x0, y1
    return pygame.Rect(x, y, abs(w), abs(h))
