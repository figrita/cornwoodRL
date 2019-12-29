import pygame as pg

class player(pg.sprite.Sprite):
    """ Representing the player as a moon buggy type car.
    """
    moving = False
    vector = (0, 0)
    time = 0
    duration = 24
    starting_pos = (320, 420)
    speed = 2
    bounce = 13
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

    def move(self, xdirection, ydirection):
        if xdirection != 0 or ydirection != 0:
            if self.moving == False:
                self.moving = True
                if xdirection != 0:
                    self.vector = (xdirection, 0)
                else:
                    self.vector = (0, ydirection)
                self.time = 0
                self.duration = 24

    def update(self):
        """ We only update the score in update() when it has changed.
        """
        if self.moving:
            self.time += 1
            (self.rect.left, self.rect.top) = (
                self.easeInOutQuad(self.time, self.starting_pos[0], 16 * self.vector[0], self.duration),
                self.easeInOutQuad(self.time, self.starting_pos[1], 16 * self.vector[1], self.duration))
            if self.time == self.duration:
                self.moving = False
                self.starting_pos = (self.rect.x, self.rect.y)

    def easeInOutQuad(self, current_time, start_value, change_in_value, duration):
        current_time = current_time / (duration / 2.)
        if (current_time < 1.):
            return change_in_value / 2. * current_time * current_time + start_value
        current_time -= 1.
        return -change_in_value / 2. * (current_time * (current_time - 2.) - 1.) + start_value
