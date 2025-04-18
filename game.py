import time
from threading import Timer
import pygame
import const
from const import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, CHUNK_SIZE, MAX_CHUNKS, screen
import player
import load_inventory

import st
from chunk import Chunk
from block import Block
import textures
import inventory
import st2

import breaking
font = pygame.font.Font('./font.otf', 32)


class Game:
    @staticmethod
    def update(dt):
        unplacable = ['pick', 'diamond', 'stick', 'wood_pickaxe', 'stone_pickaxe', 'iron', 'iron_pickaxe', 'diamond_pickaxe']
        def save_chunks():
            with open('./world.txt', 'a') as file:
                for (ch_x, ch_y), chunk in st.chunks.items():
                    file.write(f'\nCHUNK {ch_x} {ch_y}\n')
                    grid_str = repr(chunk.grid)
                    file.write(grid_str + '\n')
        def save_inventory():
            with open('./world.txt', 'a') as file:
                file.write('\nINVENTORY\n')
                file.write(repr(inventory.inventory_dict) + '\n')




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    st.player_texture = textures.PLAYER2_TEXTURE
                if event.key == pygame.K_a:
                    st.player_texture = textures.PLAYER_TEXTURE
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
                        st2.player.left_button_pressed = False
                if event.key == pygame.K_d:
                    if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
                        st2.player.right_button_pressed = False
                if event.key == pygame.K_c and st.show_inventory_overlay and inventory.selected_slot_id is not None:
                    pass
                if event.key == pygame.K_RETURN:
                    if st.show_inventory_overlay:
                        st2.inventory_overlay.check_crafting()
                    elif st.show_crafting_overlay:
                        st2.crafting_overlay.check_crafting()
                    else:
                        pass
                if event.key == pygame.K_e:
                    if not st.show_crafting_overlay:
                        st.show_inventory_overlay = not st.show_inventory_overlay
                if event.key == pygame.K_ESCAPE:
                    if st.show_crafting_overlay:
                        st.show_crafting_overlay = not st.show_crafting_overlay
                    else:
                        st2.pause_screen.show_pause_screen = not st2.pause_screen.show_pause_screen
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
                    if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
                        x, y = event.pos

                        x_w = (x + st.camera_x) // BLOCK_SIZE
                        y_w = (y + st.camera_y) // BLOCK_SIZE

                        ch_x = x_w // 32
                        ch_y = y_w // 18
                        block_x = int(x_w % 32)
                        block_y = int(y_w % 18)

                        try:
                            if inventory.inventory_dict[inventory.selected_slot_id][0] not in unplacable:
                                if inventory.selected_slot_id is None:
                                    inventory.selected_slot_id = 1
                                selected_item = inventory.inventory_dict[inventory.selected_slot_id]
                                if selected_item[0] is not None and selected_item[1] > 0 and st.chunks[(ch_x, ch_y)].grid[block_y][
                                    block_x] is None:
                                    st.chunks[(ch_x, ch_y)].grid[block_y][block_x] = selected_item[0]
                                    inventory.inventory_dict[inventory.selected_slot_id][1] -= 1

                                    st.items_in_inventory -= 1

                                    if inventory.inventory_dict[inventory.selected_slot_id][1] == 0:
                                        inventory.inventory_dict[inventory.selected_slot_id] = [None, 0]

                                else:
                                    if st.chunks[(ch_x, ch_y)].grid[block_y][block_x] == "crafting_table":
                                        st.show_crafting_overlay = True
                                    print("block alr there")
                            else:
                                if st.chunks[(ch_x, ch_y)].grid[block_y][block_x] == "crafting_table":
                                    st.show_crafting_overlay = True

                        except KeyError:
                            print("key error with placing blocks")

                if event.button == 1 and not st2.pause_screen.over_button:
                    if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
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

                    if st.show_inventory_overlay or st.show_crafting_overlay:
                        mouse_x, mouse_y = event.pos
                        pressed_key = pygame.key.get_pressed()
                        active_overlay = st2.crafting_overlay if st.show_crafting_overlay else st2.inventory_overlay
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
                                            inventory.inventory_dict[inventory.selected_slot_id], inventory.inventory_dict[
                                                slot_id] = (
                                                inventory.inventory_dict[slot_id],
                                                inventory.inventory_dict[inventory.selected_slot_id])

                                        inventory.selected_slot_id = None
                                break
                elif event.button == 1 and st2.pause_screen.over_button and st2.pause_screen.show_pause_screen:  # save and quit
                    st.state = "title_screen"
                    with open('./world.txt', 'w') as file:
                        file.write(f"{int(st2.player.x_w)}\n{int(st2.player.y_w)}\n{int(st2.player.velocity)}\n{int(st2.player.grounded)}\n{int(st.camera_x)}\n{int(st.camera_y)}\n{int(st.items_in_inventory)}")
                        file.close()
                    save_chunks()
                    save_inventory()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if st.breaking_block is not None:
                        st.breaking_block = None
        try:
            text = font.render(f"{inventory.inventory_dict[inventory.selected_slot_id][0]}", True, "white")
            textRect = text.get_rect()
            textRect.center = (600, 340)
        except KeyError:
            # print("nothing in inventory")
            pass
        mouse_buttons = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
                st2.player.right_button_pressed = True
                st2.player.move_right(dt)
        if keys[pygame.K_a]:
            if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
                st2.player.left_button_pressed = True
                st2.player.move_left(dt)
        if keys[pygame.K_SPACE]:
            if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
                st2.player.jump()
        screen.fill("0x7398ff")

        blocks = st.get_solid_blocks()
        st2.player.update(dt, blocks)

        for chunk in st.chunks.values():
            chunk.render()

        if st.show_inventory_overlay:
            st2.inventory_overlay.draw()

        elif st.show_crafting_overlay:
            st2.crafting_overlay.draw()

        elif st2.pause_screen.show_pause_screen:
            st2.pause_screen.draw()

        if not st.show_inventory_overlay and not st.show_crafting_overlay and not st2.pause_screen.show_pause_screen:
            Block.draw(x_w=st2.player.x_w, y_w=st2.player.y_w, texture=st.player_texture) # PLAYER DRAW
        if not st2.pause_screen.show_pause_screen:
            screen.blit(textures.dockimg, [406, 665])
            screen.blit(textures.selectionimg, [st.selection_blit_x, st.selection_blit_y])

        for i in range(1, 10):
            if inventory.inventory_dict[i] != [None, 0]:
                try:
                    if inventory.inventory_dict[i][0] == "door":
                        item_texture = textures.ITEM_TEXTURES["door_small"]
                    elif inventory.inventory_dict[i][0] == "diamond":
                        item_texture = textures.ITEM_TEXTURES["diamond_small"]
                    elif inventory.inventory_dict[i][0] == "iron":
                        item_texture = textures.ITEM_TEXTURES["iron_small"]
                    else:
                        item_texture = textures.ITEM_TEXTURES[inventory.inventory_dict[i][0]]
                    item_texture = pygame.transform.scale(item_texture, (40, 40))
                except Exception:
                    pass
                if not st2.pause_screen.show_pause_screen:
                    screen.blit(item_texture, [const.inventory_item_px[i], 672])

                    number_of_items = font.render(f"{inventory.inventory_dict[i][1]}", True, "White")
                    noi_rect = number_of_items.get_rect()
                    noi_rect.topleft = (const.inventory_item_px[i] + 20, 671 + 20)
                    screen.blit(number_of_items, noi_rect)
        breaking.update_breaking()
