import pygame
import st
import load_inventory, inventory
from game import Game
from screens.title_screen import Title_Screen
from screens.world_selection import World_Selection
import st2


pygame.init()
clock = pygame.time.Clock()
game = Game()
title_screen = Title_Screen()
world_selection = World_Selection()
font = pygame.font.Font('./font.otf', 32)
loaded = False
while st.running:
    dt = clock.tick(60) / 1000
    if st.state == "game":
        game.update(dt)
        if loaded is not True:
            load_inventory.load_inventory()
            loaded = True
    elif st.state == "title_screen":
        title_screen.update()
    elif st.state == "world_selection":
        world_selection.update()
    elif st.state == "info_screen":
        st2.info_screen.update()
    elif st.state == "saving_screen":
        st2.saving_screen.update()
    pygame.display.flip()
    pygame.display.set_caption("tilecraft")
pygame.quit()