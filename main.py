import pygame
import Imagesetter as image
import menu as menu
import personnage as perso
import map_module as map_module

class Main:
    def __init__(self, fps=60, width=1280, height=720):
        pygame.init()
        self.tile_set = image.tile('Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
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
        while self.running:
            # Code de boucle principale
            self.clock.tick(90)  # Temps écoulé entre chaque itération de la boucle est contrôlé, ce qui maintient la vitesse du jeu constante
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
                obj.draw(self.screen)




# UTILISATION

jeu = Main()

# PERSO

# Taille d'une tile sur l'image (en pixels)
tile_size = (32, 32)

# Création des joueurs
player = perso.Player(r"Graphic\Player\Sprites\Prototype\worksheet_blue.png", (500, 100), tile_size,1)
player2 = perso.Player(r"Graphic\Player\Sprites\Prototype\worksheet_red.png", (600, 100), tile_size,2)



# obstacles
obstacle = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (100, 500), (16, 16), (8, 6))
obstacle2 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (200, 500), (16, 16), (8, 6))
obstacle3 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (400, 500), (16, 16), (9, 6))


#ennemi
enemy = perso.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,300), (32,25), speed = 5)


#Pilier
image_path = r"Graphic\Dungeon Gathering - map asset (light)\Structure.png"
pilier = image.Image_statique(image_path, position=(100, 100))  # Positionnez l'image à (100, 100) sur l'écran
pilier2 = image.Image_statique(image_path, position=(1125, 100))  # Positionnez l'image à (100, 100) sur l'écran

slime2 = image.Image_statique(r'Graphic\Slime - Enemy\slime2.png',position=(800, 425),zoom=0.2)

# Liste d'objets à afficher
jeu.objects = [ slime2, obstacle, obstacle2, obstacle3, player, player2, pilier, pilier2, enemy]

#Musique
pygame.mixer.init()
pygame.mixer.music.load(r'SFX\robot rock.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.008)

# Lancer le jeu
jeu.start()

