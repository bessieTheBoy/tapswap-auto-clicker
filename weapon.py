from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path="resources/sprites/weapon/shotgun/0.png", scale=0.4, animation_time=90, shift=500.27):
        super().__init__(game, path=path, scale=scale, animation_time=animation_time , shift=shift)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images
             ]
        )
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 90000 if game.admin.god_gun else 50
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, self.images[0].get_height())
    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0
    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
    
    def update(self):
        self.check_animation_time()
        self.animate_shot()

