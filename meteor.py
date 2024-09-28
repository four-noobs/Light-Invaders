import pygame


class clsmeteor(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/images/meteor_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = 2

    def update(self):
        self.rect.move_ip(0, self.speedy)
        #check if sprite has gone off screen
        if self.rect.top > 1080:
             self.kill()
        
       


