import pygame
import imagesetter as image
import menu as menu
import personnage as perso
import map_module as map_module
import item as item
from pygame.locals import *
from enemy_module import Enemy

class Main:
    def __init__(self, fps=60, width=1280, height=720):
        pygame.init()
        self.tile_set = image.tile('Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.screen = pygame.display.set_mode((width, height))
        print(self.screen)
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True
        self.objects = []  # Liste pour stocker les objets à dessiner
        self.ennemies_group = pygame.sprite.Group()
        tile_set = image.tile('Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.main_menu = menu.menu()
        self.mouse_pos = (0,0)
        self.mode = 2
        self.donjon = map_module.Dongeon(self.screen,1280,720)
        self.screen_debug = self.donjon.dico_map["map_2"]

    def start(self): 
        title = menu.menu()
        while self.running: # Code de boucle principale
            while self.mode == 1:
                self.handle_events()
                self.clock.tick(90)  # Temps écoulé entre chaque itération de la boucle est contrôlé, ce qui maintient la vitesse du jeu constante
                self.screen.blit(self.screen_debug.background,(0,0))
                self.update()
                self.render()
                pygame.display.flip()
            self.collision = title.render_main_menu(self.screen)
            while self.mode == 2:
                self.handle_events()
                if self.main_menu.in_rect(self.mouse_pos,self.collision):
                    self.mode = 1
                pygame.display.flip()

        pygame.quit()
            
    def handle_events(self):          # Le jeu s'arrête quand on clique sur fermer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.mode = 0
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:  # Vérifie si un clic de souris a eu lieu
                if event.button == 1:  # Vérifie si le clic était le bouton gauche de la souris
                    # Obtient les coordonnées du clic
                    self.mouse_pos = pygame.mouse.get_pos()
                    
                    # Afficher les coordonnées du clic dans la console
                    print("Clic à la position :", self.mouse_pos)
            
                    

    def update(self):
        for obj in self.objects:
            if isinstance(obj, pygame.sprite.Group):
                for sprite in obj.sprites():
                    sprite.update()
            else:
                obj.update()

    def render(self):
        for obj in self.objects:
            if isinstance(obj, pygame.sprite.Group):
                for sprite in obj.sprites():
                    sprite.draw(self.screen)
            else:
                obj.draw(self.screen)





# UTILISATION

jeu = Main()

# PERSO

# Taille d'une tile sur l'image (en pixels)
tile_size = (32, 32)

#ennemi
enemies_group = pygame.sprite.Group()

enemy = Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,300), (32,25), speed = 5)
enemies_group.add(enemy)

# Création des joueurs
player = perso.Player(r"Graphic\Player\Sprites\Prototype\worksheet_blue.png", (500, 100), tile_size,1, enemies_group)
player2 = perso.Player(r"Graphic\Player\Sprites\Prototype\worksheet_red.png", (600, 100), tile_size,2, enemies_group)



# obstacles
obstacle = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (100, 500), (16, 16), (8, 6))
obstacle2 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (200, 500), (16, 16), (8, 6))
obstacle3 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (400, 500), (16, 16), (9, 6))


#Pilier
image_path = r"Graphic\Dungeon Gathering - map asset (light)\Structure.png"
pilier = image.Image_statique(image_path, position=(100, 100))  # Positionnez l'image à (100, 100) sur l'écran
pilier2 = image.Image_statique(image_path, position=(1125, 100))  # Positionnez l'image à (100, 100) sur l'écran

slime2 = image.Image_statique(r'Graphic\Slime - Enemy\slime2.png',position=(800, 425),zoom=0.2)

#pièce animée

coin_paths = [r'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_1.png',
              r'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_2.png',
              r'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_3.png',
              r'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_4.png']

coin1 = image.animated_sprite(coin_paths, (1145, 575))
coin2 = image.animated_sprite(coin_paths, (1100, 575))
coin3 = image.animated_sprite(coin_paths, (1055, 575))

# Liste d'objets à afficher
jeu.objects = [ slime2, obstacle, obstacle2, obstacle3, coin1, coin2, coin3, player, player2, pilier, pilier2, enemies_group]


#Musique
pygame.mixer.init()
pygame.mixer.music.load(r'SFX\robot rock.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.008)

# Lancer le jeu
jeu.start()

