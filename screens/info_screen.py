import pygame
import st2
import st
from const import screen, SCREEN_WIDTH, SCREEN_HEIGHT, font
import const
import textures

class Info_Screen():
    @staticmethod
    def update():
        st.over_cancel_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and st.over_cancelinfo_button:
                    st.state = "title_screen"
        pygame.draw.rect(screen, "white", pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(textures.bcg_img, (0, 0))

        infotxt = [
            "TILECRAFT",
            "A fun interactive game where you get to explore the 2D world,",
            "craft and build anything you want!",
            "Game made by Domen",
            "Crafting recepies can be found in README.txt",
            "Special thanks to Crt, Anze, Jacob and Svit for playtesting.",

        ]
        y_offset = 100
        for i in range(len(infotxt)):
            line = infotxt[i]
            text = font.render(line, True, "white")
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y_offset + i * 40))

        cancel_button_pos = (SCREEN_WIDTH // 2 - 600, SCREEN_HEIGHT // 2 + 280)
        cancel_button_rect = textures.BUTTON.get_rect(topleft=cancel_button_pos)

        cancel_text = font.render("Cancel", True, "Black")
        cancel_text_rect = cancel_text.get_rect()
        cancel_text_rect.center = (SCREEN_WIDTH // 2 - 380, SCREEN_HEIGHT // 2 + 305)

        mouse_pos = pygame.mouse.get_pos()
        if cancel_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 605, SCREEN_HEIGHT // 2 + 275, 460, 60))
            st.over_cancelinfo_button = True
        else:
            st.over_cancelinfo_button = False

        if st.over_cancel_button and const.play:
            const.select_sound.play()
            const.play = False
        elif not st.over_cancel_button:
            const.play = True

        st2.draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 600, SCREEN_HEIGHT // 2 + 280)
        screen.blit(cancel_text, cancel_text_rect)
