from PIL import Image   
import pygame

class tile:

    def __init__(self, fichier, x = None, y = None,size = 16):
        self.cache_tile = {} #cache des tiles 
        self.img_set = Image.open(fichier)
        self.size = size
        if x != None and y!= None:
            self.load(x, y)
        else:
            self.img_tile = None


    def debug_afficher(self):
        print('cache:',self.cache_tile )

    def load(self,i, j):
        pil_image = self.img_set.crop(
            (
                i * self.size, #gauche
                j * self.size, #haut
                (i+1)*self.size, #droite
                (j+1)*self.size #bas
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

    