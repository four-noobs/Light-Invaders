import pygame

class Speed_orb(pygame.sprite.Sprite,):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/images/speed_orb.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, bg_speed):
        speed=bg_speed
        self.rect.move_ip(0, speed)
        #check if sprite has gone off screen
        if self.rect.top > 1080:
             self.kill()