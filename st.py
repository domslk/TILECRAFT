import inventory
from inventory_overlay import Inventory_Overlay
from crafting_overlay import Crafting_Overlay
from pause_screen import Pause_Screen
from game import Game
from draw import Draw
from player import Player
from const import screen, BLOCK_SIZE
import pygame

chunks = {} # needed
camera_x = 0 # needed
camera_y = 0 # needed
items_in_inventory = 1 # needed
selection_blit_x = 406 # needed
selection_blit_y = 667 # needed
breaking_block = None



state = "title_screen"
over_singleplayer_button = False
over_play_button = False
over_exit_button = False
over_cancel_button = False
show_inventory_overlay = False
show_crafting_overlay = False


inventory_overlay = Inventory_Overlay(screen)
crafting_overlay = Crafting_Overlay(screen)
pause_screen = Pause_Screen(screen)
game = Game()
draw = Draw()
player = Player()


def get_solid_blocks():
    blocks = []
    for chunk in chunks.values():
        for i in range(18):
            for j in range(32):
                if chunk.grid[i][j] is not None and chunk.grid[i][j] != "flower" and chunk.grid[i][j] != "leaves" and chunk.grid[i][j] != "door":
                    block_rect = pygame.Rect((chunk.w_x + j) * BLOCK_SIZE, (chunk.w_y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    blocks.append(block_rect)
    return blocks
