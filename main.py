import time
from threading import Timer
import pygame
import const
from const import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, CHUNK_SIZE, MAX_CHUNKS, screen
from player import Player
import st
from chunk import Chunk
from block import Block
import textures
from inventory_overlay import Inventory_Overlay
from crafting_overlay import Crafting_Overlay
from pause_screen import Pause_Screen
from game import Game
from draw import Draw
import breaking


import inventory


pygame.init()
clock = pygame.time.Clock()
running = True

inventory_overlay = Inventory_Overlay(screen)
crafting_overlay = Crafting_Overlay(screen)
pause_screen = Pause_Screen(screen)
game = Game()
draw = Draw()
player = Player()
player_texture = textures.PLAYER_TEXTURE

state = "title_screen"
over_singleplayer_button = False
over_play_button = False
over_exit_button = False
over_cancel_button = False
show_inventory_overlay = False
show_crafting_overlay = False

font = pygame.font.Font('./font.otf', 32)
dockimg = pygame.image.load('./images/dock.png')
selectionimg = pygame.image.load('./images/selection.png')




def get_solid_blocks():
    blocks = []
    for chunk in st.chunks.values():
        for i in range(18):
            for j in range(32):
                if chunk.grid[i][j] is not None and chunk.grid[i][j] != "flower" and chunk.grid[i][j] != "leaves" and chunk.grid[i][j] != "door":
                    block_rect = pygame.Rect((chunk.w_x + j) * BLOCK_SIZE, (chunk.w_y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    blocks.append(block_rect)
    return blocks

while running:
    dt = clock.tick(60) / 1000


    if state == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_texture = textures.PLAYER2_TEXTURE
                if event.key == pygame.K_a:
                    player_texture = textures.PLAYER_TEXTURE
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                        player.left_button_pressed = False
                if event.key == pygame.K_d:
                    if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                        player.right_button_pressed = False
                if event.key == pygame.K_c and show_inventory_overlay and inventory.selected_slot_id is not None:
                    pass
                if event.key == pygame.K_RETURN:
                    if show_inventory_overlay:
                        inventory_overlay.check_crafting()
                    elif show_crafting_overlay:
                        crafting_overlay.check_crafting()
                    else:
                        pass
                if event.key == pygame.K_e:
                    if not show_crafting_overlay:
                        show_inventory_overlay = not show_inventory_overlay
                if event.key == pygame.K_ESCAPE:
                    if show_crafting_overlay:
                        show_crafting_overlay = not show_crafting_overlay
                    else:
                        pause_screen.show_pause_screen = not pause_screen.show_pause_screen
                if event.key == pygame.K_1:
                    inventory.selected_slot_id = 1
                    st.selection_blit_x = 408
                if event.key == pygame.K_2:
                    inventory.selected_slot_id = 2
                    st.selection_blit_x = 458
                if event.key == pygame.K_3:
                    inventory.selected_slot_id = 3
                    st.selection_blit_x = 510
                if event.key == pygame.K_4:
                    inventory.selected_slot_id = 4
                    st.selection_blit_x = 562
                if event.key == pygame.K_5:
                    inventory.selected_slot_id = 5
                    st.selection_blit_x = 614
                if event.key == pygame.K_6:
                    inventory.selected_slot_id = 6
                    st.selection_blit_x = 666
                if event.key == pygame.K_7:
                    inventory.selected_slot_id = 7
                    st.selection_blit_x = 718
                if event.key == pygame.K_8:
                    inventory.selected_slot_id = 8
                    st.selection_blit_x = 770
                if event.key == pygame.K_9:
                    inventory.selected_slot_id = 9
                    st.selection_blit_x = 822
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                        x, y = event.pos

                        x_w = (x + st.camera_x) // BLOCK_SIZE
                        y_w = (y + st.camera_y) // BLOCK_SIZE

                        ch_x = x_w // 32
                        ch_y = y_w // 18
                        block_x = int(x_w % 32)
                        block_y = int(y_w % 18)

                        try:
                            if inventory.selected_slot_id is None:
                                inventory.selected_slot_id = 1
                            selected_item = inventory.inventory_dict[inventory.selected_slot_id]
                            if selected_item[0] is not None and selected_item[1] > 0 and st.chunks[(ch_x, ch_y)].grid[block_y][block_x] is None:
                                st.chunks[(ch_x, ch_y)].grid[block_y][block_x] = selected_item[0]
                                inventory.inventory_dict[inventory.selected_slot_id][1] -= 1

                                st.items_in_inventory -= 1

                                if inventory.inventory_dict[inventory.selected_slot_id][1] == 0:
                                    inventory.inventory_dict[inventory.selected_slot_id] = [None, 0]
                            elif st.chunks[(ch_x, ch_y)].grid[block_y][block_x] == "crafting_table":
                                show_crafting_overlay = True

                            else:
                                print("block alr there")

                        except IndexError as e:
                            print(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                            """if block_x < 0:
                                ch_x -= 1
                                block_x += 32
                            if block_x >= 32:
                                ch_x += 1
                                block_x -= 32
                            if block_y < 0:
                                ch_y += 1
                                block_y -= 18
                            if block_y >= 18:
                                ch_y -= 1
                                block_y += 18

                            if (ch_x, ch_y) not in st.chunks:
                                st.chunks[(ch_x, ch_y)] = Chunk(ch_x * 32, ch_y * 18)
                                if ch_y > 0:
                                    st.chunks[(ch_x, ch_y)].ground()
                                elif ch_y == 0:
                                    st.chunks[(ch_x, ch_y)].generate()
                                else:
                                    st.chunks[(ch_x, ch_y)].generate_sky()

                            selected_item = inventory.inventory_dict[inventory.selected_slot_id]
                            block_type = selected_item[0]
                            item_count = selected_item[1]
                            if block_type is not None and item_count > 0 and st.chunks[(ch_x, ch_y)].grid[block_y][
                                block_x] is None:
                                st.chunks[(ch_x, ch_y)].grid[block_y][block_x] = block_type
                                inventory.inventory_dict[inventory.selected_slot_id][1] -= 1
                                st.items_in_inventory -= 1
                                if inventory.inventory_dict[inventory.selected_slot_id][1] == 0:
                                    inventory.inventory_dict[inventory.selected_slot_id] = [None, 0]
                            else:
                                print("eror")"""

                if event.button == 1 and not pause_screen.over_button:
                    if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                        x, y = event.pos
                        x_w = (x + st.camera_x) // BLOCK_SIZE
                        y_w = (y + st.camera_y) // BLOCK_SIZE
                        ch_x = x_w // 32
                        ch_y = y_w // 18
                        block_x = int(x_w % 32)
                        block_y = int(y_w % 18)
                        try:
                            if st.chunks[(ch_x, ch_y)].grid[block_y][block_x] is not None:
                                st.breaking_block = (ch_x, ch_y, block_x, block_y, time.time())

                        except (KeyError, IndexError) as e:
                            print("chunk not found")

                        if (ch_x, ch_y) not in st.chunks:
                            st.chunks[(ch_x, ch_y)] = Chunk(ch_x * 32, ch_y * 18)
                            if ch_y > 0:
                                st.chunks[(ch_x, ch_y)].generate_ground()
                            elif ch_y == 0:
                                st.chunks[(ch_x, ch_y)].generate()
                            else:
                                st.chunks[(ch_x, ch_y)].generate_sky()

                    if show_inventory_overlay or show_crafting_overlay:
                        mouse_x, mouse_y = event.pos
                        pressed_key = pygame.key.get_pressed()
                        active_overlay = crafting_overlay if show_crafting_overlay else inventory_overlay
                        for slot_id, (slot_x, slot_y) in active_overlay.x_dict.items():
                            slot_rect = pygame.Rect(slot_x, slot_y, 48, 48)
                            if slot_rect.collidepoint(mouse_x, mouse_y):
                                current_slot_item = inventory.inventory_dict[slot_id]
                                if inventory.selected_slot_id is None:
                                    if current_slot_item[0] is not None:
                                        inventory.selected_slot_id = slot_id
                                else:
                                    if slot_id == inventory.selected_slot_id:
                                        inventory.selected_slot_id = None
                                    else:
                                        held_item = inventory.inventory_dict[inventory.selected_slot_id]
                                        target_item = inventory.inventory_dict[slot_id]
                                        if held_item[0] == target_item[0] and held_item[0] is not None:
                                            combined_int = held_item[1] + target_item[1]

                                            if combined_int <= 64:
                                                inventory.inventory_dict[slot_id] = [held_item[0], combined_int]
                                                inventory.inventory_dict[inventory.selected_slot_id] = [None, 0]

                                            else:
                                                inventory.inventory_dict[slot_id] = [held_item[0], 64]
                                                remaining = combined_int - 64
                                                for new_slot_id, item in inventory.inventory_dict.items():
                                                    if item[0] is None:
                                                        inventory.inventory_dict[new_slot_id] = [held_item[0], remaining]
                                                        break
                                            inventory.inventory_dict[inventory.selected_slot_id] = [None, 0]


                                        if pressed_key[pygame.K_c] and inventory.selected_slot_id is not None:
                                            if held_item[1] > 1:
                                                inventory.inventory_dict[slot_id] = [held_item[0], held_item[1] // 2]
                                                inventory.inventory_dict[inventory.selected_slot_id][1] -= held_item[1] // 2

                                        else:
                                            inventory.inventory_dict[inventory.selected_slot_id], inventory.inventory_dict[slot_id] = (
                                                inventory.inventory_dict[slot_id],
                                                inventory.inventory_dict[inventory.selected_slot_id])

                                        inventory.selected_slot_id = None
                                break
                elif event.button == 1 and pause_screen.over_button and pause_screen.show_pause_screen: # save and quit
                    state = "title_screen"

                    """file = open("world.txt", "w")
                    file.write(f"{player.x_w}\n{player.y_w}\n0\n{player.velocity}\n1\n2\n{player.grounded}\nFalse\nFalse\n{player.colliding}\n{player.x_s}\n{player.y_s}")
                    file.write(f"\n{chunk.grid}\n{chunk.w_x}\n{chunk.w_y}\n{chunk.current_chunk_x}\n{chunk.current_chunk_y}")
                    file.close()"""
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if st.breaking_block is not None:
                        st.breaking_block = None
        try:
            text = font.render(f"{inventory.inventory_dict[inventory.selected_slot_id][0]}", True, "white")
            textRect = text.get_rect()
            textRect.center = (600, 340)
        except KeyError:
            #print("nothing in inventory")
            pass
        mouse_buttons = pygame.mouse.get_pressed()





        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                player.right_button_pressed = True
                player.move_right(dt)
        if keys[pygame.K_a]:
            if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                player.left_button_pressed = True
                player.move_left(dt)
        if keys[pygame.K_SPACE]:
            if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
                player.jump()
        screen.fill("0x7398ff")

        blocks = get_solid_blocks()
        player.update(dt, blocks)


        for chunk in st.chunks.values():
            chunk.render()


        if show_inventory_overlay:
            inventory_overlay.draw()

        elif show_crafting_overlay:
            crafting_overlay.draw()

        elif pause_screen.show_pause_screen:
            pause_screen.draw()



        if not show_inventory_overlay and not show_crafting_overlay and not pause_screen.show_pause_screen:
            Block.draw(x_w=player.x_w, y_w=player.y_w, texture= player_texture)
        screen.blit(dockimg, [406, 665])
        screen.blit(selectionimg, [st.selection_blit_x, st.selection_blit_y])

        for i in range(1, 10):
            if inventory.inventory_dict[i] != [None, 0]:
                try:
                    if inventory.inventory_dict[i][0] == "door":
                        item_texture = textures.ITEM_TEXTURES["door_small"]
                    else:
                        item_texture = textures.ITEM_TEXTURES[inventory.inventory_dict[i][0]]
                    item_texture = pygame.transform.scale(item_texture, (40, 40))
                except Exception:
                    pass
                screen.blit(item_texture, [const.inventory_item_px[i], 672])

                number_of_items = font.render(f"{inventory.inventory_dict[i][1]}", True, "White")
                noi_rect = number_of_items.get_rect()
                noi_rect.topleft = (const.inventory_item_px[i] + 20, 671 + 20)
                screen.blit(number_of_items, noi_rect)
        breaking.update_breaking()

    elif state == "title_screen":
        pause_screen.show_pause_screen = False
        pause_screen.over_button = False
        over_play_button = False
        over_cancel_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and over_singleplayer_button:
                    state = "world_selection"
                elif event.button == 1 and over_exit_button:
                    running = False
        pygame.draw.rect(screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        screen.blit(textures.TILECRAFT, (SCREEN_WIDTH // 2 - 340, SCREEN_HEIGHT // 2 - 200))

        singleplayer_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)
        singleplayer_button_rect = textures.BUTTON.get_rect(topleft=singleplayer_button_pos)

        quit_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)
        quit_button_rect = textures.BUTTON.get_rect(topleft=quit_button_pos)

        play_text = font.render(f"singleplayer", True, "Black")
        play_rect = play_text.get_rect()
        play_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)

        quit_text = font.render(f"quit", True, "Black")
        quit_rect = quit_text.get_rect()
        quit_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 125)

        mouse_pos = pygame.mouse.get_pos()
        if singleplayer_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            over_singleplayer_button = True
        else:
            over_singleplayer_button = False
        if quit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            over_exit_button = True
        else:
            over_exit_button = False

        draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)  # play button
        draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)  # exit button
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)

    elif state == "world_selection":
        over_singleplayer_button = False
        over_exit_button = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and over_play_button:
                    state = "game"
                elif event.button == 1 and over_cancel_button:
                    state = "title_screen"
        pygame.draw.rect(screen, "white", pygame.Rect(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        screen.blit(textures.TILECRAFT, (SCREEN_WIDTH // 2 - 340, SCREEN_HEIGHT // 2 - 200))

        play_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)
        play_button_rect = textures.BUTTON.get_rect(topleft=play_button_pos)

        cancel_button_pos = (SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)
        cancel_button_rect = textures.BUTTON.get_rect(topleft=cancel_button_pos)

        play_text = font.render(f"Play", True, "Black")
        play_rect = play_text.get_rect()
        play_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 45)

        cancel_text = font.render(f"cancel", True, "Black")
        cancel_rect = cancel_text.get_rect()
        cancel_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 125)

        mouse_pos = pygame.mouse.get_pos()
        if play_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            over_play_button = True
        else:
            over_play_button = False
        if cancel_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "black", pygame.Rect(SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 45, 460, 60))
            over_cancel_button = True
        else:
            over_cancel_button = False

        draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 20)  # play button
        draw.draw(textures.BUTTON, SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2 + 100)  # cancel button -> go to title_screen
        screen.blit(play_text, play_rect)
        screen.blit(cancel_text, cancel_rect)
    pygame.display.flip()
    pygame.display.set_caption("tilecraft")

pygame.quit()