import pygame
import Imagesetter as image

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, position, tile_size, player=1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.player = player
        if player == 1:
            self.movement = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]  # attribuer les touches au joueur 1
        else:
            self.movement = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]  # attribuer les touches au joueur 2
        self.sfx_move = pygame.mixer.Sound(r"SFX\footstep mc (2).mp3")
        self.is_moving = False
        self.is_sound_playing = False  # Variable pour suivre l'état du son de marche
        self.animation_lists = {"idle": [], "walk": []}
        self.animation_step = 3
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 500
        self.frame = 0
        self.load_animation_frames(tile_size)
        self.current_animation = 'idle'

    def load_animation_frames(self, tile_size):
        # Chargement des animations immobile (y = 0)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 0, tile_size[0], tile_size[1])
            self.animation_lists["idle"].append(self.image.subsurface(tile_rect))
        # Chargement des animations marche a droite (y = 1)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 32, tile_size[0], tile_size[1])
            self.animation_lists["walk"].append(self.image.subsurface(tile_rect))

    def detect_movement(self):
        keys = pygame.key.get_pressed()
        self.is_moving = any(keys[movement_key] for movement_key in self.movement)

    def update(self):
        self.detect_movement()
        keys = pygame.key.get_pressed()

        # Mouvement vers le haut
        if keys[self.movement[0]]:
            if self.rect.y > 26:
                self.rect.y -= 5
        # Mouvement vers le bas
        elif keys[self.movement[1]]:
            if self.rect.y < 502:
                self.rect.y += 5
        # Mouvement vers la gauche
        elif keys[self.movement[2]]:
            if self.rect.x > 20:
                self.rect.x -= 5
        # Mouvement vers la droite
        elif keys[self.movement[3]]:
            if self.rect.x < 1070:
                self.rect.x += 5

        # Jouer le son de marche si le joueur commence à se déplacer
        if self.is_moving:
            if not self.is_sound_playing:  # Vérifie si le son n'est pas déjà en train de jouer
                self.sfx_move.play(loops=-1)  # Joue le son en boucle (-1) en cas de maintient prolongé de la touche 
                self.is_sound_playing = True  # Met à jour l'état du son
        else:
            if self.is_sound_playing:  # Si le joueur s'arrête de se déplacer
                self.sfx_move.stop()  # Arrête le son
                self.is_sound_playing = False  # Met à jour l'état du son

        # Mise à jour de l'animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_cooldown: # Vérification cooldown animation pour éviter une animation top rapide
            self.frame = (self.frame + 1) % self.animation_step # Si l'on arrive à la dernière image, on boucle l'animation
            self.last_update = now # Remettre à jour pour le cooldown

    def draw(self, screen):
        # Dessiner l'animation appropriée en fonction de l'état actuel du joueur
        current_animation = 'walk' if self.is_moving else 'idle'
        current_frame = self.animation_lists[current_animation][self.frame]
        w, h = current_frame.get_width(), current_frame.get_height()
        image_upscaled = pygame.transform.scale(current_frame, (w * 6, h * 6))
        screen.blit(image_upscaled, self.rect.topleft)



class Obstacle(pygame.sprite.Sprite): # Décor dynamique
    def __init__(self, image_path, position, tile_size, tile_position):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.tile_position = tile_position

    def draw(self, screen):
        tile_image = self.image.subsurface(pygame.Rect(self.tile_position[0] * self.tile_size[0],
                                                       self.tile_position[1] * self.tile_size[1],
                                                       self.tile_size[0], self.tile_size[1]))
        # Redimensionner la tuile à la taille désirée
        scaled_tile_image = pygame.transform.scale(tile_image, (128, 128))

        # Afficher la tuile à la position du joueur
        screen.blit(scaled_tile_image, self.rect.topleft)

    
    # UTILISATION
    # obstacle_tile_position = (3, 4)  # Position de la tuile pour cet obstacle
    # obstacle = Obstacle("chemin/vers/image.png", (x, y), (largeur_tile, hauteur_tile), obstacle_tile_position)
    
class Ennemy(Obstacle):
    def __init__(self, image_path, position, tile_size, tile_position, speed):
        super().__init__(image_path, position, tile_size, tile_position)
        self.speed = speed
        self.direction = 1  # 1 pour déplacement vers la droite, -1 pour déplacement vers la gauche

    def update(self):
        # Déplacer l'ennemi dans la direction actuelle
        self.rect.x += self.speed * self.direction

        # Vérifier si l'ennemi atteint les bords de l'écran
        if self.rect.right >= 1125:  # Si l'ennemi atteint le bord droit
            self.direction = -1  # Changer la direction vers la gauche
        elif self.rect.left <= 65:  # Si l'ennemi atteint le bord gauche
            self.direction = 1  # Changer la direction vers la droite

        
class Image: # Décor statique
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


