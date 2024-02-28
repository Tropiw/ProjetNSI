import pygame
import menu 


import pygame
import imagesetter as image
import menu as menu
import personnage as perso
import map_module as map_module
import sys

pygame.init()
tile_set = image.tile('Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
clock.tick(90)
running = True
objects = []  # Liste pour stocker les objets à dessiner
main_menu = menu.menu()
mouse_pos = (0,0)
mode = 2
donjon = map_module.Dongeon(screen,1280,720)
screen_debug = donjon.dico_map["map_debug"]
# pygame setup
pygame.init()





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    screen.blit(screen_debug,(0,0))                       

    # fill the screen with a color to wipe away anything from last frame
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()