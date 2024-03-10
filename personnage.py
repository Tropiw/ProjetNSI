import pygame
import imagesetter as image
import item as item
import math
import UI as ui

class Player(pygame.sprite.Sprite):
    def __init__(self, position, player, enemies_group = None, item_group = None):
        super().__init__()
        self.tile_size = (16,17)
        self.rect = pygame.Rect(position[0], position[1], self.tile_size[0]*5, self.tile_size[1]*5)
        self.player = player
        
        # GESTION DES 2 JOUEURS
        if player == 1:
            self.movement = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_f]  # attribuer les touches au joueur 1
            self.health_bar = ui.HealthBar((45, -40), "Graphic/Health bar/health_bar_blue.png")
            image_movement_path = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight run Sprite-sheet 16x17.png'
            image_idle_path = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight idle Sprite-sheet 16x16.png'
            image_attack_path = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight attack 1 Sprite-sheet 32x32.png'
            self.attack_movement = pygame.image.load(image_attack_path).convert_alpha()
            self.image_movement = pygame.image.load(image_movement_path).convert_alpha()
            self.image_idle = pygame.image.load(image_idle_path).convert_alpha()
            
        else:
            self.movement = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN]  # attribuer les touches au joueur 2
            self.health_bar = ui.HealthBar((950, -40), "Graphic/Health bar/health_bar_red.png")
            image_movement_path = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight run Sprite-sheet 16x17.png'
            image_idle_path = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight idle Sprite-sheet 16x16.png'
            image_attack_path = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight attack 1 Sprite-sheet 32x32.png'
            self.attack_movement = pygame.image.load(image_attack_path).convert_alpha()
            self.image_movement = pygame.image.load(image_movement_path).convert_alpha()
            self.image_idle = pygame.image.load(image_idle_path).convert_alpha()
        
        # SON DE MARCHE
        self.sfx_move = pygame.mixer.Sound(r"SFX\footstep mc (2).mp3")
        self.sfx_death = pygame.mixer.Sound(r"SFX\ooh_death.mp3")
        self.is_moving = False
        self.is_sound_playing = False  # Variable pour suivre l'état du son de marche
        
        #ANIMATIONS
        self.animation_lists = {"idle": [], "walk_right": [], "walk_left": [], "walk_up": [], "walk_down": [], "death": [], "attack_right": [], "attack_left": [], "attack_up": [], "attack_down": []}
        self.animation_step = 8
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 70
        self.frame = 0
        self.load_animation_frames()
        self.current_animation = 'idle'
        self.direction = "down"
        
        # ATTAQUE
        self.sword = None
        self.attack_cooldown = 500  # Cooldown en millisecondes
        self.last_attack_time = 0  # Temps du dernière attaque
        self.attack_range = 150
        self.enemies = enemies_group
        self.is_attacking = False
        self.sfx_attack = pygame.mixer.Sound(r"SFX\Knife Shing SFX.mp3")
        self.sfx_attack.set_volume(0.1)
        
        # GESTION DE LA VIE
        self.collision_cooldown = 500
        self.last_collision_time = 0
        self.current_health = 1
        self.health_bar.current_health = self.current_health
        self.is_alive = True
        
        # Animation de mort
        self.is_dying = False
        self.death_animation = None
        self.item_group = item_group
        self.take_item_sfx = pygame.mixer.Sound(r'SFX\pop_item.mp3')
        self.take_item_sfx.set_volume(0.3)
        


    def load_animation_frames(self):
        # Chargement des animations immobile (1ère ligne = 0*32)
        self.tile_size = (16,16)
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 0, self.tile_size[0], self.tile_size[1])
            self.animation_lists["idle"].append(self.image_idle.subsurface(tile_rect))
        
        self.tile_size = (16,17)
        # Chargement des animations marche a droite (2eme ligne = 1*)
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 1*self.tile_size[1], self.tile_size[0], self.tile_size[1])
            self.animation_lists["walk_right"].append(self.image_movement.subsurface(tile_rect))
            
        # # Chargement des animations marche a gauche (4eme ligne = 3*)
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 3*self.tile_size[1], self.tile_size[0], self.tile_size[1])
            self.animation_lists["walk_left"].append(self.image_movement.subsurface(tile_rect))
            

        # Chargement des animations marche haut (3ème ligne = 2*)
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 2*self.tile_size[1], self.tile_size[0], self.tile_size[1])
            self.animation_lists["walk_up"].append(self.image_movement.subsurface(tile_rect))
            
        # Chargement des animations marche a bas (1ème ligne = 0*)
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 0, self.tile_size[0], self.tile_size[1])
            self.animation_lists["walk_down"].append(self.image_movement.subsurface(tile_rect))
            
        self.tile_size = (48,48)
        # Chargement des animations d'attaque vers le bas
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 0, self.tile_size[0], self.tile_size[1])
            self.animation_lists["attack_down"].append(self.attack_movement.subsurface(tile_rect))
            
        # Chargement des animations d'attaque vers la droite
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 1*self.tile_size[1], self.tile_size[0], self.tile_size[1])
            self.animation_lists["attack_right"].append(self.attack_movement.subsurface(tile_rect))
            
        # Chargement des animations d'attaque vers le haut
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 2*self.tile_size[1], self.tile_size[0], self.tile_size[1])
            self.animation_lists["attack_up"].append(self.attack_movement.subsurface(tile_rect))
            
        # Chargement des animations d'attaque vers la gauche
        for x in range(self.animation_step):
            tile_rect = pygame.Rect(x * self.tile_size[0], 3*self.tile_size[1], self.tile_size[0], self.tile_size[1])
            self.animation_lists["attack_left"].append(self.attack_movement.subsurface(tile_rect))

    def detect_movement(self):
        keys = pygame.key.get_pressed()
        self.is_moving = any(keys[movement_key] for movement_key in self.movement)  # Si on appuis sur une touche de mouvement, il est en mouvement

        if keys[self.movement[0]]:  # Vers le haut
            self.current_animation = 'walk_up'
            self.direction = "up"  # Met à jour la direction
        elif keys[self.movement[1]]:  # Vers le bas
            self.current_animation = 'walk_down'
            self.direction = "down"  # Met à jour la direction
        elif keys[self.movement[2]]:  # Vers la gauche
            self.current_animation = 'walk_left'
            self.direction = "left"  # Met à jour la direction
        elif keys[self.movement[3]]:  # Vers la droite
            self.current_animation = 'walk_right'
            self.direction = "right"  # Met à jour la direction
        else:
            self.current_animation = 'idle'
            self.direction = "down"
        if keys[self.movement[4]]:
            self.is_moving = False #enlever le son de marche


    def handle_attack(self):
        if self.sword != None:
            keys = pygame.key.get_pressed()
            if keys[self.movement[4]]:
                if self.direction == "down":
                    self.attack()
                    self.current_animation= 'attack_down'
                if self.direction == "up":
                    self.attack()
                    self.current_animation= 'attack_up'
                if self.direction == "right":
                    self.attack()
                    self.current_animation= 'attack_right'
                if self.direction == "left":
                    self.attack()
                    self.current_animation= 'attack_left'
                    
                
    
    def key_movement(self):
        keys = pygame.key.get_pressed()
        
        # Mouvement vers le haut
        if keys[self.movement[0]]:
            if self.rect.y > 40 :
                self.rect.y -= 5
        # Mouvement vers le bas
        elif keys[self.movement[1]]:
            if self.rect.y < 560:
                self.rect.y += 5
        # Mouvement vers la gauche
        elif keys[self.movement[2]]:
            if self.rect.x > 75:
                self.rect.x -= 5
        # Mouvement vers la droite
        elif keys[self.movement[3]]:
            if self.rect.x < 1125:
                self.rect.x += 5
                
    def walking_sound(self):
            # Jouer le son de marche si le joueur commence à se déplacer
        if self.is_alive:
            if self.is_moving:
                if not self.is_sound_playing:  # Vérifie si le son n'est pas déjà en train de jouer
                    self.sfx_move.play(loops=-1)  # Joue le son en boucle (-1) en cas de maintient prolongé de la touche 
                    self.is_sound_playing = True  # Met à jour l'état du son
            else:
                if self.is_sound_playing:  # Si le joueur s'arrête de se déplacer
                    self.sfx_move.stop()  # Arrête le son
                    self.is_sound_playing = False  # Met à jour l'état du son
        
    def update(self):
        if self.is_alive:   # Optimisation, evite de faire des calcul+s si il et mort
            self.key_movement()
            self.detect_movement()
            self.walking_sound()
            self.detect_enemy_collision()
            self.bring_item()
            self.handle_attack()
            if self.sword:  # Mettre à jour la position de l'épée si elle est ramassée
                item.AnimatedSword.update(self.sword)  # Mettre à jour l'animation de l'épée

            # Mise à jour de l'animation
            now = pygame.time.get_ticks()
            if now - self.last_update > self.animation_cooldown: # Vérification cooldown animation pour éviter une animation top rapide
                self.frame = (self.frame + 1) % self.animation_step # Si l'on arrive à la dernière image, on boucle l'animation
                self.last_update = now # Remettre à jour pour le cooldown
                


        else:
            if self.is_dying:
                # Initialiser l'animation de mort à la position actuelle du joueur
                if not self.death_animation:
                    self.death_animation = DeathAnimation((self.rect.x-65, self.rect.y-65))
                # Mettre à jour l'animation de mort
                self.death_animation.update()
            
    def draw(self, screen):
        if self.is_alive:

            # Obtenir le cadre actuel de l'animation
            current_frame = self.animation_lists[self.current_animation][self.frame]

            # Redimensionner l'image du cadre
            w, h = current_frame.get_width(), current_frame.get_height()
            image_upscaled = pygame.transform.scale(current_frame, (w * 5, h * 5))
            
            if self.current_animation == 'attack_down' or self.current_animation == 'attack_up' or self.current_animation == 'attack_right' or self.current_animation == 'attack_left':
                # Dessiner l'image redimensionnée à la position du joueur
                screen.blit(image_upscaled, (self.rect.x-80, self.rect.y-80))
            else:
                # Dessiner l'image redimensionnée à la position du joueur
                screen.blit(image_upscaled, self.rect.topleft)
            
            #Dessiner la barre de vie
            self.health_bar.draw(screen,self.sword)
            
        else:
            if self.is_dying:
                if self.death_animation:
                    # Dessiner l'animation de mort à la position actuelle du joueur
                    self.death_animation.draw(screen)
                    
            
                
    
    def attack(self):
        if self.is_attacking != True:
            self.sfx_attack.play()
            if self.sword != None:
                self.is_attacking = True
                
                # Parcourir les ennemis
                for enemy in self.enemies:
                    # Calculer la distance entre le joueur et l'ennemi
                    dist = self.distance(enemy.rect)
                    
                    # Vérifier si l'ennemi est dans la zone d'attaque
                    if dist <= self.attack_range:
                        # L'ennemi est dans la zone d'attaque, effectuer des actions d'attaque
                        enemy.kill()
                    
    def detect_enemy_collision(self):
        # Vérifie la collision avec les ennemis
        current_time = pygame.time.get_ticks()
        if current_time - self.last_collision_time > self.collision_cooldown:
            # Cooldown expiré, on peut détecter une nouvelle collision
            collision_enemy = pygame.sprite.spritecollideany(self, self.enemies)
            if collision_enemy:  # Si une collision est détectée
                if self.current_health > 0:  # Vérifie que le joueur a encore des vies restantes
                    self.current_health -= 1  # Retire une vie au joueur
                    #Mise à jour de la barre de vie du joueur
                    self.health_bar.update_health(self.current_health)
                    if self.current_health == 0:
                        self.kill()
                self.last_collision_time = current_time  # Met à jour le temps de la dernière détection de collision
                

    def distance(self, rect2): # Détection pour la distance d'attaque
        # Obtenir les coordonnées du centre du joueur
        player_center = self.rect.center
        
        # Obtenir les coordonnées du centre du rectangle 2
        rect2_center = rect2.center

        # Calculer la distance entre les deux centres
        distance_x = player_center[0] - rect2_center[0]
        distance_y = player_center[1] - rect2_center[1]
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return distance

    def kill(self):
        self.sfx_move.stop()
        self.sfx_death.play()
        if not self.is_dying:
            self.is_alive = False
            self.is_dying = True
            
    def bring_item(self):
        for object in self.item_group:
            dist = self.distance(object.rect)
            if dist < 75:
                self.take_item_sfx.play()
                if isinstance(object, item.AnimatedSword):  # Vérifie si l'élément est une épée
                    self.sword = object
                    self.item_group.remove(object)
                    self.health_bar.sword_status = object
                else:
                    self.health_bar.current_health += 1
                    self.item_group.remove(object)
