import pygame
import imagesetter as image

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
    def __init__(self, position, zoom=2):
        super().__init__()
        self.position = position
        self.zoom = zoom
        self.is_open = False  # Indique si le coffre est ouvert ou fermé

        # Chargement des chemins des images pour l'animation du coffre fermé
        chest_close_paths = [rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\chest\chest_{i}.png' for i in range(1, 5)]
        # Chargement des chemins des images pour l'animation du coffre ouvert
        chest_open_paths = [rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\chest\chest_open_{i}.png' for i in range(1, 5)]

        # Création de l'animation pour le coffre fermé
        self.chest_close_animation = image.animated_sprite(chest_close_paths, position)
        # Création de l'animation pour le coffre ouvert
        self.chest_open_animation = image.animated_sprite(chest_open_paths, position)

    def open_chest(self):
        # Change l'état du coffre à ouvert et lance l'animation du coffre ouvert
        self.is_open = True
        self.chest_close_animation.stop()  # Arrête l'animation du coffre fermé
        self.chest_open_animation.start()  # Lance l'animation du coffre ouvert

    def close_chest(self):
        # Change l'état du coffre à fermé et lance l'animation du coffre fermé
        self.is_open = False
        self.chest_open_animation.stop()  # Arrête l'animation du coffre ouvert
        self.chest_close_animation.start()  # Lance l'animation du coffre fermé

    def update(self):
        # Met à jour les animations du coffre
        if self.is_open:
            self.chest_open_animation.update()
        else:
            self.chest_close_animation.update()

    def draw(self, screen):
        # Dessine le coffre sur l'écran en fonction de son état (ouvert ou fermé)
        if self.is_open:
            self.chest_open_animation.draw(screen)
        else:
            self.chest_close_animation.draw(screen)
            
        
            
            
            
