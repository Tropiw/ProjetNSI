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
    def __init__(self, position, radius, color, speed=10):
        super().__init__(position, radius, color) #'super'-->  héritage fonction circle
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            if self.position.y > 110 :
                self.position.y -= self.speed
        if keys[pygame.K_s]:
            if self.position.y < 640 - self.radius:
                self.position.y += self.speed
        if keys[pygame.K_q]:
            if self.position.x > 80 + self.radius:
                self.position.x -= self.speed
        if keys[pygame.K_d]:
            if self.position.x < 1200 - self.radius:
                self.position.x += self.speed
                
            
class Player2(Player):
    def __init__(self, position, radius, color, speed=10):
        super().__init__(position, radius, color, speed=10) #'super'-->  héritage fonction circle
        self.speed = speed

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
    def __init__(self, position, radius, color, speed=1):
        super().__init__(position, radius, color)
        self.speed = speed
    
    def update(self):
        if self.position.x < 1200 - self.radius:
            self.position.x += self.speed