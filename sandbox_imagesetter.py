import pygame
import Imagesetter as image


dungeon = image.tile('Graphic/Dungeon Gathering Free Version/Set 1.1.png')
for i in range(15):
    for j in range(7):
        dungeon.load(i,j)

MAP_DEBUG = 1
        
character = image.tile('Graphic/perso/Sprites/Prototype/Prototype_Worksheet.png')
for i in range(4):
    for j in range(12):
        character.load(i,j)

dungeon.debug_afficher()
character.debug_afficher()
print(len(character.cache_tile))