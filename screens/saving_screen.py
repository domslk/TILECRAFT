import pygame
import time
import textures
import st
from const import SCREEN_WIDTH, SCREEN_HEIGHT, screen, font


class Saving_Screen:
    @staticmethod
    def update():
        start_time = time.time()
        rotate = 0
        while time.time() - start_time < 2:
            screen.fill((0, 0, 0))
            if int(time.time() * 2) % 2 == 0:
                rotate += 90
            cd_texture = pygame.transform.rotate(textures.CD_TEXTURE, rotate)
            cd_rect = cd_texture.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(cd_texture, cd_rect)
            saving_text = font.render("SAVING...", True, "White")
            saving_rect = saving_text.get_rect(center=(SCREEN_WIDTH // 2 + 5, SCREEN_HEIGHT // 2))
            screen.blit(saving_text, saving_rect)
            pygame.display.flip()
            if time.time() - start_time > 2:
                st.state = "title_screen"