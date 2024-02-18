import pygame

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
            obj.draw(self.screen)

class Circle:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

# Exemple d'utilisation
jeu = Main(60)
circle1 = Circle((100, 100), 50, (255, 0, 0))
circle2 = Circle((200, 200), 30, (0, 255, 0))
jeu.objects = [circle1, circle2]  # Stockez les objets à dessiner dans une liste
jeu.start()
