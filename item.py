import pygame
import Imagesetter as image

class AnimatedSword(pygame.sprite.Sprite):
    def __init__(self, position, zoom=2.5):
        super().__init__()
        self.image_paths = [ r'Graphic\Weapon\Sword\images_cut\frame_0_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_1_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_2_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_3_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_4_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_5_delay-0.1s.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in self.image_paths]
        self.rect = pygame.Rect(position[0], position[1], self.images[0].get_width(), self.images[0].get_height())
        self.zoom = zoom

    def start_attack(self):
        self.is_attacking = True

    def update(self):
        pass

    def draw(self, screen):
        # Afficher la première image de l'animation lorsque l'épée n'attaque pas
        first_image = self.images[0]
        w, h = first_image.get_width(), first_image.get_height()
        first_image_upscaled = pygame.transform.scale(first_image, (w * self.zoom, h * self.zoom))
        screen.blit(first_image_upscaled, self.rect.topleft)
        
        
class Chest(pygame.sprite.Sprite):
    # A terminer
    def __init__(self, position):
        super().__init__()
        self.position = position
        
        # Charger les images d'animation du coffre fermé
        chest_close_paths = []
        for i in range(1, 5): 
            chest_close_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\chest\chest_{i}.png')
        self.chest_close = image.animated_sprite(chest_close_paths, position)
        
        # Charger les images d'animation du coffre ouvert
        chest_open_paths = []
        for i in range(1, 5): 
            chest_open_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\chest\chest_open_{i}.png')
        self.chest_open = image.animated_sprite(chest_open_paths, position)
        
        # Indicateur pour savoir si le coffre est ouvert ou fermé
        self.is_open = False  

        # Obtenir le rectangle encadrant du coffre
        self.rect = self.chest_close.rect  # Utiliser le rectangle du coffre fermé par défaut

    def open(self):
        self.is_open = True
        
    def update(self):
        if self.is_open:
            self.chest_open
        else:
            self.chest_close


    def draw(self, screen):
        if self.is_open:
            self.chest_open.draw(screen)
        else:
            self.chest_close_animation.draw(screen)
            
        
            
            
            
class AnimatedCoin(pygame.sprite.Sprite):
    def __init__(self, position, zoom=4):
        super().__init__()
        self.images = []
        for i in range(1,5):
            self.images.append(pygame.image.load(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_{i}.png').convert_alpha())
        self.rect = pygame.Rect(position[0], position[1], self.images[0].get_width(), self.images[0].get_height())
        self.zoom = zoom
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
