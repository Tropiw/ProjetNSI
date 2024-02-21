from PIL import Image   
import pygame

class tile:
    SIZE = 16 # width and length

    def __init__(self, fichier, x = None, y = None):
        self.cache_tile = {} #cache des tiles 
        self.img_set = Image.open(fichier)
        if x != None and y!= None:
            self.load(x, y)
        else:
            self.img_tile = None


    def debug_afficher(self):
        print('cache:',self.cache_tile )

    def load(self,i, j):
        pil_image = self.img_set.crop(
            (
                i * tile.SIZE, #gauche
                j * tile.SIZE, #haut
                (i+1)*tile.SIZE, #droite
                (j+1)*tile.SIZE #bas
            ))
        image_data = pil_image.tobytes()        #Permet de convertir une image pillow en surface pygame
        image_dimensions = pil_image.size
        mode = pil_image.mode
        pygame_surface = pygame.image.fromstring(image_data, image_dimensions, mode)
        pygame_surface = pygame.transform.scale(pygame_surface, (80, 80))
        self.img_tile = pygame_surface
        self.cache_tile[(i,j)] = pygame_surface ##insertion des tile dans le cache 
    
    
    def render(self, screen,tile_pos,coordonate):
        if self.img_tile != None:
            screen.blit((self.img_tile),(coordonate))
            
    def blit_tile(self,screen,tile,pos):   
        screen.blit(self.cache_tile[tile],pos)