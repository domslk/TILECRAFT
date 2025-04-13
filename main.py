import pygame
import const
from const import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, screen
import st
import textures
from game import Game
import st2

pygame.init()
clock = pygame.time.Clock()
game = Game()





font = pygame.font.Font('./font.otf', 32)




while st.running:
    dt = clock.tick(60) / 1000

    if st.state == "game":
        game.update(dt)

    elif st.state == "title_screen":
        st2.pause_screen.show_pause_screen = False
        st2.pause_screen.over_button = False
        st.over_play_button = False
        st.over_cancel_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and st.over_singleplayer_button:
                    st.state = "world_selection"
                elif event.button == 1 and st.over_exit_button:
                    running = False
        pygame.draw.rect(screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        screen.blit(textures.TILECRAFT, (SCREEN_WIDTH // 2 - 340, SCREEN_HEIGHT // 2 - 200))

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
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            st.over_singleplayer_button = True
        else:
            st.over_singleplayer_button = False
        if quit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            st.over_exit_button = True
        else:
            st.over_exit_button = False

        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)  # play button
        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)  # exit button
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)

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

        play_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)
        play_button_rect = textures.BUTTON.get_rect(topleft=play_button_pos)

        cancel_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)
        cancel_button_rect = textures.BUTTON.get_rect(topleft=cancel_button_pos)

        play_text = font.render(f"Play", True, "Black")
        play_rect = play_text.get_rect()
        play_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)

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

        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)  # play button
        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)  # cancel button -> go to title_screen
        screen.blit(play_text, play_rect)
        screen.blit(cancel_text, cancel_rect)
    pygame.display.flip()
    pygame.display.set_caption("tilecraft")
    #print(st.state)
pygame.quit()