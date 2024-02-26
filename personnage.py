import pygame
import imagesetter as image

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
        self.animation_lists = {"idle": [], "walk_right": [], "walk_left": [], "walk_up": [], "walk_down": []}
        self.animation_step = 3
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.load_animation_frames(tile_size)
        self.current_animation = 'idle'

    def load_animation_frames(self, tile_size):
        # Chargement des animations immobile (1ère ligne = 0*32)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 0, tile_size[0], tile_size[1])
            self.animation_lists["idle"].append(self.image.subsurface(tile_rect))
            
        # Chargement des animations marche a droite (5ème ligne = 4*32)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 4*32, tile_size[0], tile_size[1])
            self.animation_lists["walk_right"].append(self.image.subsurface(tile_rect))
            
        # Chargement des animations marche à gauche (en reflétant les images de gauche)
        for frame in self.animation_lists['walk_right']:
            walk_left_frame = pygame.transform.flip(frame, True, False)
            self.animation_lists['walk_left'].append(walk_left_frame)

        # Chargement des animations marche haut (6ème ligne = 5*32)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 5*32, tile_size[0], tile_size[1])
            self.animation_lists["walk_up"].append(self.image.subsurface(tile_rect))
            
        # Chargement des animations marche a bas (4ème ligne = 3*32)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 3*32, tile_size[0], tile_size[1])
            self.animation_lists["walk_down"].append(self.image.subsurface(tile_rect))

    def detect_movement(self):
        keys = pygame.key.get_pressed()
        self.is_moving = any(keys[movement_key] for movement_key in self.movement)

        if keys[self.movement[0]]:  # Vers le haut
            self.current_animation = 'walk_up'
        elif keys[self.movement[1]]:  # Vers le bas
            self.current_animation = 'walk_down'
        elif keys[self.movement[2]]:  # Vers la gauche
            self.current_animation = 'walk_left'
        elif keys[self.movement[3]]:  # Vers la droite
            self.current_animation = 'walk_right'
        else:
            self.current_animation = 'idle'

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
        # Sélectionner l'animation appropriée en fonction de la direction du mouvement
        if self.is_moving:
            current_animation = self.current_animation
        else:
            current_animation = 'idle'

        # Obtenir le cadre actuel de l'animation
        current_frame = self.animation_lists[current_animation][self.frame]

        # Redimensionner l'image du cadre
        w, h = current_frame.get_width(), current_frame.get_height()
        image_upscaled = pygame.transform.scale(current_frame, (w * 6, h * 6))

        # Dessiner l'image redimensionnée à la position du joueur
        screen.blit(image_upscaled, self.rect.topleft)

    
    # UTILISATION
    # obstacle_tile_position = (3, 4)  # Position de la tuile pour cet obstacle
    # obstacle = Obstacle("chemin/vers/image.png", (x, y), (largeur_tile, hauteur_tile), obstacle_tile_position)
    


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, position, tile_size, speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.is_moving = False
        self.direction = 1
        self.speed = speed
        self.animation_lists = { 'walk_right': [], 'walk_left': [], 'eat_left': [], 'eat_right': [], 'die': []}
        self.animation_step = 7
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.load_animation_frames(tile_size)
        
    def load_animation_frames(self, tile_size):
        # Chargement des animations marche à gauche
        for i in range(self.animation_step):
            tile_rect = pygame.Rect(i * tile_size[0], 0, tile_size[0], tile_size[1])
            self.animation_lists['walk_left'].append(self.image.subsurface(tile_rect))

        # Chargement des animations marche à droite (en reflétant les images de gauche)
        for frame in self.animation_lists['walk_left']:
            walk_right_frame = pygame.transform.flip(frame, True, False)
            self.animation_lists['walk_right'].append(walk_right_frame)
            
        # Chargement des animations manger à gauche (2ème ligne = 1*25)
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * tile_size[0], 1*25, tile_size[0], tile_size[1])
            self.animation_lists["eat_left"].append(self.image.subsurface(tile_rect))
            
        # Chargement des animations manger à droite (2ème ligne = 1*25) --> miroir animation gauche
        for frame in self.animation_lists['eat_left']:
            eat_right_frame = pygame.transform.flip(frame, True, False)
            self.animation_lists['eat_right'].append(eat_right_frame)

        
        # Chargement des animations de mort (3ème ligne = 2*25)
        for x in range(3):
            tile_rect = pygame.Rect(x * tile_size[0], 2*25, tile_size[0], tile_size[1])
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
        if now - self.last_update > self.animation_cooldown: # Vérification cooldown animation pour éviter une animation top rapide
            self.frame = (self.frame + 1) % self.animation_step # Si l'on arrive à la dernière image, on boucle l'animation
            self.last_update = now # Remettre à jour pour le cooldown
            
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

        # Dessiner l'image redimensionnée à la position du joueur
        screen.blit(image_upscaled, self.rect.topleft)



