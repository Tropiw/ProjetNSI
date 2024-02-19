import pygame
import Imagesetter as image

class Main:
    DEBUG_MAP = [((5,5),(0,0)),((3,6),(80,0)),((3,6),(160,0)),((4,5),(0,80)),((11,0),(80,80))]
    def __init__(self, fps=60, width=1280, height=720):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True
        self.objects = []  # Liste pour stocker les objets à dessiner
        
    def start(self):
        while self.running:
            self.handle_events()
            self.mapdebug()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)  # Limiter le taux de rafraîchissement
            
        pygame.quit()
            
    def handle_events(self):          #le jeu s'arrête quand on clique sur fermer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for obj in self.objects:
            obj.update()  # Appel à la méthode update de chaque objet
        
    def mapdebug(self):
        image.tile.blit_tile(self.screen,(5,5),(0,0))
        for i in range(14):
            image.tile.blit_tile(self.screen,(3,6),((i+1)*80,0))
        image.tile.blit_tile(self.screen,(6,5),(1200,0))



    def render(self):
        for obj in self.objects:
            obj.draw(self.screen)


class Circle:
    def __init__(self, position, radius, color):
        self.position = pygame.Vector2(position) #vecteur convertie coordonnées (100,200) en x=100 et y =200
        self.radius = radius
        self.color = color
    
    def draw(self, screen):
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
            self.position.y -= self.speed
        if keys[pygame.K_s]:
            self.position.y += self.speed
        if keys[pygame.K_q]:
            self.position.x -= self.speed
        if keys[pygame.K_d]:
            self.position.x += self.speed
            
class Ennemy(Circle):
    def __init__(self, position, radius, color, speed=1):
        super().__init__(position, radius, color)
        self.speed = speed
    
    def update(self):
        self.position.x += self.speed

# Exemple d'utilisation
jeu = Main()

# Créer le joueur
player = Player((100, 100), 50, (255, 0, 0))

# Créer l'obstacle (cercle immobile)
obstacle = Circle((200, 200), 30, (0, 255, 0))

# Créer l'ennemi
ennemi = Ennemy((500,50), 25,(56,23,145))

# Liste d'objets à afficher
jeu.objects = [player, obstacle, ennemi]

# Lancer le jeu
jeu.start()
