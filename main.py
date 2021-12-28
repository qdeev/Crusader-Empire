from CONSTANTS import *
import pygame as pygame


if __name__ == '__main__':
    running = True
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()