import time

import pygame

import inventory
import st
import st2
from const import SCREEN_WIDTH, SCREEN_HEIGHT, screen, font
import const
import textures
import os
hover = False

class World_Selection:
    @staticmethod
    def update():
        st.over_singleplayer_button = False
        st.over_exit_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and st.over_play_button:
                    st.state = "game"
                elif event.button == 1 and st.over_cancel_button:
                    st.state = "title_screen"
                elif event.button == 1 and st.over_info_button:
                    st.state = "info_screen"




        screen.blit(textures.bcg_img, (0, 0))
        #### BUTTON COLLIDERS ###
        play_button_pos = (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 280)
        play_button_rect = textures.BUTTON.get_rect(topleft=play_button_pos)

        cancel_button_pos = (SCREEN_WIDTH // 2 - 600, SCREEN_HEIGHT // 2 + 280)
        cancel_button_rect = textures.BUTTON.get_rect(topleft=cancel_button_pos)

        info_button_pos = (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 220)
        info_button_rect = textures.BUTTON.get_rect(topleft=info_button_pos)
        ######################

        #### BUTTON TEXTS ####
        play_text = font.render(f"play world", True, "Black")
        play_rect = play_text.get_rect()
        play_rect.center = (SCREEN_WIDTH // 2 + 320, SCREEN_HEIGHT // 2 + 305)

        cancel_text = font.render(f"cancel", True, "Black")
        cancel_rect = cancel_text.get_rect()
        cancel_rect.center = (SCREEN_WIDTH // 2 - 380, SCREEN_HEIGHT // 2 + 305)

        info_text = font.render(f"Info", True, "Black")
        info_rect = info_text.get_rect()
        info_rect.center = (SCREEN_WIDTH // 2 + 315, SCREEN_HEIGHT // 2 + 245)
        ######################

        mouse_pos = pygame.mouse.get_pos()
        if play_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 + 95, SCREEN_HEIGHT // 2 + 275, 460, 60))
            st.over_play_button = True
        else:
            st.over_play_button = False
        if cancel_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 605, SCREEN_HEIGHT // 2 + 275, 460, 60))
            st.over_cancel_button = True
        else:
            st.over_cancel_button = False
        if info_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 + 95, SCREEN_HEIGHT // 2 + 215, 460, 60))
            st.over_info_button = True
        else:
            st.over_info_button = False
        ###### buttron drawing #####

        if (st.over_play_button or st.over_cancel_button or st.over_info_button) and const.play:
            const.select_sound.play()
            const.play = False
        elif not (st.over_play_button or st.over_cancel_button or st.over_info_button):
            const.play = True

        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 280)  # play button
        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 600,
                      SCREEN_HEIGHT // 2 + 280)  # cancel button -> go to title_screen
        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 220)  # create world button

        ##################################

        screen.blit(play_text, play_rect)
        screen.blit(cancel_text, cancel_rect)
        screen.blit(info_text, info_rect)
