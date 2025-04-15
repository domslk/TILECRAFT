from const import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, CHUNK_SIZE, MAX_CHUNKS
from st import chunks
import st
import pygame
from chunk import Chunk
import os


class Player:
    def __init__(self):
        if os.path.exists(f'./world.txt'):
            with open('./world.txt', 'r') as file:
                lines = file.readlines()
            self.x_w = int(lines[0].strip())
            self.y_w = int(lines[1].strip())
            self.velocity = int(lines[2].strip())
            self.grounded = lines[3].strip() == "True"
            self.speed = 3
            self.width = 1
            self.height = 2
            self.right_button_pressed = False
            self.left_button_pressed = False
            self.colliding = False
            self.x_s = self.x_w * BLOCK_SIZE
            self.y_s = self.y_w * BLOCK_SIZE
        else:
            self.x_w = 16
            self.y_w = 0
            self.speed = 3
            self.velocity = 0
            self.width = 1
            self.height = 2
            self.grounded = False
            self.right_button_pressed = False
            self.left_button_pressed = False
            self.colliding = False
            self.x_s = self.x_w * BLOCK_SIZE
            self.y_s = self.y_w * BLOCK_SIZE

    def get_rect(self):
        return pygame.Rect(self.x_w * BLOCK_SIZE, self.y_w * BLOCK_SIZE, self.width * BLOCK_SIZE, self.height * BLOCK_SIZE)

    def jump(self):
        if self.grounded:
            self.velocity = -8.5
            self.grounded = False

    def move_right(self, dt):
        self.x_w += self.speed * dt

    def move_left(self, dt):
        self.x_w -= self.speed * dt
    def generate_chunk(self):
        chunk_x = int(self.x_w // 32)
        chunk_y = int(self.y_w // 18)
        print(self.x_w)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                cx = chunk_x + dx
                cy = chunk_y + dy
                if (cx, cy) not in chunks:
                    chunks[(cx, cy)] = Chunk(cx * 32, cy * 18)
                    if cy > 0 and not chunk_y == 3:
                        chunks[(cx, cy)].generate_ground()
                    elif cy == 0:
                        chunks[(cx, cy)].generate()
                    else:
                        chunks[(cx, cy)].generate_sky()


    def update(self, dt, blocks_list):
        self.generate_chunk()
        old_x_w = self.x_w
        if self.right_button_pressed:
            self.move_right(dt)
        if self.left_button_pressed:
            self.move_left(dt)

        player_rect = self.get_rect()
        for block in blocks_list:
            if player_rect.colliderect(block):
                if self.x_w > old_x_w:
                    self.x_w = (block.left / BLOCK_SIZE) - self.width
                elif self.x_w < old_x_w:
                    self.x_w = (block.right / BLOCK_SIZE)
                player_rect = self.get_rect()

        self.velocity += 18 * dt
        self.y_w += self.velocity * dt
        player_rect = self.get_rect()
        self.grounded = False

        for block in blocks_list:
            if player_rect.colliderect(block):
                if self.velocity > 0:
                    if chunk_y < 0:
                        self.y_w = (block.top / BLOCK_SIZE) - self.height
                    else:
                        self.y_w = (block.top / BLOCK_SIZE) - self.height+ 0.01
                    self.velocity = 0
                    self.grounded = True
                elif self.velocity < 0:
                    self.y_w = (block.bottom / BLOCK_SIZE)
                    self.velocity = 0
                player_rect = self.get_rect()

        st.camera_x = self.x_w * BLOCK_SIZE - SCREEN_WIDTH // 2
        st.camera_y = self.y_w * BLOCK_SIZE - SCREEN_HEIGHT + 320