class DeathAnimation(pygame.sprite.Sprite):
    def __init__(self, position, zoom=8):
        super().__init__()
        # Charger les images de l'animation de mort
        self.images = []
        for i in range(3):
            self.images.append(pygame.image.load(rf'Graphic\Generic death animation\death_{i}.png').convert_alpha())
        
        # Définir le rectangle pour l'animation à la position spécifiée
        self.rect = self.images[0].get_rect(topleft=position)
        
        # Nombre d'étapes dans l'animation
        self.animation_step = len(self.images)
        
        # Délai entre chaque étape de l'animation en millisecondes
        self.animation_cooldown = 75
        
        # Étape actuelle de l'animation
        self.frame = 0
        
        # Temps de la dernière mise à jour de l'animation
        self.last_update = pygame.time.get_ticks()
        
        # Facteur de zoom pour redimensionner l'animation
        self.zoom = zoom
        
        # Indicateur pour savoir si l'animation est en cours
        self.in_progress = True

    def update(self):
        # Mettre à jour l'animation si elle est en cours
        now = pygame.time.get_ticks()
        if self.in_progress and now - self.last_update > self.animation_cooldown:
            if self.frame < self.animation_step:
                self.frame += 1
                self.last_update = now
            else:
                # L'animation est terminée
                self.in_progress = False

    def draw(self, screen):
        # Dessiner l'étape actuelle de l'animation si elle est en cours
        if self.in_progress and self.frame < self.animation_step:
            current_image = self.images[self.frame]
            resized_image = pygame.transform.scale(current_image, (current_image.get_width() // self.zoom, current_image.get_height() // self.zoom))
            screen.blit(resized_image, self.rect.topleft)