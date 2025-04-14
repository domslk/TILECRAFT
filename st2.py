from screens.inventory_overlay import Inventory_Overlay
from screens.crafting_overlay import Crafting_Overlay
from screens.pause_screen import Pause_Screen
from draw import Draw
from player import Player
from const import screen

inventory_overlay = Inventory_Overlay(screen)
crafting_overlay = Crafting_Overlay(screen)
pause_screen = Pause_Screen(screen)
draw = Draw()
player = Player()