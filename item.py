import pygame

class AnimatedSword(pygame.sprite.Sprite):
    def __init__(self, position, zoom=3):
        super().__init__()
        self.image_paths = [ r'Graphic\Weapon\Sword\images_cut\frame_0_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_1_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_2_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_3_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_4_delay-0.1s.png',
                       r'Graphic\Weapon\Sword\images_cut\frame_5_delay-0.1s.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in self.image_paths]
        self.rect = pygame.Rect(position[0], position[1], self.images[0].get_width(), self.images[0].get_height())
        self.animation_step = len(self.images)
        self.animation_cooldown = 50
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.zoom = zoom
        self.is_attacking = False

    def start_attack(self):
        print('attaque !')
        self.is_attacking = True

    def stop_attack(self):
        self.is_attacking = False

    def update_position(self, new_position):
        self.rect.x = new_position[0]
        self.rect.y = new_position[1]
    
    def update(self):
        now = pygame.time.get_ticks()
        if self.is_attacking:
            # Mettre à jour l'animation d'attaque si l'attaque est en cours
            if now - self.last_update > self.animation_cooldown:
                self.frame = (self.frame + 1) % self.animation_step  # Mettre à jour le cadre de l'animation
                if self.frame == 0:  # Si l'animation est terminée
                    self.is_attacking = False  # Réinitialiser l'attaque
                self.last_update = now
        else:
            # Mettre à jour l'animation même si l'attaque n'est pas en cours
            self.frame = 0  # Réinitialiser le cadre de l'animation
            self.last_update = now



    def draw(self, screen):
        if self.is_attacking:
            # Obtenir l'image actuelle de l'animation d'attaque
            current_image = self.images[self.frame]

            # Redimensionner l'image
            w, h = current_image.get_width(), current_image.get_height()
            image_upscaled = pygame.transform.scale(current_image, (w * self.zoom, h * self.zoom))

            # Dessiner l'image à la position de l'épée sur l'écran
            screen.blit(image_upscaled, self.rect.topleft)
        else:
            # Afficher la première image de l'animation lorsque l'épée n'attaque pas
            first_image = self.images[0]
            w, h = first_image.get_width(), first_image.get_height()
            first_image_upscaled = pygame.transform.scale(first_image, (w * self.zoom, h * self.zoom))
            screen.blit(first_image_upscaled, self.rect.topleft)