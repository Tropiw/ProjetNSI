# enemy.py

import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, position, tile_size, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.is_moving = False
        self.direction = 1
        self.speed = speed
        self.animation_lists = {'walk_right': [], 'walk_left': [], 'die': []}
        self.animation_step = 7
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.load_animation_frames(tile_size)
        self.health = 100

    def load_animation_frames(self, tile_size):
        # Chargement des animations marche à gauche
        for i in range(self.animation_step):
            tile_rect = pygame.Rect(i * tile_size[0], 0, tile_size[0], tile_size[1])
            self.animation_lists['walk_left'].append(self.image.subsurface(tile_rect))

        # Chargement des animations marche à droite (en reflétant les images de gauche)
        for frame in self.animation_lists['walk_left']:
            walk_right_frame = pygame.transform.flip(frame, True, False)
            self.animation_lists['walk_right'].append(walk_right_frame)

        # Chargement des animations de mort (3ème ligne = 2*25)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 2 * tile_size[1], tile_size[0], tile_size[1])
            self.animation_lists["die"].append(self.image.subsurface(tile_rect))

    def update(self):
        # Mettre à jour la position de l'ennemi

        # Déplacer l'ennemi dans la direction actuelle
        self.rect.x += self.speed * self.direction

        # Vérifier si l'ennemi atteint les bords de l'écran
        if self.rect.right >= 1125:  # Si l'ennemi atteint le bord droit
            self.direction = -1  # Changer la direction vers la gauche
        elif self.rect.left <= 65:  # Si l'ennemi atteint le bord gauche
            self.direction = 1  # Changer la direction vers la droite

        # Mise à jour de l'animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_cooldown:  # Vérification cooldown animation pour éviter une animation top rapide
            self.frame = (self.frame + 1) % self.animation_step  # Si l'on arrive à la dernière image, on boucle l'animation
            self.last_update = now  # Remettre à jour pour le cooldown

        # Changer l'animation en fonction de la direction de déplacement
        if self.direction == 1:  # Vers la droite
            self.current_animation = 'walk_right'
        else:  # Vers la gauche
            self.current_animation = 'walk_left'

    def draw(self, screen):
        # Obtenir le cadre actuel de l'animation
        current_frame = self.animation_lists[self.current_animation][self.frame]

        # Redimensionner l'image du cadre
        w, h = current_frame.get_width(), current_frame.get_height()
        image_upscaled = pygame.transform.scale(current_frame, (w * 4, h * 4))

        # Dessiner l'image redimensionnée à la position de l'ennemi
        screen.blit(image_upscaled, self.rect.topleft)
