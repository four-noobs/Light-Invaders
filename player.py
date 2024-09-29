import pygame

class Player:
    def __init__(self, pos, screen_width, screen_height):
        self.position = pygame.Vector2(pos)
        
        self.speed = 500
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.original_image = pygame.image.load("assets/images/Player.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (screen_width/28, screen_width/28))

        self.image = self.original_image
        self.image = pygame.transform.scale(self.image, (screen_width/28, screen_width/28))
        self.angle = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.shield = False
        self.shieldDuration = 300     # how many dt
        self.shieldTimer = 0
        self.rect = self.image.get_rect(center=self.position)
        self.hitbox = pygame.Rect(self.position.x - self.width/2, self.position.y - self.height/2, self.width, self.height)

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= self.speed * dt
            
        if keys[pygame.K_s]:
            self.position.y += self.speed * dt
            
        if keys[pygame.K_a]:
            self.position.x -= self.speed * dt
            self.angle = 45
        elif keys[pygame.K_d]:
            self.position.x += self.speed * dt
            self.angle = -45
        else:
            self.angle = 0

        if keys[pygame.K_SPACE] and self.shield == False:
            self.shield = True
            self.shieldTimer = self.shieldDuration
            self.speed=max(0,self.speed - 50) 

        if self.shieldTimer > 0:
            self.shieldTimer -= 1
        else:
            self.shieldTimer = 0
            self.shield = False


        if self.position.x - self.width > self.screen_width:
            self.position.x = -self.width
        elif self.position.x + self.width < 0:
            self.position.x = self.screen_width + self.width

        self.position.y = max(self.position.y, self.height / 2)

        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.rect = self.image.get_rect(center=self.position)
        self.hitbox.topleft = (self.position.x - self.width/2, self.position.y - self.height/2)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, "green", self.hitbox, 2)   # for testing only

        if self.shield:
            pygame.draw.circle(screen, "blue", self.rect.center, int (self.screen_width / 32), int(self.screen_width / 240))  # draw the shield