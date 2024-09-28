import pygame, math, sys, random
from player import Player
from meteor import clsmeteor
from enemy import clsenemy
from game import game_end
from speed_orb import Speed_orb
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
bg_speed=100
background_y=-3600
background=pygame.image.load('assets/images/background.png')


player = Player((screen.get_width() / 2, screen.get_height() / 2), screen.get_width(), screen.get_height())

speed_orbs = pygame.sprite.Group()
SpawnOrb = pygame.USEREVENT + 1
Orbtimer = 500
pygame.time.set_timer(SpawnOrb, Orbtimer)

meteors = pygame.sprite.Group()
SpawnMeteor = pygame.USEREVENT + 1
Meteortimer = 2000
pygame.time.set_timer(SpawnMeteor, Meteortimer)  # 1000 milliseconds = 1 second

enemies = pygame.sprite.Group()

projectiles = pygame.sprite.Group()
SpawnProjectiles = pygame.USEREVENT + 1
projectilestimer = 1000
pygame.time.set_timer(SpawnProjectiles, projectilestimer) 


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SpawnMeteor:   
            meteors.add(clsmeteor(random.randint(90,1830),-100))
        elif event.type == SpawnOrb:  
            speed_orbs.add(Speed_orb(random.randint(90,1830),100))
        elif event.type == SpawnProjectiles:   
            projectiles.add(clsenemy.shoot())

    if random.randint(0,10) == 0:
        enemies.add(clsenemy())
            

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,background_y))

    player.handle_input(dt)
    player.position.y+=dt*bg_speed
    player.draw(screen)

    if(player.position.y>=1000):
        game_end()

    speed_orbs.update(bg_speed*dt)
    speed_orbs.draw(screen)
    
    meteors.update(bg_speed*dt)
    meteors.draw(screen)
    collisions = pygame.sprite.spritecollide(player, meteors, False)
    if collisions:
        print("Collision detected!")

    enemies.update(bg_speed * dt)
    enemies.draw(screen)

    projectiles.update(bg_speed*dt)
    projectiles.draw(screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    bg_speed+=dt
    background_y+=dt*bg_speed
    if(background_y>=0):background_y=-3600

pygame.quit()

