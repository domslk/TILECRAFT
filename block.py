import pygame
from const import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, CHUNK_SIZE, MAX_CHUNKS, screen
from st import camera_x, camera_y
import st
class Block:
    @staticmethod
    def draw(x_w, y_w, texture = None, color = None):
        screen_x = x_w * BLOCK_SIZE - st.camera_x
        screen_y = y_w * BLOCK_SIZE - st.camera_y
        if texture:
            screen.blit(texture, (screen_x, screen_y))
        elif color:
            pygame.draw.rect(screen, color, pygame.Rect(screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
    @staticmethod
    def draw_on_screen(x, y, texture = None):
        screen.blit(texture, (x, y))

