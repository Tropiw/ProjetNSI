import pygame
import Imagesetter as image
import menu as menu
import personnage as perso
import map_module as map_module
import item as item
from pygame.locals import *
from enemy_module import Enemy

class Main:
    def __init__(self, fps=60, width=1280, height=720):
        #init pygame
        pygame.init()

        #definit le tile set (pas sur que ce soit utile)
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')

        #definit l'affichage, les fps et autre parametre du genre
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True

        #definit la liste des objets, des monstres present sur la map 
        self.objects = []  # Liste pour stocker les objets à dessiner
        self.ennemies_group = pygame.sprite.Group()

        #fini par definir le menu, la pos de la souris(pas vraiment la pos juste pour pas que ca bug) et le mode(si on est dans un menu ou dans le jeu)
        self.main_menu = menu.menu()
        self.mouse_pos = (0,0)
        self.mode = 2

        #defini le donjon actuelle
        self.donjon = map_module.Dongeon(self.screen,1280,720)

    def start(self,player1,player2): 
        title = menu.menu()
        while self.running: # Code de boucle principale
            while self.mode == 1:
                self.handle_events()
                self.clock.tick(90)  # Temps écoulé entre chaque itération de la boucle est contrôlé, ce qui maintient la vitesse du jeu constante
                self.donjon.blit_map()
                self.update()
                self.render()
                if  menu.rect_in_rect(player1.rect,self.donjon.map_list[self.donjon.actual_room].sortie) and menu.rect_in_rect(player2.rect,self.donjon.map_list[self.donjon.actual_room].sortie):
                    self.donjon.actual_room = self.donjon.topologie[self.donjon.room_index+1]
                    player1.rect[1] = 500
                    player2.rect[1] = 500
                    self.objects[3] = self.donjon.map_list[self.donjon.actual_room].enemies_group
                pygame.display.flip()
            self.collision = title.render_main_menu(self.screen)
            while self.mode == 2:
                self.handle_events()
                if menu.point_in_rect(self.mouse_pos,self.collision):
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

# ENNEMIS

player_group = pygame.sprite.Group()



# Items
item_group = pygame.sprite.Group()
sword1 = item.AnimatedSword((600,500))
sword2 = item.AnimatedSword((800,500))
item_group.add(sword1, sword2)

# JOUEUR

player1 = perso.Player(r"Graphic\Player\Sprites\Prototype\worksheet_blue.png", (500, 100), 1, jeu.donjon.map_list[jeu.donjon.actual_room].enemies_group, item_group=item_group)
player2 = perso.Player(r"Graphic\Player\Sprites\Prototype\worksheet_red.png", (600, 100), 2, jeu.donjon.map_list[jeu.donjon.actual_room].enemies_group, item_group=item_group)
player_group.add(player1)
player_group.add(player2)


# OBSTACLE
map_assets = pygame.sprite.Group()

obstacle1 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (100, 500), (16, 16), (8, 6))
obstacle2 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (200, 500), (16, 16), (8, 6))
obstacle3 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                          (400, 500), (16, 16), (9, 6))

slime2 = image.ImageStatique(r'Graphic\Slime - Enemy\slime2.png',position=(800, 425),zoom=0.2)

# PIECE ANIMEE
coin_paths = []
for i in range(1,5): # Chemin des image étapes d'animations de la pièce
    coin_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_{i}.png')

coin1 = image.animated_sprite(coin_paths, (1145, 575))
coin2 = image.animated_sprite(coin_paths, (1100, 575))
coin3 = image.animated_sprite(coin_paths, (1055, 575))


# Remplissage du groupe d'asset de la map
map_assets.add(coin1,coin2,coin3,obstacle1,obstacle2,obstacle3,slime2)


#TESTS

# Liste d'objets à afficher
jeu.objects = [ map_assets, player_group, item_group]
jeu.objects.append(jeu.donjon.map_list[jeu.donjon.actual_room].enemies_group)


#Musique
pygame.mixer.init()
pygame.mixer.music.load(r'SFX\robot rock.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.008)

# Lancer le jeu
jeu.start(player1, player2)

