from PIL import Image   
import pygame

class tile:
    SIZE = 16 # width and length

    def __init__(self, fichier):
        self.img = Image.open(fichier)


    def debug_afficher(self):
        self.img.show()

    def load(self,i, j):
        pil_image = self.img.crop(
            (
                i * tile.SIZE, #gauche
                j*tile.SIZE, #haut
                (i+1)*tile.SIZE, #droite
                (j+1)*tile.SIZE #bas
            ))
        image_data = pil_image.tobytes()
        image_dimensions = pil_image.size
        mode = pil_image.mode
        pygame_surface = pygame.image.fromstring(image_data, image_dimensions, mode)
        pygame_surface = pygame.transform.scale(pygame_surface, (80, 80))
        return pygame_surface
    
    def blit_tile(screen,tile_pos,coordonate):
        screen.blit(tile('Graphic\Dungeon Gathering Free Version\Set 1.1.png').load(tile_pos[0],tile_pos[1]),(coordonate))



