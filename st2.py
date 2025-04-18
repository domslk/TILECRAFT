from screens.inventory_overlay import Inventory_Overlay
from screens.crafting_overlay import Crafting_Overlay
from screens.pause_screen import Pause_Screen
from draw import Draw
from player import Player
from const import screen
from screens.splash_screen import Splash_Screen
from helper.add_items_back_to_inventory import AddBack

inventory_overlay = Inventory_Overlay(screen)
crafting_overlay = Crafting_Overlay(screen)
pause_screen = Pause_Screen(screen)
splash_screen = Splash_Screen(screen)
draw = Draw()
player = Player()
add_back_to_inventory = AddBack()
