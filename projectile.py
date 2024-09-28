import pygame

projectileImage = pygame.image.load('assets/images/meteor_1.png')

class projectile(pygame.sprite.Sprite):

    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = projectileImage
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vector = speed

    def update(self):
        newpos = self.calcnewpos(self.rect,self.speed)
        self.rect = newpos

    def calcnewpos(self,rect,speed):
        (dx,dy) = (0,speed)
        return rect.move(dx,dy)