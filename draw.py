import pygame
from const import BLOCK_SIZE, screen
import st

class Draw:
    @staticmethod
    def draw(texture, x,y):
        if texture:
            screen.blit(texture, (x, y))
