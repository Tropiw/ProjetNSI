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
        #init pygame
        pygame.init()

        #definit le tile set (pas sur que ce soit utile)
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')

        #definit l'affichage, les fps et autre parametre du genre
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.running = True

        #Musique
        pygame.mixer.init()
        pygame.mixer.music.load(r'SFX\robot rock.mp3')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.008) #0.008

        #definit la liste des objets, des monstres present sur la map 
        self.objects = []  # Liste pour stocker les objets à dessiner

        #fini par definir le menu, la pos de la souris(pas vraiment la pos juste pour pas que ca bug) et le mode(si on est dans un menu ou dans le jeu)
        self.main_menu = menu.menu()
        self.mouse_pos = (0,0)
        self.mode = 2

        #defini le donjon actuelle
        self.donjon = map_module.Dongeon(self.screen,1280,720)
        self.actual_room = self.donjon.map_list[self.donjon.actual_room]

        #player groupe
        self.player_group = pygame.sprite.Group()
        player1_movement_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight run Sprite-sheet 16x17.png'
        player1_idle_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight idle Sprite-sheet 16x16.png'
        player2_movement_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight run Sprite-sheet 16x17.png'
        player2_idle_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight idle Sprite-sheet 16x16.png'
        
        self.player1 = perso.Player(player1_movement_image, player1_idle_image,(600, 100), 1, self.actual_room.enemies_group, item_group=self.actual_room.item_group)
        self.player2 = perso.Player(player2_movement_image, player2_idle_image,(500, 100), 2, self.actual_room.enemies_group, item_group=self.actual_room.item_group)
        self.player_group.add(self.player1)
        self.player_group.add(self.player2)
        
        
        #ORDRE : objects[map_assets, item_group, player_group, enemies_group]
        self.objects = [self.actual_room.map_assets,
                        self.actual_room.item_group,
                        self.player_group,
                        self.actual_room.enemies_group
                        ]
        # Son GAME OVER
        self.sfx_game_over = pygame.mixer.Sound(r"SFX\game_over.mp3")
        self.sfx_game_over.set_volume(0.07)

    def start(self): 
        while self.running:  # Code de boucle principale
            while self.mode == 1:
                self.handle_events()
                self.clock.tick(90)  # Temps écoulé entre chaque itération de la boucle est contrôlé, ce qui maintient la vitesse du jeu constante
                self.donjon.blit_map()
                self.update()
                self.render()                
                pygame.display.flip()

            while self.mode == 2:
                self.collision = self.main_menu.render_main_menu(self.screen)
                self.handle_events()
                if menu.point_in_rect(self.mouse_pos,self.collision):
                    self.mouse_pos = (0,0)
                    self.mode = 1
                pygame.display.flip()
            
            while self.mode == 3:
                self.collision = self.main_menu.render_game_over(self.screen)
                self.handle_events()
                if menu.point_in_rect(self.mouse_pos,self.collision):
                    self.reset_all()
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
                    
            
                    
    
    def update(self): 
        if  menu.pass_through(self.player1,self.player2,self.actual_room.sortie):
                    #on change de salle 
                    self.donjon.room_index += 1
                    self.donjon.actual_room = self.donjon.topologie[self.donjon.room_index]
                    self.actual_room  = self.donjon.map_list[self.donjon.actual_room]

                    #on tp les joueur
                    self.player1.rect[self.actual_room.sens_tp_entrer] = self.actual_room.tp_entrer  # TP le joueur 1
                    self.player2.rect[self.actual_room.sens_tp_entrer] = self.actual_room.tp_entrer  # TP le joueur 2

                    #on redefinit les objs et les enemies
                    self.objects[3] = self.actual_room.enemies_group
                    self.player1.enemies =  self.objects[3]
                    self.player2.enemies =  self.objects[3]
                    self.objects[0] = self.actual_room.map_assets
                    self.objects[1] = self.actual_room.item_group
                    self.player1.item_group =  self.objects[1]
                    self.player2.item_group =  self.objects[1]

                    
        elif menu.pass_through(self.player1,self.player2,self.actual_room.entrer):

                    #on change de salle 
                    self.donjon.room_index -= 1
                    self.donjon.actual_room = self.donjon.topologie[self.donjon.room_index]
                    self.actual_room  = self.donjon.map_list[self.donjon.actual_room]

                    #on tp les joueur
                    self.player1.rect[self.actual_room.sens_tp_sortie] = self.actual_room.tp_sortie   # TP le joueur 1
                    self.player2.rect[self.actual_room.sens_tp_sortie] = self.actual_room.tp_sortie    # TP le joueur 2

                    #on redefinit les objs et les enemies 
                    self.objects[3] = self.actual_room.enemies_group
                    self.player1.enemies =  self.objects[3]
                    self.player2.enemies =  self.objects[3]
                    self.objects[0] = self.actual_room.map_assets
                    self.objects[1] = self.actual_room.item_group
                    self.player1.item_group =  self.objects[1]
                    self.player2.item_group =  self.objects[1]
        


        if not self.player1.is_alive and not self.player2.is_alive: # Si les 2 joueur sont mort
                    self.sfx_game_over.play()
                    self.mode = 3  # Menu game over
        
        
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

    def reset_all(self):
        self.main_menu.nouveau_msg()
        self.mouse_pos = (0,0)
        self.mode = 2

        #defini le donjon actuelle
        self.donjon = map_module.Dongeon(self.screen,1280,720)
        self.actual_room = self.donjon.map_list[self.donjon.actual_room]
        #player groupe
        self.player_group = pygame.sprite.Group()
        player1_movement_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight run Sprite-sheet 16x17.png'
        player1_idle_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Blue Knight idle Sprite-sheet 16x16.png'
        player2_movement_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight run Sprite-sheet 16x17.png'
        player2_idle_image = r'Graphic\Peros\-No Shield - Sprite Sheet\Red Knight idle Sprite-sheet 16x16.png'
        
        self.player1 = perso.Player(player1_movement_image, player1_idle_image,(600, 100), 1, self.actual_room.enemies_group, item_group=self.actual_room.item_group)
        self.player2 = perso.Player(player2_movement_image, player2_idle_image,(500, 100), 2, self.actual_room.enemies_group, item_group=self.actual_room.item_group)
        self.player_group.add(self.player1)
        self.player_group.add(self.player2)
        
        
        #ORDRE : objects[map_assets, item_group, player_group, enemies_group]
        self.objects = [self.actual_room.map_assets,
                        self.actual_room.item_group,
                        self.player_group,
                        self.actual_room.enemies_group
                        ]
    


# UTILISATION
jeu = Main()

# Lancer le jeu
jeu.start()

