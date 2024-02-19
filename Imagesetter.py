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
        image_dimensions = (tile.SIZE,tile.SIZE)
        pygame_surface = pygame.image.fromstring(image_data, image_dimensions, "RGB")
        return pygame_surface



