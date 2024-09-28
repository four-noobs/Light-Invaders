import pygame, math, random
import projectile

enemyImage = pygame.image.load('assets/images/meteor_1.png')

class enemy(pygame.sprite.Sprite):

    def __init__(self):
        pos = (random.randint(1920), -100)
        vector = (random.randrange(-20, 20), random.randint(1,6))

        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = enemyImage
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
    
    def shoot(self):
        projectile((self.rect.x // 2, self.rect.y // 2), random.randint(1,6))