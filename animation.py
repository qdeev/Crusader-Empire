from CONSTANTS import *
from itertools import cycle
from threading import Timer


"""https://github.com/JktuJQ/PyGG"""


class Animation:

    class __AnimationState(IntEnum):
        """Animation states"""
        DISABLED = 0
        ENABLED = 1

    def __init__(self, sprite, images_dictionary: Dict[str, Iterable[pygame.Surface]]):
        self.binded_sprite = sprite
        self.packed_images = {key: cycle(value) for key, value in images_dictionary.items()}
        self.status: str = "idle"
        self.__animation_state = self.__AnimationState.DISABLED
        self.__timer: Timer = Timer(0, self.animate)
        self.__images_generator: Generator = (_ for _ in ())

    def start_animation(self, delay: float = 0.3):
        """Start animation cycle if possible"""
        self.__animation_state = self.__animation_state.ENABLED
        self.__images_generator = self.generator()
        self.animate(delay)

    def animate(self, delay: float = 0.3):
        """Function that is called every animation cycle iteration"""
        if self.__animation_state == self.__AnimationState.ENABLED:
            self.binded_sprite.image = next(self.__images_generator)
            self.__timer = Timer(delay, self.animate)
            self.__timer.start()

    def stop_animation(self):
        """Stops animation cycle if possible"""
        self.__timer.cancel()

    def generator(self):
        """Creates generator of images"""
        while True:
            if self.__animation_state == self.__AnimationState.ENABLED:
                yield next(self.packed_images[self.status])