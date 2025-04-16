import os, ast, inventory

def load_inventory(inventory_dict):

    if os.path.exists('./world.txt'):
        with open('./world.txt', 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if lines[i].strip() == 'INVENTORY':
                    if i + 1 < len(lines):
                        dicline = lines[i + 1]
                        inventory.inventory_dict = ast.literal_eval(dicline)
                        print(ast.literal_eval(dicline))
                    break
