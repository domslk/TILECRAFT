import pygame
from const import screen, SCREEN_WIDTH, SCREEN_HEIGHT
from draw import Draw
import textures
import const

font = pygame.font.Font('./font.otf', 25)
draw = Draw()

class Pause_Screen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 175))
        self.over_button = False
        self.show_pause_screen = False


    def draw(self):
        if self.show_pause_screen:
            self.screen.blit(self.overlay, (0, 0))
            save_text = font.render(f"Save & Quit to title", True, "Black")
            save_rect = save_text.get_rect()
            save_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 + 75)
            button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 50)
            button_rect = textures.BUTTON.get_rect(topleft=button_pos)
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, "WHITE", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
                self.over_button = True
            else:
                self.over_button = False
            draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 50)
            self.screen.blit(textures.logo, (SCREEN_WIDTH // 2 - 340, SCREEN_HEIGHT // 2 - 200))
            self.screen.blit(save_text, save_rect)
            if not self.show_pause_screen:
                self.over_button = False

            if self.over_button and const.play:
                const.select_sound.play()
                const.play = False
            if not self.over_button:
                const.play = True
