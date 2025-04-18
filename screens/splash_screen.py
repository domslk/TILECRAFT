import pygame, const
from const import SCREEN_WIDTH, SCREEN_HEIGHT
class Splash_Screen:

    def __init__(self, screen):
        self.show_splash_screen = True
        self.screen = screen
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 100))
    def update(self):
        if self.show_splash_screen:
            pygame.draw.rect(self.screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        #self.screen.blit()