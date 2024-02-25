import pygame
import Imagesetter as image

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, position, tile_size, player=1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        # rect pour gerer la position puis les collision facilement 
        # position[0], position[1] pour recuperer position x,y 
        # tile_size[0], tile_size[1] pour taille x,y de la tile (32x32 ici)
        self.tile_size = tile_size
        self.tile_position = (0, 0)
        self.player = player
        if player == 1:
            self.movement = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]  # attribuer les touches au joueur 1
        else:
            self.movement = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]  # attribuer les touches au joueur 2
        self.sfx_move = pygame.mixer.Sound(r"SFX\footstep mc (2).mp3")
        self.is_moving = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Mouvement vers le haut
        if keys[self.movement[0]]:  
            if self.rect.y > 26:
                self.rect.y -= 5
            if not self.is_moving:
                self.sfx_move.play(loops=-1)
                self.is_moving = True
        # Mouvement vers le bas
        elif keys[self.movement[1]]:
            if self.rect.y < 502:
                self.rect.y += 5
            if not self.is_moving:
                self.sfx_move.play(loops=-1)
                self.is_moving = True
        # Mouvement vers la gauche
        elif keys[self.movement[2]]:
            if self.rect.x > 20:
                self.rect.x -= 5
            if not self.is_moving:
                self.sfx_move.play(loops=-1)
                self.is_moving = True
        # Mouvement vers la droite
        elif keys[self.movement[3]]:
            if self.rect.x < 1070:
                self.rect.x += 5
            if not self.is_moving:
                self.sfx_move.play(loops=-1)
                self.is_moving = True
        else:
            if self.is_moving:
                self.sfx_move.stop()
                self.is_moving = False


    def draw(self, screen):
        tile_image = self.image.subsurface(pygame.Rect(self.tile_position[0] * self.tile_size[0],
                                                       self.tile_position[1] * self.tile_size[1],
                                                       self.tile_size[0], self.tile_size[1]))
        w = tile_image.get_width()
        h = tile_image.get_height()
        tile_image_upscaled = pygame.transform.scale(tile_image, (w * 6, h * 6)) # Grandir la tile du perso car trop petite
        screen.blit(tile_image_upscaled, self.rect.topleft) # Renvoie un tuple x,y du haut gauche, positionner ici
        

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

