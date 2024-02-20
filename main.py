import pygame
import Imagesetter as image

class Main:
    def __init__(self, fps=60, width=1280, height=720):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen_debug = pygame.Surface((1280,720))
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True
        self.objects = []  # Liste pour stocker les objets à dessiner
        
    def start(self):
        self.mapdebug()
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)  # Limiter le taux de rafraîchissement
            
        pygame.quit()
            
    def handle_events(self):          # Le jeu s'arrête quand on clique sur fermer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for obj in self.objects:
            obj.update()  # Appel à la méthode update de chaque objet
        
    def mapdebug(self):
        image.tile.blit_tile(self.screen_debug,(5,5),(0,0))
        image.tile.blit_tile(self.screen_debug,(6,5),(1200,0))
        image.tile.blit_tile(self.screen_debug,(6,6),(1200,640))
        image.tile.blit_tile(self.screen_debug,(5,6),(0,640)) #Les coins 
        for i in range(14):
            image.tile.blit_tile(self.screen_debug,(3,6),((i+1)*80,0))
            image.tile.blit_tile(self.screen_debug,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                image.tile.blit_tile(self.screen_debug,(4,5),(0,(j+1)*80))
                image.tile.blit_tile(self.screen_debug,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                image.tile.blit_tile(self.screen_debug,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        
        self.screen.blit(self.screen_debug,(0,0))

    def render(self):
        for obj in self.objects:
            obj.draw(self.screen,self.screen_debug)


class Circle:
    def __init__(self, position, radius, color):
        self.position = pygame.Vector2(position) # Vecteur convertie coordonnées (100,200) en x=100 et y =200
        self.ancienne_position = (-int(self.position.x-radius),-int(self.position.y-radius))
        print(self.ancienne_position)
        self.radius = radius
        self.color = color
        self.background = 0
    
    def draw(self, screen, screen_ref):
        self.background = pygame.Surface((self.radius*2,self.radius*2))
        self.background.blit( screen_ref,self.ancienne_position) 
        print(self.ancienne_position)
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
            if self.position.y > 80 :
                self.ancienne_position = (-int(self.position.x-self.radius),-int(self.position.y-self.radius))
                self.position.y -= self.speed
        if keys[pygame.K_s]:
            if self.position.y < 640 - self.radius:
                self.ancienne_position = (-int(self.position.x-self.radius),-int(self.position.y-self.radius))
                self.position.y += self.speed
        if keys[pygame.K_q]:
            if self.position.x > 80 + self.radius:
                self.ancienne_position = (-int(self.position.x-self.radius),-int(self.position.y-self.radius))
                self.position.x -= self.speed
        if keys[pygame.K_d]:
            if self.position.x < 1200 - self.radius:
                self.ancienne_position = (-int(self.position.x-self.radius+2),-int(self.position.y-self.radius+2))
                self.position.x += self.speed
            
class Ennemy(Circle):
    def __init__(self, position, radius, color, speed=1):
        super().__init__(position, radius, color)
        self.speed = speed
    
    def update(self):
        if self.position.x < 1200 - self.radius:
            self.ancienne_position = (-int(self.position.x-self.radius+1),-int(self.position.y-self.radius))
            self.position.x += self.speed
            

# Exemple d'utilisation
jeu = Main()

# Créer le joueur
player = Player((100, 100), 30, (255, 0, 0),3)

# Créer l'obstacle (cercle immobile)
obstacle = Circle((200, 200), 30, (0, 255, 0))

# Créer l'ennemi
ennemi = Ennemy((500,50), 25,(56,23,145))

# Liste d'objets à afficher
jeu.objects = [player, obstacle, ennemi]

# Lancer le jeu
jeu.start()
