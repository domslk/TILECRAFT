import pygame
from const import BLOCK_SIZE, BUTTON_SIZE_X, BUTTON_SIZE_Y
STONE_TEXTURE = pygame.image.load("./images/stone.png").convert()
STONE_TEXTURE = pygame.transform.scale(STONE_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
GRASS_TEXTURE = pygame.image.load("./images/grass.png").convert()
GRASS_TEXTURE = pygame.transform.scale(GRASS_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
DIRT_TEXTURE = pygame.image.load("./images/dirt.png").convert()
DIRT_TEXTURE = pygame.transform.scale(DIRT_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
PLAYER_TEXTURE = pygame.image.load("./images/player.png").convert_alpha()
PLAYER_TEXTURE = pygame.transform.scale(PLAYER_TEXTURE, (50, 100))
PLAYER2_TEXTURE = pygame.image.load("./images/player2.png").convert_alpha()
PLAYER2_TEXTURE = pygame.transform.scale(PLAYER2_TEXTURE, (50, 100))
FLOWER_TEXTURE = pygame.image.load("./images/flower.png").convert_alpha()
FLOWER_TEXTURE = pygame.transform.scale(FLOWER_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
WOOD_TEXTURE = pygame.image.load("./images/wood.png").convert()
WOOD_TEXTURE = pygame.transform.scale(WOOD_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
LEAVES_TEXTURE = pygame.image.load("./images/leaves.png").convert_alpha()
LEAVES_TEXTURE = pygame.transform.scale(LEAVES_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
PLANK_TEXTURE = pygame.image.load("./images/plank.png").convert_alpha()
PLANK_TEXTURE = pygame.transform.scale(PLANK_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
DOOR_TEXTURE = pygame.image.load("./images/door.png").convert_alpha()
DOOR_TEXTURE = pygame.transform.scale(DOOR_TEXTURE, (BLOCK_SIZE, 100))
CRAFTING_TABLE_TEXTURE = pygame.image.load("./images/crafting_table.png").convert_alpha()
CRAFTING_TABLE_TEXTURE = pygame.transform.scale(CRAFTING_TABLE_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
DOOR_SMALL_TEXTURE = pygame.image.load("./images/door_small.png").convert_alpha()
DOOR_SMALL_TEXTURE = pygame.transform.scale(DOOR_SMALL_TEXTURE, (50, 50))
BREAK_1_TEXTURE = pygame.image.load("./images/break1.png").convert_alpha()
BREAK_1_TEXTURE = pygame.transform.scale(BREAK_1_TEXTURE, (50, 50))
BREAK_2_TEXTURE = pygame.image.load("./images/break2.png").convert_alpha()
BREAK_2_TEXTURE = pygame.transform.scale(BREAK_2_TEXTURE, (50, 50))
BREAK_3_TEXTURE = pygame.image.load("./images/break3.png").convert_alpha()
BREAK_3_TEXTURE = pygame.transform.scale(BREAK_3_TEXTURE, (50, 50))
BREAK_4_TEXTURE = pygame.image.load("./images/break4.png").convert_alpha()
BREAK_4_TEXTURE = pygame.transform.scale(BREAK_4_TEXTURE, (50, 50))
BUTTON = pygame.image.load("./images/button.png").convert_alpha()
BUTTON = pygame.transform.scale(BUTTON, (BUTTON_SIZE_X, BUTTON_SIZE_Y))
TILECRAFT = pygame.image.load("./images/tilecraft.png").convert_alpha()
TILECRAFT = pygame.transform.scale(TILECRAFT, (700, 150))
ENTER = pygame.image.load("./images/enter.png").convert_alpha()
ENTER = pygame.transform.scale(ENTER, (50, 50))
dockimg = pygame.image.load('./images/dock.png')
selectionimg = pygame.image.load('./images/selection.png')
bcg_img = pygame.image.load('./images/bcg.png')
logo = pygame.image.load("./images/logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (700, 150))
DIAMOND_TEXTURE = pygame.image.load("./images/diamond.png").convert()
DIAMOND_TEXTURE = pygame.transform.scale(DIAMOND_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
PICK_TEXTURE = pygame.image.load("./images/pick.png").convert_alpha()
PICK_TEXTURE = pygame.transform.scale(PICK_TEXTURE, (BLOCK_SIZE, BLOCK_SIZE))
DIAMOND_SMALL_TEXTURE = pygame.image.load("./images/diamond_small.png").convert_alpha()
DIAMOND_SMALL_TEXTURE = pygame.transform.scale(DIAMOND_SMALL_TEXTURE, (50, 50))
STICK_TEXTURE = pygame.image.load("./images/stick.png").convert_alpha()
STICK_TEXTURE = pygame.transform.scale(STICK_TEXTURE, (50, 50))
WOOD_PICKAXE_TEXTURE = pygame.image.load("./images/wood_pickaxe.png").convert_alpha()
WOOD_PICKAXE_TEXTURE = pygame.transform.scale(WOOD_PICKAXE_TEXTURE, (50, 50))
STONE_PICKAXE_TEXTURE = pygame.image.load("./images/stone_pickaxe.png").convert_alpha()
STONE_PICKAXE_TEXTURE = pygame.transform.scale(STONE_PICKAXE_TEXTURE, (50, 50))
IRON_TEXTURE = pygame.image.load("./images/iron.png").convert_alpha()
IRON_TEXTURE = pygame.transform.scale(IRON_TEXTURE, (50, 50))
IRON_SMALL_TEXTURE = pygame.image.load("./images/iron_small.png").convert_alpha()
IRON_SMALL_TEXTURE = pygame.transform.scale(IRON_SMALL_TEXTURE, (50, 50))
IRON_PICKAXE_TEXTURE = pygame.image.load("./images/iron_pickaxe.png").convert_alpha()
IRON_PICKAXE_TEXTURE = pygame.transform.scale(IRON_PICKAXE_TEXTURE, (50, 50))
DIAMOND_PICKAXE_TEXTURE = pygame.image.load("./images/diamond_pickaxe.png").convert_alpha()
DIAMOND_PICKAXE_TEXTURE = pygame.transform.scale(DIAMOND_PICKAXE_TEXTURE, (50, 50))
BEDROCK_TEXTURE = pygame.image.load("./images/bedrock.png").convert()
BEDROCK_TEXTURE = pygame.transform.scale(BEDROCK_TEXTURE, (50, 50))



ITEM_TEXTURES = {
    "stone": STONE_TEXTURE,
    "grass": GRASS_TEXTURE,
    "dirt": DIRT_TEXTURE,
    "flower": FLOWER_TEXTURE,
    "wood": WOOD_TEXTURE,
    "leaves": LEAVES_TEXTURE,
    "plank": PLANK_TEXTURE,
    "door": DOOR_TEXTURE,
    "crafting_table": CRAFTING_TABLE_TEXTURE,
    "door_small": DOOR_SMALL_TEXTURE,
    "BREAK_1_TEXTURE": BREAK_1_TEXTURE,
    "BREAK_2_TEXTURE": BREAK_2_TEXTURE,
    "BREAK_3_TEXTURE": BREAK_3_TEXTURE,
    "BREAK_4_TEXTURE": BREAK_4_TEXTURE,
    "diamond": DIAMOND_TEXTURE,
    "pick": PICK_TEXTURE,
    "diamond_small": DIAMOND_SMALL_TEXTURE,
    "stick": STICK_TEXTURE,
    "wood_pickaxe": WOOD_PICKAXE_TEXTURE,
    "stone_pickaxe": STONE_PICKAXE_TEXTURE,
    "iron": IRON_TEXTURE,
    "iron_small": IRON_SMALL_TEXTURE,
    "iron_pickaxe": IRON_PICKAXE_TEXTURE,
    "diamond_pickaxe": DIAMOND_PICKAXE_TEXTURE,
    "bedrock": BEDROCK_TEXTURE

}
