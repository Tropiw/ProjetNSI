import pygame
import Imagesetter as image

class Circle:
    def __init__(self, position, radius, color):
        self.position = pygame.Vector2(position) # Vecteur convertie coordonnées (100,200) en x=100 et y =200
        self.radius = radius
        self.color = color
        self.background = 0
    
    def draw(self, screen, screen_debug):
        self.background = pygame.Surface((self.radius*2,self.radius*2))
        screen.blit(self.background, (self.position.x-self.radius,self.position.y-self.radius))
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self):
        pass  # Les cercles n'ont pas besoin d'être mis à jour

class circle_Player(Circle):
    def __init__(self, position, radius, color, speed=1 ,player = 1):
        super().__init__(position, radius, color) #'super'-->  héritage fonction circle
        self.speed = speed
        self.player = player
        if player == 1:
            self.movement = [pygame.K_z,pygame.K_s,pygame.K_q,pygame.K_d] #attribuer les touches au joueur 1
        else:
            self.movement= [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT] #attribuer les touches au joueur 2

    def update(self):                               #attribution des touche du joueur au mouvement 
        keys = pygame.key.get_pressed()
        if keys[self.movement[0]]:
            if self.position.y > 110 :
                self.position.y -= self.speed
        if keys[self.movement[1]]:
            if self.position.y < 640 - self.radius:
                self.position.y += self.speed
        if keys[self.movement[2]]:
            if self.position.x > 80 + self.radius:
                self.position.x -= self.speed
        if keys[self.movement[3]]:
            if self.position.x < 1200 - self.radius:
                self.position.x += self.speed
                
                
class Ennemy(Circle):
    def __init__(self, position, radius, color, speed=0.1):
        super().__init__(position, radius, color)
        self.speed = speed
    
    def update(self):
        if self.position.x < 1200 - self.radius:
            self.position.x += self.speed
            
            


import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, position, tile_size, player=1):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(position[0], position[1], tile_size[0], tile_size[1])
        self.tile_size = tile_size
        self.tile_position = (0, 0)
        self.player = player
        if player == 1:
            self.movement = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]  # attribuer les touches au joueur 1
        else:
            self.movement = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]  # attribuer les touches au joueur 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.movement[0]]:  # Touche Z ou flèche haut
            if self.rect.y > 26:
                self.rect.y -= 1
        if keys[self.movement[1]]:  # Touche S ou flèche bas
            if self.rect.y < 502:
                self.rect.y += 1
        if keys[self.movement[2]]:  # Touche Q ou flèche gauche
            if self.rect.x > 20:
                self.rect.x -= 1
        if keys[self.movement[3]]:  # Touche D ou flèche droite
            if self.rect.x < 1070:
                self.rect.x += 1
        print(self.rect)

    def draw(self, screen):
        tile_image = self.image.subsurface(pygame.Rect(self.tile_position[0] * self.tile_size[0],
                                                       self.tile_position[1] * self.tile_size[1],
                                                       self.tile_size[0], self.tile_size[1]))
        w = tile_image.get_width()
        h = tile_image.get_height()
        tile_image_upscaled = pygame.transform.scale(tile_image, (w * 6, h * 6)) #grandir la tile du perso car trop petite
        screen.blit(tile_image_upscaled, self.rect.topleft)