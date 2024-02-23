import pygame

class Circle:
    def __init__(self, position, radius, color):
        self.position = pygame.Vector2(position) # Vecteur convertie coordonnées (100,200) en x=100 et y =200
        self.radius = radius
        self.color = color
        self.background = 0
    
    def draw(self, screen, screen_ref):
        self.background = pygame.Surface((self.radius*2,self.radius*2))
        screen.blit(self.background, (self.position.x-self.radius,self.position.y-self.radius))
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self):
        pass  # Les cercles n'ont pas besoin d'être mis à jour

class Player(Circle):
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
                
            
class Player2(Player):
    def __init__(self, position, radius, color, speed=1):
        super().__init__(position, radius, color, speed) #'super'-->  héritage fonction circle

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.position.y > 110 :
                self.position.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.position.y < 640 - self.radius:
                self.position.y += self.speed
        if keys[pygame.K_LEFT]:
            if self.position.x > 80 + self.radius:
                self.position.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.position.x < 1200 - self.radius:
                self.position.x += self.speed
                
                
class Ennemy(Circle):
    def __init__(self, position, radius, color, speed=0.1):
        super().__init__(position, radius, color)
        self.speed = speed
    
    def update(self):
        if self.position.x < 1200 - self.radius:
            self.position.x += self.speed