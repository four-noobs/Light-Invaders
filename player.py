import pygame

class Player:
    def __init__(self, pos, screen_width, screen_height):
        self.position = pygame.Vector2(pos)
        
        self.speed = 500
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("assets/images/Player.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.position)
        self.width = self.image.get_width()
        print(self.width)
        self.height = self.image.get_height()
        print(self.height)
        self.hitbox = pygame.Rect(self.position.x - self.width, self.position.y - self.height, self.width * 2, self.height * 2)

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.position.y += self.speed * dt
        if keys[pygame.K_a]:
            self.position.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.position.x += self.speed * dt

        if self.position.x - self.width > self.screen_width:
            self.position.x = -self.width
        elif self.position.x + self.width < 0:
            self.position.x = self.screen_width + self.width

        self.position.y = max(self.height, min(self.position.y, self.screen_height - self.height))

        self.hitbox.topleft = (self.position.x - self.width, self.position.y - self.height)
        self.rect.center = self.position


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, "green", self.hitbox, 2)   # for testing only