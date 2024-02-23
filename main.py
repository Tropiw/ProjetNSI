import pygame
import Imagesetter as image
import menu as menu
import personnage as perso
import map as map

class Main:
    def __init__(self, fps=60, width=1280, height=720):
        pygame.init()
        self.tile_set = image.tile('Graphic/Dungeon Gathering Free Version/Set 1.1.png')
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)

        self.screen = pygame.display.set_mode((width, height))
        print(self.screen)
        self.screen_debug = pygame.Surface((1280,720))
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True
        self.objects = []  # Liste pour stocker les objets à dessiner
        
    def start(self):
        
        self.mapdebug()
        title = menu.menu()
        collision = title.render_main_menu(self.screen)
        self.clock.tick(60)
        while self.running:
            '''mouse_pos = pygame.mouse.get_pos()
            if title.in_rect(mouse.pos,collision):
            '''
            
            #else:            #ça fait crash python, c'est surement le ifZ
            self.screen.blit(self.screen_debug,(0,0))
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
              # Limiter le taux de rafraîchissement
            self.handle_events()
        pygame.quit()
            
    def handle_events(self):          # Le jeu s'arrête quand on clique sur fermer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for obj in self.objects:
            obj.update()  # Appel à la méthode update de chaque objet
        
    def mapdebug(self):
        self.tile_set.blit_tile(self.screen_debug,(5,5),(0,0))
        self.tile_set.blit_tile(self.screen_debug,(6,5),(1200,0))
        self.tile_set.blit_tile(self.screen_debug,(6,6),(1200,640))
        self.tile_set.blit_tile(self.screen_debug,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set.blit_tile(self.screen_debug,(3,6),((i+1)*80,0))
            self.tile_set.blit_tile(self.screen_debug,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set.blit_tile(self.screen_debug,(4,5),(0,(j+1)*80))
                self.tile_set.blit_tile(self.screen_debug,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set.blit_tile(self.screen_debug,(12,4),((i+1)*80,(j+1)*80)) #Le milieux

    def render(self):
        for obj in self.objects:
            obj.draw(self.screen,self.screen_debug)



# Exemple d'utilisation
jeu = Main()

# Créer le joueur
player = perso.Player((100, 500), 30, (255, 0, 0),0.8,1)
player2 = perso.Player((100, 500), 30, (255, 150, 0),0.8,2)
# Créer l'obstacle (cercle immobile)
obstacle = perso.Circle((200, 200), 30, (0, 255, 0))

# Créer l'ennemi
ennemi = perso.Ennemy((500,200), 25,(56,23,145))


# Liste d'objets à afficher
jeu.objects = [player, obstacle, ennemi, player2]

# Lancer le jeu
jeu.start()


#.convert_alpha()