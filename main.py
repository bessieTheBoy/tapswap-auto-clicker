import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from admin import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *




class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.admin = Admin(self)
        self.dt = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 100)
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.obj_handle = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = Pathfinding(self)
        pg.mixer.music.play()
        self.npc_count = -1
        
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.admin.update()
        self.obj_handle.update()
        self.weapon.update()
        pg.display.flip()
        self.dt = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")
        
    def draw(self):
        #self.screen.fill("black")
        self.object_renderer.draw()
        self.weapon.draw()
        #self.map.draw()
        #self.player.draw()
    def check_events(self):
        self.global_trigger = False
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif e.type == self.global_event:
                self.global_trigger = True
                
            self.player.single_fire_event(e)
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()