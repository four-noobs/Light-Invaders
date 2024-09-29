import pygame
def game_end():
    print("you died")

def display_speed(screen, speed):
    font = pygame.font.Font(None, int(screen.get_width() / 21)) 
    
    text = font.render(f"Speed: {speed}", True, (255, 255, 255)) 

    text_rect = text.get_rect(center=(screen.get_width() / 2, 50))  
    
    screen.blit(text, text_rect)
    
def collision(type):
    if type=="slow":
        return -100
    if type=="veryslow":
        return -200
    if type=="fast":
        return 100