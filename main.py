import pygame, math, sys, random
from player import Player
from meteor import clsmeteor
from enemy import clsenemy
from projectile import projectile 
from game import *
from speed_orb import Speed_orb
from music import Music


def play():
    # pygame setup
    max_speed=500
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running=True
    dt = 0
    bg_speed=100
    background_y=-3600
    background=pygame.image.load('assets/images/background.png')
    music.game_music()
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
    
    blackhole_speed = 0
    max_wobble = 5
    direction = 0.2
    blackhole_bottom = pygame.image.load("assets/images/blackhole_bottom.png").convert_alpha()
    blackhole_top = pygame.image.load("assets/images/blackhole_top.png").convert_alpha()

    blackhole_bottom_scaled = pygame.transform.scale(blackhole_bottom, (screen_width, screen_height / 18))
    blackhole_top_scaled = pygame.transform.scale(blackhole_top, (screen_width, screen_height / 30))
    blackhole_bottom_y = screen_height - blackhole_bottom_scaled.get_height()
    blackhole_top_y = blackhole_bottom_y - blackhole_top_scaled.get_height()
    blackhole_bottom_x = 0
    blackhole_top_x = 0

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
        
        blackhole_speed += direction
        if (blackhole_speed > max_wobble or blackhole_speed < -max_wobble):
            direction = -direction
            if (blackhole_speed > 0):
                blackhole_speed -= 2
            else:
                blackhole_speed += 2
                

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(background,(0,background_y))

        blackhole_bottom_x += blackhole_speed
        blackhole_top_x += blackhole_speed

        screen.blit(blackhole_top_scaled, (blackhole_top_x, blackhole_top_y)) 

        player.handle_input(dt)
        player.position.y+=dt*bg_speed
        player.draw(screen)

        if(player.position.y>screen_height-screen_height/18+screen_height/56):
            running = False
            music.end_music()
            return max_speed

        speed_orbs.update(bg_speed*dt)
        speed_orbs.draw(screen)
        
        meteors.update(bg_speed*dt)
        meteors.draw(screen)
        hit_meteor = pygame.sprite.spritecollide(player, meteors, True)
        if hit_meteor:
            player.speed=max(0,player.speed+collision('slow')) 
            max_speed=max(player.speed,max_speed)
            music.meteor_sound()
        hit_enemy = pygame.sprite.spritecollide(player, enemies, True)
        if hit_enemy:
            player.speed=max(0,player.speed+collision('slow')) 
            max_speed=max(player.speed,max_speed)
            music.enemy_sound()
        hit_orb = pygame.sprite.spritecollide(player, speed_orbs, True)
        if hit_orb:
            player.speed+= collision('fast')
            max_speed=max(player.speed,max_speed)
            music.speed_up()

        hit_projectile = pygame.sprite.spritecollide(player, projectiles, True)
        if hit_projectile:
            player.speed=max(0,player.speed+collision('slow'))
            max_speed=max(player.speed,max_speed)
            music.enemy_sound()

        enemies.update(bg_speed * dt)
        enemies.draw(screen)

        projectiles.update(bg_speed*dt)
        projectiles.draw(screen)

        
        display_speed(screen, player.speed)
        
        screen.blit(blackhole_bottom_scaled, (blackhole_bottom_x, blackhole_bottom_y))
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        bg_speed+=dt
        background_y+=dt*bg_speed
        if(background_y>=0):background_y=-3600


pygame.init()
highscore = 0
music=Music()
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
music.end_music()
background=pygame.image.load('assets/images/background.png')
font = pygame.font.Font(None, 74)
white = (255, 255, 255)
black = (0, 0, 0)
testcolour = (11, 219, 53)
lightcream = (255, 253, 208)
darkcream = (255,241,208)
speedtxt = font.render(f"Your highscore is {highscore}.",True, lightcream)
Gameovertxt = font.render("Game Over", True, black)
Playtxt = font.render("Play", True, black)
play_button = pygame.Rect(screen_width // 2 - 60, screen_height // 2, 120, 70)
Exittxt = font.render("Exit", True, black)
exit_button = pygame.Rect(screen_width // 2 - 60, screen_height // 2 + 80, 120, 70)

while True: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button.collidepoint(mouse_pos):
                    speed = play()
                    if speed > highscore:
                        highscore = speed
                    speedtxt = font.render(f"Your speed was {speed} and your high score is {highscore}", True, black)
                    screen.blit(Gameovertxt, (screen_width // 2 - Gameovertxt.get_width() // 2, screen_height // 2 - Gameovertxt.get_height() // 2 - 50))
                    
                if exit_button.collidepoint(mouse_pos):
                    
                    f = open("highscore.txt", "w")
                    f.write(highscore)
                    f.close()

                    pygame.quit()
                    sys.exit()

    screen.blit(background,(0,-3600))
    screen.blit(speedtxt, (screen_width // 2 - speedtxt.get_width() // 2, screen_height // 2 - speedtxt.get_height() // 2 - 150))

    pygame.draw.rect(screen, darkcream, play_button)
    screen.blit(Playtxt, (play_button.x + 10, play_button.y + 10))

    pygame.draw.rect(screen, darkcream, exit_button)
    screen.blit(Exittxt, (exit_button.x + 10, exit_button.y + 10)) 

    pygame.display.flip()
    