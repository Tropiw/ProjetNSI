from PIL import Image   
import pygame
# Fichier d'outils pour la création de la map 
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
        
        
        
        
class Image_statique: # Image simple à afficher
    def __init__(self, image_path, position=(0, 0), zoom=3):
        self.image = pygame.image.load(image_path)
        self.position = position
        w = self.image.get_width()
        h = self.image.get_height()
        self.image_upscaled = pygame.transform.scale(self.image, (w * zoom, h * zoom))  # Grandir l'image

    def draw(self, screen):
        screen.blit(self.image_upscaled, self.position)
        
    def update(self):
        pass # pas besoin mais obligatoire
    
    
    
    
class Obstacle(pygame.sprite.Sprite): # # Outil pour afficher une image à partir d'une spritesheet avec des tiles
    def __init__(self, image_path, position, tile_size, tile_position, zoom = 1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.tile_position = tile_position
        self.zoom = zoom

    def draw(self, screen):
        # Extrait une tuile spécifique de l'image principale en fonction de la position et de la taille de la tuile
        tile_image = self.image.subsurface(pygame.Rect(self.tile_position[0] * self.tile_size[0],
                                                       self.tile_position[1] * self.tile_size[1],
                                                       self.tile_size[0], self.tile_size[1]))
        
        # Redimensionner la tuile à la taille désirée
        w,h = tile_image.get_width(), tile_image.get_height()
        image_upscaled = pygame.transform.scale(tile_image, (w * self.zoom, h * self.zoom))

        # Afficher la tuile à la position du joueur
        screen.blit(image_upscaled, self.rect.topleft)


class animated_sprite(pygame.sprite.Sprite): # Outil pour animer des image si on en a plusieurs
    def __init__(self, image_paths, position, zoom = 4):
        super().__init__()
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.rect = pygame.Rect(position[0], position[1], self.images[0].get_width(), self.images[0].get_height())
        self.animation_step = len(self.images)
        self.animation_cooldown = 100
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.zoom = zoom

    def update(self):
        # Mettre à jour l'animation de rotation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_cooldown:
            self.frame = (self.frame + 1) % self.animation_step
            self.last_update = now

    def draw(self, screen):
        # Obtenir l'image actuelle de l'animation de rotation
        current_image = self.images[self.frame]

        # Redimensionner l'image
        w,h = current_image.get_width(), current_image.get_height()
        image_upscaled = pygame.transform.scale(current_image, (w * self.zoom, h * self.zoom))
        
        # Dessiner l'image à la position de la l'élément sur l'écran
        screen.blit(image_upscaled, self.rect.topleft)


    