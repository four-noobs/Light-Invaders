import pygame
class Music:
    def __init__(self) -> None:
        self.meteor=pygame.mixer.Sound('assets/sounds/meteor.wav')
        self.enemy=pygame.mixer.Sound('assets/sounds/enemy_collision.mp3')
        self.speed=pygame.mixer.Sound('assets/sounds/speed_up.wav')
    def game_music(self):
        pygame.mixer.music.load('assets/sounds/bg_music.mp3')
        pygame.mixer.music.play(-1,5,2)
    def end_music(self):
        pygame.mixer.music.load('assets/sounds/end_music.mp3')
        pygame.mixer.music.play(0,5,2)
    def speed_up(self):
        self.speed.play()
    def enemy_sound(self):
        self.enemy.play()
    def meteor_sound(self):
        self.meteor.play()