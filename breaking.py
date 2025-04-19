import st
import const
import time
import inventory
from const import screen
import textures


def update_breaking():
    if st.breaking_block is None:
        return

    ch_x, ch_y, block_x, block_y, start_time = st.breaking_block
    world_x = ch_x * const.CHUNK_SIZE + block_x
    world_y = ch_y * const.CHUNK_SIZE + block_y
    screen_x = world_x * const.BLOCK_SIZE - st.camera_x
    screen_y = world_y * const.BLOCK_SIZE - st.camera_y

    elapsed = time.time() - start_time

    try:
        block_type = st.chunks[(ch_x, ch_y)].grid[block_y][block_x]
    except KeyError:
        st.breaking_block = None
        return

    break_time = 1.0
    match block_type:
        case "stone":
            break_time = 0
        case "wood":
            break_time = 2
        case "flower" | "leaves":
            break_time = 0.1
        case "grass" | "dirt":
            break_time = 0.3
        case "diamond":
            break_time = 1.5

    for time1 in range(1, len(const.breaking_block_overlay)):
        if elapsed > const.breaking_block_overlay[time1][0] * break_time:
            screen.blit(textures.ITEM_TEXTURES[const.breaking_block_overlay[time1][1]], (screen_x, screen_y))
    if elapsed >= break_time:
        for i in range(1, len(inventory.inventory_dict) + 1):
            if inventory.inventory_dict[i][0] == block_type and inventory.inventory_dict[i][1] < 64:
                if st.return_pickability(block_type):
                    inventory.inventory_dict[i][1] += 1
                    st.items_in_inventory += 1
                    break
            elif inventory.inventory_dict[i][0] is None:
                if st.return_pickability(block_type):
                    inventory.inventory_dict[i] = [block_type, 1]
                    st.items_in_inventory += 1
                    break
        else:
            pass

        st.chunks[(ch_x, ch_y)].grid[block_y][block_x] = None
        st.breaking_block = None

