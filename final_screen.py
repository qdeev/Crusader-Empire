from CONSTANTS import *

background_image = pygame.image.load(os.path.join('data/assets/textures/fon.jpg'))


class FinalScreen:

    def __init__(self, wood, iron, food):
        logging.info("the_end")
        self.wood = wood
        self.iron = iron
        self.food = food

    def draw(self):
        screen.blit(background_image, (0, 0))
        font = pygame.font.Font(os.path.join('data/assets/title_font.ttf'), 100)
        text = font.render("You Won!", True, (0, 0, 0))
        text1 = font.render("You had", True, (0, 0, 0))
        text2 = font.render(f"wood: {self.wood} iron: {self.iron} ", True, (0, 0, 0))
        text3 = font.render(f"food: {self.food}", True, (0, 0, 0))
        text_x = SCREEN_WIDTH // 2 - text.get_width() // 2
        text_y = SCREEN_HEIGHT // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y - 100))
        screen.blit(text1, (text_x + 20, text_y))
        screen.blit(text2, (text_x - 400, text_y + 100))
        screen.blit(text3, (text_x + 20, text_y + 230))

    def run(self):
        self.draw()
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
