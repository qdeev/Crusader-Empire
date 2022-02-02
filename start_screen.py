from CONSTANTS import *
from game import Game

name_fon = (255, 255, 255)
font = pygame.font.Font(os.path.join('data/assets/title_font.ttf'), 100)
background_image = pygame.image.load(os.path.join('data/assets/textures/fon.jpg'))
game_name = font.render('CRUSADER EMPIRE', True, name_fon)


class Menu:
    def __init__(self):
        logging.info("started_menu")
        pygame.mixer.music.load(os.path.join("data", "Awakening.wav"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        self._options = []
        self._callbacks = []
        self._current_option_index = 0
        self.running = True
        self.append_option('Start game', lambda: (self.quit_game(), Game().run()))
        self.append_option('Quit', self.quit_game)

    def append_option(self, option, callback):
        self._options.append(font.render(option, True, (0, 0, 0)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = abs(self._current_option_index + direction) % 2

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._options):
            option_rect: pygame.Rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding + 50)
            if i == self._current_option_index:
                pygame.draw.rect(surf, (205, 133, 63), option_rect)
            surf.blit(option, option_rect)
        for i, option in enumerate(self._options):
            option_rect: pygame.Rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding + 50)
            surf.blit(option, option_rect)

    def quit_game(self):
        self.running = False

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.quit_game()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_w:
                        self.switch(-1)
                    elif e.key == pygame.K_s:
                        self.switch(1)
                    elif e.key == pygame.K_SPACE:
                        self.select()

            screen.blit(background_image, (0, 0))
            screen.blit(game_name, (430, 100))

            self.draw(screen, 500, 400, 75)
            pygame.display.flip()
