import pygame as pg

class player(pg.sprite.Sprite):
    """ Representing the player as a moon buggy type car.
    """

    speed = 10
    bounce = 24
    gun_offset = -11
    images = []

    def __init__(self, img, group):
        pg.sprite.Sprite.__init__(self)
        self.add(group)
        self.images = [img, pg.transform.flip(img, 1, 0)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pg.Rect(0, 0, 640, 480).midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(pg.Rect(0, 0, 640, 480))
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

    def update(self):
        """ We only update the score in update() when it has changed.
        """