from CONSTANTS import *
import sprites
import game_features
from final_screen import FinalScreen
import os.path
from datetime import datetime
import pygame.sprite
import building_sprites
import buildings
import unit_sprites
import units
from animation import Animation


class Game:

    def __init__(self, caption="Crusader Empire"):
        pygame.mixer.music.load(os.path.join("data", "The_Lions_Heart.wav"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.screen = screen
        pygame.display.set_caption(caption)
        self.running = False
        self.clock = pygame.time.Clock()
        self.game_init()
        self.iron = 0
        self.wood = 0
        self.food = 1
        self.max_food = 10
        self.win = False

    def game_init(self):
        self.player_race = Race.CRUSADER

        self.cursor = game_features.Cursor()
        self.camera = game_features.Camera()

        self.all_sprites_group = game_features.SelectionGroup()
        self.crusader_sprites_group = game_features.SelectionGroup()
        self.arab_sprites_group = game_features.SelectionGroup()

        self.selected_group = game_features.SelectionGroup()
        self.selection_group1 = game_features.SelectionGroup()
        self.selection_group2 = game_features.SelectionGroup()
        self.selection_group3 = game_features.SelectionGroup()
        self.selection_group4 = game_features.SelectionGroup()
        self.selection_group5 = game_features.SelectionGroup()
        self.selection_group6 = game_features.SelectionGroup()
        self.selection_group7 = game_features.SelectionGroup()
        self.selection_group8 = game_features.SelectionGroup()
        self.selection_group9 = game_features.SelectionGroup()
        self.selection_group0 = game_features.SelectionGroup()
        self.selection_groupF2 = game_features.SelectionGroup()

        self.c_f = building_sprites.CrusaderFortressSprite(self, random.randint(50, 850), random.randint(50, 900),
                                                           [self.all_sprites_group])
        unit_sprites.CrusaderWorkerSprite(self, self.c_f.rect.x + 50, self.c_f.rect.y + self.c_f.rect.height + 5,
                                          [self.all_sprites_group])
        self.a_p = building_sprites.ArabPalaceSprite(self, random.randint(1000, 1800), random.randint(50, 900),
                                                     [self.all_sprites_group])

        self.start_coords = [(self.a_p.rect.x - 35, self.a_p.rect.y),
                             (self.a_p.rect.x - 55, self.a_p.rect.y + 15),
                             (self.a_p.rect.x - 75, self.a_p.rect.y + 50),
                             (self.a_p.rect.x - 40, self.a_p.rect.y + 75),
                             (self.a_p.rect.x - 15, self.a_p.rect.y - 50)]
        self.arab_defenders = [
            unit_sprites.ArabSpearmanSprite(self, self.a_p.rect.x - 35, self.a_p.rect.y,
                                            [self.all_sprites_group]),
            unit_sprites.ArabSpearmanSprite(self, self.a_p.rect.x - 55, self.a_p.rect.y + 15,
                                            [self.all_sprites_group]),
            unit_sprites.ArabSpearmanSprite(self, self.a_p.rect.x - 75, self.a_p.rect.y + 50,
                                            [self.all_sprites_group]),
            unit_sprites.ArabSwordsmanSprite(self, self.a_p.rect.x - 40, self.a_p.rect.y + 75,
                                             [self.all_sprites_group]),
            unit_sprites.ArabSwordsmanSprite(self, self.a_p.rect.x - 15, self.a_p.rect.y - 50,
                                             [self.all_sprites_group])]

        """healthbar"""
        rect = pygame.Rect(self.a_p.rect.x - 200, self.a_p.rect.y - 200, 500, 500)
        self.attack_box = sprites.Sprite()
        self.attack_box.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])

        c = 0
        while True:
            m = building_sprites.CrusaderTreeSprite(self, random.randint(50, 1900), random.randint(50, 900), [])
            if not pygame.sprite.spritecollide(m, self.all_sprites_group, dokill=False):
                self.all_sprites_group.add(m)
                c += 1
            if c == 50:
                break
        self.mines = []
        self.mines_animations = []
        c = 0
        while True:
            m = building_sprites.CrusaderMineSprite(self, random.randint(50, 700), random.randint(50, 900), [])
            if not pygame.sprite.spritecollide(m, self.all_sprites_group, dokill=False):
                self.all_sprites_group.add(m)
                self.mines.append(m)
                c += 1
            if c == 3:
                break

        self.fortress_animation = Animation(self.c_f, CRUSADER_FORTRESS_DICT)
        self.fortress_animation.start_animation()
        for mine in self.mines:
            self.mines_animations.append(Animation(mine, CRUSADER_MINE_DICT))
            self.mines_animations[-1].start_animation()

    def update_groups(self):
        """refilling the units groups"""
        self.crusader_sprites_group.empty()
        self.arab_sprites_group.empty()

        self.crusader_sprites_group.add(*filter(lambda x: x.race == Race.CRUSADER, list(self.all_sprites_group)))
        self.arab_sprites_group.add(*filter(lambda x: x.race == Race.ARAB, list(self.all_sprites_group)))

    def update_camera(self):
        """for future camera"""
        for sprite in self.all_sprites_group:
            self.camera.apply_ip(sprite.rect)

    def draw_selectbox(self, rect: pygame.Rect):
        pygame.draw.rect(self.screen, pygame.Color("green"), rect, width=1)

    def set_camera(self, target):
        """for future camera"""
        self.camera.update(target)
        self.update_camera()

    def process_events(self):
        """processing pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.fortress_animation.stop_animation()
                for mine in self.mines_animations:
                    mine.stop_animation()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.cursor.x0, self.cursor.y0 = event.pos
                    self.cursor.button_down = True
                if event.button == pygame.BUTTON_RIGHT:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.BUTTON_RIGHT, args={"args": event.pos})

            if event.type == pygame.MOUSEMOTION:
                if self.cursor.button_down:
                    self.cursor.x1, self.cursor.y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    self.cursor.x1, self.cursor.y1 = event.pos

                    if self.cursor.x0 == self.cursor.x1 and self.cursor.y0 == self.cursor.y1:
                        self.cursor.x1 += 1
                        self.cursor.y1 += 1
                    self.cursor.button_down = False
                    rect = game_features.create_rect(self.cursor.x0, self.cursor.y0,
                                                     self.cursor.x1, self.cursor.y1)
                    sprite = sprites.Sprite()
                    sprite.load(rect.x, rect.y, pygame.Surface((abs(rect.w), abs(rect.h))), [])
                    if self.player_race == Race.CRUSADER:
                        selected = pygame.sprite.spritecollide(sprite, self.crusader_sprites_group, dokill=False)
                        if self.cursor.x0 + 1 == self.cursor.x1 and self.cursor.y0 + 1 == self.cursor.y1 and selected:
                            selected = [selected[0]]
                        if not pygame.key.get_pressed()[pygame.K_LSHIFT]:
                            self.selected_group.empty()
                        self.selected_group.add(*selected)
                    self.cursor.x1, self.cursor.y1 = -1, -1

            """binding selection groups"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group1.empty()
                        self.selection_group1 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group1.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group1.copy()
                elif event.key == pygame.K_2:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group2.empty()
                        self.selection_group2 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group2.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group2.copy()
                elif event.key == pygame.K_3:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group3.empty()
                        self.selection_group3 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group3.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group3.copy()
                elif event.key == pygame.K_4:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group4.empty()
                        self.selection_group4 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group4.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group4.copy()
                elif event.key == pygame.K_5:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group5.empty()
                        self.selection_group5 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group5.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group5.copy()
                elif event.key == pygame.K_6:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group6.empty()
                        self.selection_group6 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group6.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group6.copy()
                elif event.key == pygame.K_7:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group7.empty()
                        self.selection_group7 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group7.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group7.copy()
                elif event.key == pygame.K_8:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group8.empty()
                        self.selection_group8 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group8.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group8.copy()
                elif event.key == pygame.K_9:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group9.empty()
                        self.selection_group9 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group9.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group9.copy()
                elif event.key == pygame.K_0:
                    if event.mod & pygame.KMOD_LCTRL:
                        self.selection_group0.empty()
                        self.selection_group0 = self.selected_group.copy()
                    elif event.mod & pygame.KMOD_LSHIFT:
                        self.selected_group.add(*iter(self.selection_group0.copy()))
                    else:
                        self.selected_group.empty()
                        self.selected_group = self.selection_group0.copy()
                elif event.key == pygame.K_F2:
                    self.selected_group.empty()
                    self.selected_group.add(*filter(lambda x: isinstance(x, units.CrusaderSoldier),
                                                    list(self.crusader_sprites_group)))

                """connecting abilities to buttons"""
                if event.key == pygame.K_w:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.K_w, args={"args": ()})
                if event.key == pygame.K_s:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.K_s, args={"args": ()})
                if event.key == pygame.K_d:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.K_d, args={"args": ()})
                if event.key == pygame.K_f:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.K_f, args={"args": (pygame.mouse.get_pos())})
                if event.key == pygame.K_b:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.K_b, args={"args": (pygame.mouse.get_pos())})
                if event.key == pygame.K_v:
                    self.selected_group.update("call", function="ability_cast",
                                               key=pygame.K_v, args={"args": (pygame.mouse.get_pos())})

    def run(self):

        """the main cycle"""
        self.running = True

        while self.running:
            self.screen.blit(MAP_IMAGE, (-500, -500))

            self.process_events()
            if self.cursor.button_down and self.cursor.x1 != -1 and self.cursor.y1 != -1:
                self.draw_selectbox(game_features.create_rect(self.cursor.x0, self.cursor.y0,
                                                              self.cursor.x1, self.cursor.y1))

            for sprite in self.all_sprites_group:
                """if sprite is dead remove its food_cost"""
                if sprite.hp <= 0:
                    self.food -= sprite.food_cost
            alive = game_features.SelectionGroup(*filter(lambda x: x.hp > 0, self.all_sprites_group))
            self.all_sprites_group = alive
            for sprite in self.all_sprites_group:
                sprite.task_manager.process()
                """adding rallypoint to the production buildings"""
                if isinstance(sprite, buildings.CrusaderProductionBuilding) and sprite.highlighted \
                        and sprite.rallypoint is not None:
                    self.screen.blit(RALLYPOINTFLAG_IMAGE, sprite.rallypoint)

            self.update_groups()
            self.all_sprites_group.draw(self.screen)
            self.all_sprites_group.update()
            """highlighting the chosen units"""
            self.selected_group.update("call", function="highlight")

            for sprite in self.all_sprites_group:
                """displaying sprites hp"""
                if sprite.race == Race.ARAB or (sprite.race == Race.CRUSADER and sprite.highlighted):
                    pygame.draw.rect(
                        self.screen, color=pygame.Color(
                            "green" if sprite.hp >= 0.8 * sprite.max_hp else "yellow"
                            if sprite.hp >= 0.4 * sprite.max_hp else "red"),
                        rect=pygame.Rect(sprite.rect.left,
                                         sprite.rect.bottom - 2,
                                         sprite.rect.width * sprite.hp / sprite.max_hp, 5))

            target = list(filter(lambda x: x.race == Race.CRUSADER and isinstance(x, units.CrusaderUnit),
                                 (pygame.sprite.spritecollide(self.attack_box, self.all_sprites_group, dokill=False))))

            if target:
                for arab in self.arab_defenders:
                    """making arabs attack the invaders"""
                    arab.move(target[0].rect.center)
                    if (abs(arab.rect.x - target[0].rect.center[0]) < arab.attack_range and
                            abs(arab.rect.y - target[0].rect.center[1]) < arab.attack_range):
                        if arab.task_started is None:
                            arab.task_started = datetime.now()
                        arab.attack(target[0])
            else:
                for i in range(len(self.arab_defenders)):
                    """moving arabs to their places"""
                    self.arab_defenders[i].move(self.start_coords[i])

            """win condition"""
            if self.a_p.hp <= 0:
                self.win = True
            if self.win:
                self.running = False
                FinalScreen(self.wood, self.iron, self.food).run()

            # print(f"дерево: {self.wood}, железо: {self.iron}, еда: {self.food}")
            self.clock.tick(FPS)
            pygame.display.flip()


class Demo(Game):

    def __init__(self, caption="Crusader Empire (DEMO)"):
        super().__init__(caption)

    def game_init(self):
        super().game_init()

        unit_sprites.CrusaderWorkerSprite(self, 150, 550, [self.all_sprites_group])
        building_sprites.CrusaderFortressSprite(self, 100, 500, [self.all_sprites_group])
        building_sprites.CrusaderMineSprite(self, 200, 200, [self.all_sprites_group])
