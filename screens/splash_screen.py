import pygame
class Splash_Screen:

    def __init__(self):
        self.show_splash_screen = False
    def update(self):
        if self.show_splash_screen:
            pygame.draw.rect(screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))