import pygame

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLOCK_SIZE = 50
CHUNK_SIZE = 32
screen = pygame.display.set_mode((1280, 720))
inventory_item_px = {1: 412, 2: 463, 3: 515, 4: 567, 5: 619, 6: 671, 7: 723, 8: 775, 9: 827}
breaking_block_overlay = {1: (0.25, "BREAK_1_TEXTURE"), 2: (0.50, "BREAK_2_TEXTURE"), 3: (0.75, "BREAK_3_TEXTURE"), 4: (1, "BREAK_4_TEXTURE")}
BUTTON_SIZE_X = 450
BUTTON_SIZE_Y = 50
font = pygame.font.Font('./font.otf', 32)
select_sound = pygame.mixer.Sound("./sounds/select.mp3")
play = True
