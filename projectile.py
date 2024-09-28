import pygame

class projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('assets/images/Projectile.png')
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.vector = speed

    def update(self, dt):
        self.rect.move_ip(0, self.speed * dt)
        #check if sprite has gone off screen
        if self.rect.top > 1080:
             self.kill()