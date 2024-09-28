import pygame, math, sys, random
from player import Player
from meteor import clsmeteor
from enemy import clsenemy
from projectile import projectile 
from game import *
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
Orbtimer = 1000
pygame.time.set_timer(SpawnOrb, Orbtimer)

meteors = pygame.sprite.Group()
SpawnMeteor = pygame.USEREVENT + 2
Meteortimer = 1000
pygame.time.set_timer(SpawnMeteor, Meteortimer)  # 1000 milliseconds = 1 secoand

enemies = pygame.sprite.Group()

projectiles = pygame.sprite.Group()
SpawnProjectiles = pygame.USEREVENT + 3
projectilestimer = 3000
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
            for i in enemies:
                projectiles.add(projectile(i.rect.center))

    if random.randint(0,10) == 0:
        enemies.add(clsenemy())
            

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,background_y))

    player.handle_input(dt)
    player.position.y+=dt*bg_speed
    player.draw(screen)

    if(player.position.y>=1000):
        game_end()
        running = False

    speed_orbs.update(bg_speed*dt)
    speed_orbs.draw(screen)
    
    meteors.update(bg_speed*dt)
    meteors.draw(screen)
    hit_meteor = pygame.sprite.spritecollide(player, meteors, True)
    if hit_meteor:
        player.speed=max(0,player.speed+collision('slow')) 

    hit_enemy = pygame.sprite.spritecollide(player, enemies, True)
    if hit_enemy:
        player.speed=max(0,player.speed+collision('slow')) 

    hit_orb = pygame.sprite.spritecollide(player, speed_orbs, True)
    if hit_orb:
        player.speed+= collision('fast')

    hit_projectile = pygame.sprite.spritecollide(player, projectiles, True)
    if hit_projectile:
        player.speed=max(0,player.speed+collision('slow'))

    enemies.update(bg_speed * dt)
    enemies.draw(screen)

    projectiles.update(bg_speed*dt)
    projectiles.draw(screen)

    
    display_speed(screen, player.speed)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    bg_speed+=dt
    background_y+=dt*bg_speed
    if(background_y>=0):background_y=-3600

PlayAgain = True   
while PlayAgain:
    break
    
pygame.quit()
sys.exit()
