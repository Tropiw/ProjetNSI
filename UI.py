import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, position, image_path, zoom=8):
        super().__init__()
        self.image_path = image_path
        self.image = pygame.image.load(image_path).convert_alpha()
        self.tile_size = (32,32)
        self.rect = pygame.Rect(position[0], position[1], self.tile_size[0] * zoom, self.tile_size[1] * zoom)
        self.health_states = [(1,1), (1, 0), (0, 2), (0, 1), (0,0)]  # 5 états de barre de vie correspondant à chaque vie restante
        self.zoom = zoom
        self.current_health = 4  # Initialisation de la vie actuelle au maximum

    def update_health(self, new_health):
        # Met à jour la barre de vie avec la nouvelle valeur de santé
        self.current_health = new_health

    def draw(self, screen):
        # Extrait la tuile correspondant à l'état actuel de la barre de vie
        tile_position = self.health_states[self.current_health]
        tile_image = self.image.subsurface(pygame.Rect(tile_position[0] * self.tile_size[0],
                                                       tile_position[1] * self.tile_size[1],
                                                       self.tile_size[0], self.tile_size[1]))

        # Redimensionne la tuile à la taille désirée
        w, h = tile_image.get_width(), tile_image.get_height()
        image_upscaled = pygame.transform.scale(tile_image, (w * self.zoom, h * self.zoom))

        # Affiche la tuile à la position spécifiée
        screen.blit(image_upscaled, self.rect.topleft)
