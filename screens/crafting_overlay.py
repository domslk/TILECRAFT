import pygame


from const import SCREEN_WIDTH, SCREEN_HEIGHT
import inventory
import block
import textures
import crafting
pygame.init()
x = 240
y = 175
font = pygame.font.Font('./font.otf', 32)



t_dict = {}
y_count = 0
j = 0
for i in range(1,55):
    j += 1
    t_dict[i] = (x + 56 * j, y)
    y_count += 1
    if y_count > 8:
        y += 56
        y_count = 0
        j = 0
t_dict[55] = (820, 230)
t_dict[56] = (875, 230)
t_dict[57] = (930, 230)

t_dict[58] = (820, 285)
t_dict[59] = (875, 285)
t_dict[60] = (930, 285)

t_dict[61] = (820, 340)
t_dict[62] = (875, 340)
t_dict[63] = (930, 340)



class Crafting_Overlay:
    def __init__(self, screen):
        self.screen = screen
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 100))
        self.x_dict = t_dict

    def draw(self):
        global x
        pygame.draw.rect(self.screen, "white", pygame.Rect(SCREEN_WIDTH // 2 - 375, SCREEN_HEIGHT // 2 - 230, 750, 420))
        for slot_id, (slot_x, slot_y) in self.x_dict.items():
            if slot_id != inventory.selected_slot_id:
                slot_rect = pygame.Rect(slot_x, slot_y, 48, 48)
                pygame.draw.rect(self.screen, (160, 160, 160), slot_rect, 2)
            else:
                slot_rect = pygame.Rect(slot_x - 3, slot_y - 3, 56, 56)
                pygame.draw.rect(self.screen, (0, 0, 0), slot_rect, 5)
        for item in range(1, len(inventory.inventory_dict)):
            if inventory.inventory_dict[item][0] is not None:
                if inventory.inventory_dict[item][0] == "door":
                    texture = textures.ITEM_TEXTURES["door_small"]
                else:
                    texture = textures.ITEM_TEXTURES[(inventory.inventory_dict[item][0])]
                block.Block.draw_on_screen(self.x_dict[item][0], self.x_dict[item][1], texture)

                number_of_items = font.render(f"{inventory.inventory_dict[item][1]}", True, "White")
                noi_rect = number_of_items.get_rect()
                noi_rect.topleft = (self.x_dict[item][0] + 20, self.x_dict[item][1] + 20)
                self.screen.blit(number_of_items, noi_rect)

        self.screen.blit(self.overlay, (0, 0))
        self.screen.blit(textures.ENTER, (875, 400))


    def get_3x3_table(self):
        table = []
        items = {}
        for i in range(55, 65):
            table.append(inventory.inventory_dict[i])
        for item in table:
            if item[0] is None:
                continue
            if item[0] not in items:
                items[item[0]] = item[1]
            else:
                items[item[0]] += item[1]
        return table, items

    def pass_requirements(self, items, requirements):
        for item, num in requirements.items():
            if items.get(item, 0) < num:
                return False
        return True

    def table_to_crafting(self, table):
        block_types = [item[0] for item in table]
        grid = []
        for i in range(0, 9, 3):
            grid.append(block_types[i:i + 3])
        return grid

    def table_3x3_to_slots(self, crafting_3x3):
        slots_3x3 = []
        for line in range(len(crafting_3x3)):
            for row in range(len(crafting_3x3[0])):
                if crafting_3x3[line][row] == None:
                    slots_3x3.append(0)
                else:
                    slots_3x3.append(1)
        return slots_3x3


    def remove_from_table_3x3(self, slots_3x3, number): # number -> recipe[requirements]
        for i in range(len(slots_3x3)):
            if slots_3x3[i] != 0:
                inventory_slot = 55 + i
                item_count = inventory.inventory_dict[inventory_slot][1]
                if item_count > 0:
                    inventory.inventory_dict[inventory_slot][1] -= number[inventory.inventory_dict[inventory_slot][0]]
                    if inventory.inventory_dict[inventory_slot][1] <= 0:
                        inventory.inventory_dict[inventory_slot] = [None, 0]

    def check_crafting(self):
        table, items = self.get_3x3_table()
        crafting_3x3 = self.table_to_crafting(table)
        slots_3x3 = self.table_3x3_to_slots(crafting_3x3)
        for recipe_name, recipe in crafting.crafting_3x3_table.items():
            if self.pass_requirements(items, recipe["requirements"]):
                if recipe["position"] == "any":
                    self.remove_from_table_3x3(slots_3x3, recipe["requirements"])
                    self.add_output_to_inventory(recipe["output"])
                    break
                for positions in recipe["position"]:
                    if self.match_crafting_grids(positions, crafting_3x3):
                        self.remove_from_table_3x3(slots_3x3, recipe["requirements"])
                        self.add_output_to_inventory(recipe["output"])
                        break

    def match_crafting_grids(self, position, the_grid):
        for i in range(3):
            for j in range(3):
                if position[i][j] != the_grid[i][j]:
                    return False
        return True

    def add_output_to_inventory(self, output):
        for j in range(1, 55):
            slot = inventory.inventory_dict[j]
            if slot[0] == output[0]:
                if slot[1] < 64:
                    slot[1] += output[1]
                    return
                else:
                    continue
        for j in range(1, 55):
            slot = inventory.inventory_dict[j]
            if slot[0] is None:
                inventory.inventory_dict[j] = list(output)
                return



