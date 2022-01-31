import pygame.sprite

import units
from CONSTANTS import *


class PhysicObject:

    def __init__(self, game):
        self.game = game


class RigidBody(PhysicObject):

    def __init__(self, game):
        super().__init__(game)
        self.draw = 0

        self.velocity = pygame.math.Vector2()
        self.velocity.x, self.velocity.y = 0, 0

    def avoid(self):
        """changing sprites pos to avoid the collision"""
        for unit in filter(lambda x: isinstance(x, units.Unit), self.game.all_sprites_group):
            if unit != self:
                shift = pygame.math.Vector2(self.rect.center) - pygame.math.Vector2(unit.rect.center)
                if pygame.Rect.colliderect(self.rect, unit.rect):
                    self.rect.center += shift.normalize()

    def collide(self):
        """colliding with units and obstacles"""
        hits_list = pygame.sprite.spritecollide(self, pygame.sprite.Group(list(
            filter(lambda x: not isinstance(x, units.Unit), self.game.all_sprites_group))), False)
        if hits_list:
            if hits_list[0].rect.centerx > self.rect.centerx:
                x = hits_list[0].rect.left - self.rect.width / 2
            elif hits_list[0].rect.centerx < self.rect.centerx:
                x = hits_list[0].rect.right + self.rect.width / 2
            else:
                x = self.rect.center[0]
            self.velocity.x = 0
            self.rect.centerx = x

        hits_list = pygame.sprite.spritecollide(self, pygame.sprite.Group(list(
            filter(lambda x: not isinstance(x, units.Unit), self.game.all_sprites_group))), False)
        if hits_list:
            if hits_list[0].rect.centery > self.rect.centery:
                y = hits_list[0].rect.top - self.rect.height / 2
            elif hits_list[0].rect.centery < self.rect.centery:
                y = hits_list[0].rect.bottom + self.rect.height / 2
            else:
                y = self.rect.center[1]
            self.velocity.y = 0
            self.rect.centery = y

    def process_physics(self, pos: Tuple[int, int]):
        """moving"""
        try:
            leg_x, leg_y = abs(pos[0] - self.rect.center[0]) if abs(pos[0] - self.rect.center[0]) > 0 else 0.001, \
                           abs(pos[1] - self.rect.center[1])
            velocity_x = self.move_speed / math.sqrt(1 + (leg_y / leg_x))
            velocity_y = velocity_x * (leg_y / leg_x)
            if 0 <= leg_x < 10:
                velocity_x = 0
            if 0 <= leg_y < 10:
                velocity_y = 0
            if velocity_x > 3:
                velocity_x = 3
            if velocity_y > 3:
                velocity_y = 3

            if pos[0] >= self.rect.center[0] and pos[1] <= self.rect.center[1]:
                to_point = pygame.math.Vector2((velocity_x, -velocity_y))
            elif pos[0] >= self.rect.center[0] and pos[1] >= self.rect.center[1]:
                to_point = pygame.math.Vector2((velocity_x, velocity_y))
            elif pos[0] <= self.rect.center[0] and pos[1] <= self.rect.center[1]:
                to_point = pygame.math.Vector2((-velocity_x, -velocity_y))
            elif pos[0] <= self.rect.center[0] and pos[1] >= self.rect.center[1]:
                to_point = pygame.math.Vector2((-velocity_x, velocity_y))
            else:
                to_point = pygame.math.Vector2()
            self.rect.center += to_point

            self.avoid()
            self.collide()

        except ValueError:
            pass

        finally:
            if isinstance(self, units.CrusaderWorker) and abs(pos[0] - self.rect.center[0]) < 30 \
                    and abs(pos[1] - self.rect.center[1]) < 30:
                return 1
            elif isinstance(self, units.CrusaderSoldier) and abs(pos[0] - self.rect.center[0]) < self.attack_range \
                    and abs(pos[1] - self.rect.center[1]) < self.attack_range:
                return 1
            return 0


class Obstacle(PhysicObject):

    def __init__(self, game):
        super().__init__(game)
