import pygame as pg
from settings import *


class Admin:
    def __init__(self, game):
        self.noclip = False
        self.game = game
        self.die = False
        self.safety = False
        self.shoot_throuh_walls = False
        self.god_gun = False
    def check(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_0]:
            self.noclip = True if not self.noclip else False
        if keys[pg.K_1]:
            self.shoot_throuh_walls = True if not self.shoot_throuh_walls else False
        if keys[pg.K_2]:
            self.god_gun = True if not self.god_gun else False
        if keys[pg.K_BACKSPACE] and keys[pg.K_y]:
            self.safety = True
        if keys[pg.K_n] and keys[pg.K_o] and self.safety:
            self.game.object_renderer.sky_image = self.game.object_renderer.get_texture('resources/sprites/npc/soldier/0.png', (WIDTH, HALF_HEIGHT))
            self.game.player.oops()
        
    def update(self):
        self.check()