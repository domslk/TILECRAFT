import random
import math
import pygame
from block import Block
from st import chunks
from const import BLOCK_SIZE
import textures
class Chunk:
    global camera_x
    def __init__(self, w_x, w_y):
        self.grid = [[None for _ in range(32)] for _ in range(18)]
        self.w_x = w_x
        self.w_y = w_y
        self.current_chunk_x = self.w_x // 32
        self.current_chunk_y = self.w_y // 18
    def generate_tree(self, i, j):

        if i < 4 or  i >= 18 or j < 2 or j >= 30:
            return

        self.grid[i][j] = "wood"
        self.grid[i-1][j] = "wood"
        self.grid[i-2][j] = "leaves"
        self.grid[i - 2][j+1] = "leaves"
        self.grid[i - 2][j-1] = "leaves"
        self.grid[i - 2][j + 2] = "leaves"
        self.grid[i - 2][j - 2] = "leaves"
        self.grid[i - 3][j+1] = "leaves"
        self.grid[i - 3][j-1] = "leaves"
        self.grid[i-3][j] = "leaves"
        self.grid[i-4][j] = "leaves"


    def generate(self):
        amplitude = random.randint(2,4) ## visina
        freq = random.uniform(0.1, 0.2)
        base = random.randint(6,10)
        for j in range(32):
            height = base + int(math.sin((self.w_x + j) * freq) * amplitude)
            for i in range(len(self.grid)):
                if i >= height + 3:
                    self.grid[i][j] = "stone"
                elif height <= i < height + 3:
                    self.grid[i][j] = "dirt"
                elif i == height - 1:
                    self.grid[i][j] = "grass"
                elif i == height - 2 and random.random() < 0.1 and height < 14:
                    if 4 <= i <= 12 and 2 <= j <= 29:
                        self.generate_tree(i,j)
                elif i == height - 2 and random.random() < 0.1:
                    self.grid[i][j] = "flower"


    def generate_ground(self):
        for j in range(32):
            for i in range(len(self.grid)):
                self.grid[i][j] = "stone"
    def generate_sky(self):
        for j in range(32):
            for i in range(len(self.grid)):
                self.grid[i][j] = None

    def get_solid_blocks(self):
        blocks = []
        for chunk in chunks.values():
            for i in range(32):
                for j in range(18):
                    if chunk.grid[i][j] is not None:
                        block_rect = pygame.Rect(chunk.w_x * BLOCK_SIZE, chunk.w_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                        blocks.append(block_rect)
        return blocks


    def render(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is not None:
                    Block.draw(j + self.w_x , i + self.w_y , texture = textures.ITEM_TEXTURES[self.grid[i][j]])



