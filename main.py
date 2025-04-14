import pygame
import st
from game import Game
from screens.title_screen import Title_Screen
from screens.world_selection import World_Selection

pygame.init()
clock = pygame.time.Clock()
game = Game()
title_screen = Title_Screen()
world_selection = World_Selection()





font = pygame.font.Font('./font.otf', 32)




while st.running:
    dt = clock.tick(60) / 1000

    if st.state == "game":
        game.update(dt)

    elif st.state == "title_screen":
        title_screen.update()

    elif st.state == "world_selection":
        world_selection.update()
    
    pygame.display.flip()
    pygame.display.set_caption("tilecraft")
pygame.quit()