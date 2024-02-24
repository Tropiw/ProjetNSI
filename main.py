import pygame
import Imagesetter as image
import menu as menu
import personnage as perso
import map_module as map_module

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
        testmap = map_module.Dongeon(self.screen_debug) # Appeller
        testmap.map2()  # Appeler la méthode map2() du module map 
        
        title = menu.menu()
        collision = title.render_main_menu(self.screen)
        self.clock.tick(60)
        while self.running:
            # Votre code de boucle principale ici
            self.screen.blit(self.screen_debug,(0,0))
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
        pygame.quit()
            
    def handle_events(self):          # Le jeu s'arrête quand on clique sur fermer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for obj in self.objects:
            obj.update()  # Appel à la méthode update de chaque objet
        
    def render(self):
        for obj in self.objects:
            if isinstance(obj, perso.Player):  # Vérifie si l'objet est une instance de Player
                obj.draw(self.screen)
            else:
                obj.draw(self.screen, self.screen_debug)




# Exemple d'utilisation
jeu = Main()

# peros
# Chargement de l'image du personnage
player_image_path = "Graphic\perso\Sprites\Prototype\Prototype_Worksheet.png"

# Taille d'une tile sur l'image (en pixels)
tile_size = (32, 32)

# Création de l'instance du joueur
player_sprite = perso.Player(player_image_path, (100, 100), tile_size,1)
player_sprite2 = perso.Player(player_image_path, (100, 100), tile_size,2)

# Créer le joueur
player = perso.circle_Player((100, 500), 30, (255, 0, 0),0.8,1)
player2 = perso.circle_Player((100, 500), 30, (255, 150, 0),0.8,2)
# Créer l'obstacle (cercle immobile)
obstacle = perso.Circle((200, 200), 30, (0, 255, 0))

# Créer l'ennemi
ennemi = perso.Ennemy((500,200), 25,(56,23,145))


# Liste d'objets à afficher
jeu.objects = [ obstacle, ennemi, player_sprite, player_sprite2]

# Lancer le jeu
jeu.start()


#.convert_alpha()