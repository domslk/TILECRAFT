import pygame
import st2
import st
from const import screen, SCREEN_WIDTH, SCREEN_HEIGHT, font
import const
import textures

class Title_Screen():
    def update(self):

        st2.pause_screen.show_pause_screen = False
        st2.pause_screen.over_button = False
        st.over_play_button = False
        st.over_cancel_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and st.over_singleplayer_button:
                    st.state = "world_selection"
                elif event.button == 1 and st.over_exit_button:
                    st.running = False
        pygame.draw.rect(screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        screen.blit(textures.bcg_img, (0, 0))
        screen.blit(textures.logo, (SCREEN_WIDTH // 2 - 340, SCREEN_HEIGHT // 2 - 200))

        singleplayer_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)
        singleplayer_button_rect = textures.BUTTON.get_rect(topleft=singleplayer_button_pos)

        quit_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)
        quit_button_rect = textures.BUTTON.get_rect(topleft=quit_button_pos)

        play_text = font.render(f"singleplayer", True, "Black")
        play_rect = play_text.get_rect()
        play_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)

        quit_text = font.render(f"quit", True, "Black")
        quit_rect = quit_text.get_rect()
        quit_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 125)

        mouse_pos = pygame.mouse.get_pos()
        if singleplayer_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 15, 460, 60))
            st.over_singleplayer_button = True
        else:
            st.over_singleplayer_button = False
        if quit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 95, 460, 60))
            st.over_exit_button = True
        else:
            st.over_exit_button = False



        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)  # play button
        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)  # exit button
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)
