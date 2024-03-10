import pygame

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
        
            
            
            
