import pygame
import Imagesetter as image

class Main:
    def __init__(self, fps=60, width=1280, height=720):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True
        
    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.render(*self.objects)  # Appel à la méthode render avec les objets à dessiner
            pygame.display.flip()

        pygame.quit()
            
    def render(self, *objects):
        for obj in objects:
            self.screen.blit(obj, (0,0))


class Circle:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

# Exemple d'utilisation
DEBUG = image.tile('Graphic\Dungeon Gathering Free Version\Set 1.1.png')
DEBUG_MAP = [DEBUG.load(2,2)]
jeu = Main(60)
circle1 = Circle((100, 100), 50, (255, 0, 0))
circle2 = Circle((200, 200), 30, (0, 255, 0))
jeu.objects = [DEBUG_MAP]  # Stockez les objets à dessiner dans une liste
jeu.start()
