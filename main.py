import pygame
import const
from const import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, screen
import st
import textures
from game import Game
import st2
from title_screen import Title_Screen

pygame.init()
clock = pygame.time.Clock()
game = Game()
title_screen = Title_Screen()





font = pygame.font.Font('./font.otf', 32)




while st.running:
    dt = clock.tick(60) / 1000

    if st.state == "game":
        game.update(dt)

    elif st.state == "title_screen":
        title_screen.update()

    elif st.state == "world_selection":
        st.over_singleplayer_button = False
        st.over_exit_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and st.over_play_button:
                    st.state = "game"
                elif event.button == 1 and st.over_cancel_button:
                    st.state = "title_screen"
        pygame.draw.rect(screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        screen.blit(textures.TILECRAFT, (SCREEN_WIDTH // 2 - 340, SCREEN_HEIGHT // 2 - 200))

        play_button_pos = (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 280)
        play_button_rect = textures.BUTTON.get_rect(topleft=play_button_pos)

        cancel_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)
        cancel_button_rect = textures.BUTTON.get_rect(topleft=cancel_button_pos)

        play_text = font.render(f"play world", True, "Black")
        play_rect = play_text.get_rect()
        play_rect.center = (SCREEN_WIDTH // 2 + 320, SCREEN_HEIGHT // 2 + 305)

        cancel_text = font.render(f"cancel", True, "Black")
        cancel_rect = cancel_text.get_rect()
        cancel_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 125)

        mouse_pos = pygame.mouse.get_pos()
        if play_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            st.over_play_button = True
        else:
            st.over_play_button = False
        if cancel_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            st.over_cancel_button = True
        else:
            st.over_cancel_button = False

        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 280)  # play button
        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)  # cancel button -> go to title_screen
        screen.blit(play_text, play_rect)
        screen.blit(cancel_text, cancel_rect)
    pygame.display.flip()
    pygame.display.set_caption("tilecraft")
    print(st.state)
pygame.quit()