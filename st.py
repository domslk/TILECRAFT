import inventory
from const import BLOCK_SIZE
import pygame
import textures
import os
chunks = {}
camera_x = 0
camera_y = 0
items_in_inventory = 1

if os.path.exists(f'./world.txt'):
    with open('world.txt', 'r') as file:
        lines = file.readlines()
    camera_x = int(lines[4])
    camera_y = int(lines[5])
    items_in_inventory = int(lines[6])
else:
    chunks = {}
    camera_x = 0
    camera_y = 0
    items_in_inventory = 1
selection_blit_x = 406
selection_blit_y = 667
breaking_block = None


state = "title_screen"
over_singleplayer_button = False
over_play_button = False
over_exit_button = False
over_cancel_button = False
over_info_button = False
show_inventory_overlay = False
show_crafting_overlay = False

running = True
player_texture = textures.PLAYER_TEXTURE

item_breaking_const = {  # " what it is " : (break time, item break int minimum) > hand, grass... = 0, pickaxe = 1
        "stone": [1.5, 1],
        "wood": [2, 0],
        "flower": [0.1, 0],
        "leaves": [0.1, 0],
        "grass": [0.3, 0],
        "dirt": [0.3, 0],
        "diamond": [3, 2],
        "plank": [1.5, 0],
        "door": [2, 0],
        "crafting_table": [1.5, 0],
    }

tool_breaking_const = {
    "any": 0,
    "pick": 1
}

def return_pickability(block_type):
    if item_breaking_const[block_type][1] != 0:
        if inventory.inventory_dict[inventory.selected_slot_id][0] == "pick":
            return True
        else:
            return False
    else:
        return True




def get_solid_blocks():
    blocks = []
    for chunk in chunks.values():
        for i in range(18):
            for j in range(32):
                if chunk.grid[i][j] is not None and chunk.grid[i][j] != "flower" and chunk.grid[i][j] != "leaves" and chunk.grid[i][j] != "door":
                    block_rect = pygame.Rect((chunk.w_x + j) * BLOCK_SIZE, (chunk.w_y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    blocks.append(block_rect)
    return blocks
