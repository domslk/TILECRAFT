import pygame
import inventory
#54 - 63
class AddBack():
    @staticmethod
    def add_back_to_inventory():

        def addit(item, i_of_item):
            print("adding")
            print(item[0])
            print(i_of_item)

            for i in range(1, 55):
                if inventory.inventory_dict[i][0] == item[0]:
                    combined_i = inventory.inventory_dict[i][1] + item[1]
                    if combined_i <= 64:
                        inventory.inventory_dict[i] = [item[0], combined_i]
                        inventory.inventory_dict[i_of_item] = [None, 0]
                        return
                    else:
                        inventory.inventory_dict[i] = [item[0], 64]
                        remaining = combined_i - 64
                        inventory.inventory_dict[i_of_item] = [item[0], remaining]
            if item[1] > 0:
                for i in range(1,55):
                    if inventory.inventory_dict[i][0] is None:
                        inventory.inventory_dict[i] = [item[0], item[1]]
                        inventory.inventory_dict[i_of_item] = [None, 0]
                        return

        for i in range(54, len(inventory.inventory_dict)):
            if inventory.inventory_dict[i][0] is not None:
                addit(inventory.inventory_dict[i], i)



