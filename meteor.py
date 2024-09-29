import pygame, random


class clsmeteor(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/images/meteor_1.png')
        self.image = pygame.transform.scale_by(self.image, round(random.uniform(0.5, 3),1))
        self.image = pygame.transform.rotate(self.image, (random.uniform(0, 360)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = round(random.uniform(1, 3),1)
        self.speedx = random.randint(-2,2)
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = self.rect.width // 2

    def update(self,bg_speed):
        speedy = self.speedy+bg_speed
        self.rect.move_ip(self.speedx, speedy)
        #check if sprite has gone off screen
        if self.rect.top > 1080:
             self.kill()
        
       


