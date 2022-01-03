from CONSTANTS import *


class Game:

    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def run(self):
        self.running = True

        while self.running:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # all_sprites.draw(screen)
            # all_sprites.update()
            self.clock.tick(FPS)
            pygame.display.flip()

