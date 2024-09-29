import pygame, math, random

class clsenemy(pygame.sprite.Sprite):

    def __init__(self):
        pos = (random.randint(100, 1820), -20)
        vector = (random.randrange(250, 290), random.randint(1,3))

        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('assets/images/enemy.png')
        self.image=pygame.transform.scale_by(self.image,4)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vector = vector

    def update(self, dt):
        self.rect.move_ip(self.calcnewpos(dt))
        #check if sprite has gone off screen
        if self.rect.top > 1080 or self.rect.bottom<(-80):
             self.kill()

    def calcnewpos(self, dt):
        (angle,z) = self.vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return dx * dt,dy * dt