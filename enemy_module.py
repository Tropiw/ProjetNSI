import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, position, tile_size, speed=1, player_group = None, enemies_group = None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.is_moving = False
        self.direction = 1
        self.speed = speed
        self.animation_lists = {'walk_right': [], 'walk_left': [], 'die': [], 'eat_left': [], 'eat_right': []}
        self.animation_step = 7
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        self.load_animation_frames(tile_size)
        self.health = 100
        self.is_alive = True
        self.player_group = player_group
        self.is_eating = False
        self.enemies_group = enemies_group
        self.is_dying = False
        self.is_finished = False
        self.sfx_kill = pygame.mixer.Sound(r"SFX\Knife Cut SFX.mp3")
        self.sfx_kill.set_volume(0.3)
        
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
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * tile_size[0], 2 * 25, tile_size[0], tile_size[1])
            self.animation_lists["die"].append(self.image.subsurface(tile_rect))
        
        # Chargement des animations de manger a gacuhe
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * tile_size[0], 1*25, tile_size[0], tile_size[1])
            self.animation_lists["eat_left"].append(self.image.subsurface(tile_rect))
            
        # Chargement des animations de manger a droite
        for frame in self.animation_lists['eat_left']:
            eat_left_frame = pygame.transform.flip(frame, True, False)
            self.animation_lists['eat_right'].append(eat_left_frame)
            
    def update(self):
        if self.is_alive:

            # Déplacer l'ennemi dans la direction actuelle
            self.rect.x += self.speed * self.direction

            # Vérifier si l'ennemi atteint les bords de l'écran
            if self.rect.right >= 1125:  # Si l'ennemi atteint le bord droit
                self.direction = -1  # Changer la direction vers la gauche
            elif self.rect.left <= 65:  # Si l'ennemi atteint le bord gauche
                self.direction = 1  # Changer la direction vers la droite


            if self.player_group is not None:
                self.is_eating = False  # Réinitialiser la variable à False avant de parcourir les joueurs
                for player in self.player_group:
                    dist = self.distance(player.rect)
                    if dist < 100:
                        if self.direction == 1:
                            self.current_animation = 'eat_right'
                        else:
                            self.current_animation = 'eat_left'
                        self.is_eating = True  # Mettre à True seulement si un joueur est à portée
                        break  # Sortir de la boucle dès qu'un joueur est trouvé à portée


            # Si l'ennemi a fini de manger, reprendre l'animation de marche
            if not self.is_eating:
                if self.direction == 1:
                    self.current_animation = 'walk_right'
                else:
                    self.current_animation = 'walk_left'

                
            now = pygame.time.get_ticks()
            if now - self.last_update > self.animation_cooldown:  # Vérification cooldown animation pour éviter une animation top rapide
                self.frame = (self.frame + 1) % self.animation_step  # Si l'on arrive à la dernière image, on boucle l'animation
                self.last_update = now  # Remettre à jour pour le cooldown
            
        
        elif self.is_dying:
            if not self.is_finished:
                #animation mort
                self.current_animation = 'die'
                now = pygame.time.get_ticks()
                if now - self.last_update > self.animation_cooldown:  
                    # Vérification du cooldown de l'animation pour éviter une animation trop rapide
                    if self.frame < self.animation_step - 1:  
                        # Vérification si ce n'est pas la dernière image de l'animation
                        self.frame += 1  # Passer à l'image suivante de l'animation
                        self.last_update = now  # Remettre à jour pour le cooldown
                    else:
                        self.is_finished = True
                if self.is_finished:
                    self.enemies_group.remove(self)


    def draw(self, screen):
        # Obtenir le cadre actuel de l'animation
        current_frame = self.animation_lists[self.current_animation][self.frame]

        # Redimensionner l'image du cadre
        w, h = current_frame.get_width(), current_frame.get_height()
        image_upscaled = pygame.transform.scale(current_frame, (w * 4, h * 4))

        # Dessiner l'image redimensionnée à la position de l'ennemi
        screen.blit(image_upscaled, self.rect.topleft)
        

    def kill(self):
        if not self.is_dying:
            self.sfx_kill.play()
            self.is_alive = False
            self.is_dying = True
            self.is_finished = False  # Réinitialiser la variable is_finished
            self.frame = 0  # Réinitialiser la frame à 0
                
            
    def distance(self, rect2): # Détection pour la distance d'attaque
        # Obtenir les coordonnées du centre du joueur
        enemy_center = self.rect.center
        
        # Obtenir les coordonnées du centre du rectangle 2
        rect2_center = rect2.center

        # Calculer la distance entre les deux centres
        distance_x = enemy_center[0] - rect2_center[0]
        distance_y = enemy_center[1] - rect2_center[1]
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return distance
        