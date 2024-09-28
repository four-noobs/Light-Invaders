import pygame, math, sys, random
from player import Player
from meteor import clsmeteor
import enemy
import game
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
bg_speed=0
background_y=-3600
background=pygame.image.load('assets/images/background.png')

speed=100

player = Player((screen.get_width() / 2, screen.get_height() / 2), screen.get_width(), screen.get_height())

meteors = pygame.sprite.Group()
meteors.add(clsmeteor(random.randint(100,1820),-100))

enemies = pygame.sprite.Group()
enemies.add(enemy())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,background_y))

    player.handle_input(dt)
    player.position.y-dt*bg_speed
    player.draw(screen)
    if(player.postion.y==1080):
        game.game_end()

    meteors.update()
    meteors.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    bg_speed+=dt
    background_y+=dt*speed
    if(background_y==0):background_y=-3600

pygame.quit()

