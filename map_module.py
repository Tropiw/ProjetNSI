import pygame
import item as item
import imagesetter as image
import enemy_module as enemy
import random

class Map():
    def __init__(self, width,height):
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)

        
    
class map1(Map):
    def __init__(self ,width,height):
        
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()
        enemy1 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,80), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group, sens = 1)
        enemy2 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,400), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy3 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (600,500), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        self.enemies_group.add(enemy1)#, enemy2, enemy3

        
    
        

        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)

        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(8):
                self.tile_set1.load(i,j)

        #entrer et sortie
        self.porte_Nord =  porte(pygame.rect.Rect(560,0,160,80),200,self)

        self.porte_Est = None

        self.porte_Ouest = None

        self.porte_Sud = None

        


        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        
        self.obstacle2 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 10), (16,32), (0,0),4)#pillier 2 
        self.obstacle1 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 10), (16,32), (0,0),4)#pillier 1
        self.tile_set1.blit_tile(self.screen,(5,5),(0,0))
        self.tile_set1.blit_tile(self.screen,(6,5),(1200,0))
        self.tile_set1.blit_tile(self.screen,(6,6),(1200,640))
        self.tile_set1.blit_tile(self.screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set1.blit_tile(self.screen,(3,6),((i+1)*80,0))
            self.tile_set1.blit_tile(self.screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set1.blit_tile(self.screen,(4,5),(0,(j+1)*80))
                self.tile_set1.blit_tile(self.screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux 
        self.tile_set1.blit_tile(self.screen,(5,3),(560,0))# porte g
        self.tile_set1.blit_tile(self.screen,(6,3),(640,0))#porte d
        self.obstacle1.draw(self.screen) #pillier 1
        self.obstacle2.draw(self.screen) #pillier 2
        self.tile_set1.blit_tile(self.screen,(5,7),(310,410)) #support epee 1
        self.tile_set1.blit_tile(self.screen,(5,7),(880,410)) #support epee 2
        self.tile_set1.blit_tile(self.screen,(12,5),(800,160)) #sol insalubre1
        self.tile_set1.blit_tile(self.screen,(13,5),(880,160)) #sol insalubre2
        self.tile_set1.blit_tile(self.screen,(12,6),(800,240)) #sol insalubre3
        self.tile_set1.blit_tile(self.screen,(13,6),(880,240)) #sol insalubre4
        self.tile_set1.blit_tile(self.screen,(3,3),(320,0)) #mur trou1
        self.tile_set1.blit_tile(self.screen,(3,3),(880,0)) #mur trou2
        self.tile_set1.blit_tile(self.screen,(7,3),(480,0)) #mur cassé
        
        
        
        # PIECE ANIMEE
        coin_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            coin_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_{i}.png')


        coin1 = image.animated_sprite(coin_paths, (1145, 575))
        coin2 = image.animated_sprite(coin_paths, (1100, 575))
        coin3 = image.animated_sprite(coin_paths, (1055, 575))
    
        torch_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            torch_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\torch\torch_{i}.png')

        torch1 = image.animated_sprite(torch_paths, (1125, 45))
        torch2 = image.animated_sprite(torch_paths, (80, 45))
        torch3 = image.animated_sprite(torch_paths, (730, 0))

    
        # OBSTACLE
        obstacle1 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                                (100, 500), (16, 16), (8, 6))
        obstacle2 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                                (200, 500), (16, 16), (8, 6))
        obstacle3 = image.Obstacle(r"Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png",
                                (400, 500), (16, 16), (9, 6))
       
        self.map_assets = pygame.sprite.Group()
        
        # Remplissage du groupe d'asset de la map
        self.map_assets.add(coin1,coin2,coin3,obstacle1,obstacle2,obstacle3)
        self.map_assets.add(torch1,torch2,torch3)
       


        #Item group
        self.item_group = pygame.sprite.Group()
        sword1 = item.AnimatedSword((320,400))
        sword2 = item.AnimatedSword((890,400))
        
        potion_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            potion_paths.append(rf'C:\Users\tropi\Documents\GitHub\ProjetNSI\Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\flasks\flasks_1_{i}.png')
        
        potion = image.animated_sprite(potion_paths, (1125, 100))
        
        self.item_group.add(sword1, sword2, potion)
        
        
class map2(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()
        enemy1 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,200), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy2 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (300,300), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        self.enemies_group.add(enemy1, enemy2)

        #Designe les tile sets utiliser
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)


        #entrer et sortie
        self.porte_Nord = None
        
        self.porte_Est = None

        self.porte_Ouest = None

        self.porte_Sud = porte(pygame.rect.Rect(570, 560,160,80),350,self)


        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(18):
            for j in range(8):
                self.tile_set.load(i,j)
            for j in range(11):
                self.tile_set2.load(i,j)

        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        self.tile_set.blit_tile(self.screen,(5,5),(0,0))
        self.tile_set.blit_tile(self.screen,(6,5),(1200,0))
        self.tile_set.blit_tile(self.screen,(6,6),(1200,640))
        self.tile_set.blit_tile(self.screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set.blit_tile(self.screen,(3,6),((i+1)*80,0))
            self.tile_set.blit_tile(self.screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set.blit_tile(self.screen,(4,5),(0,(j+1)*80))
                self.tile_set.blit_tile(self.screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set2.blit_tile(self.screen,(7,4),(560,640))
        self.tile_set2.blit_tile(self.screen,(8,4),(640,640))
        self.tile_set.blit_tile(self.screen,(2,4),(720,640))
        self.tile_set.blit_tile(self.screen,(4,4),(480,640))

        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()
        
        

class map3(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()
        enemy1 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,300), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy2 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (300,400), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy3 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (600,40), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        self.enemies_group.add(enemy1, enemy2, enemy3)



        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)

        #entrer et sortie
        self.porte_Nord = None
        
        self.porte_Est = None

        self.porte_Ouest =  porte(pygame.rect.Rect(80,320,80,80),300,self)

        self.porte_Sud =  porte(pygame.rect.Rect(570, 560,160,80),350,self)


        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(16):
            for j in range(8):
                self.tile_set1.load(i,j)
            for j in range(11):
                self.tile_set2.load(i,j)
        
        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        
        self.obstacle1 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 10), (16,32), (0,0),4)#pillier 1
        self.obstacle2 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 10), (16,32), (0,0),4)#pillier 2
        self.obstacle3 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 480), (16,32), (0,0),4)#pillier3 3
        
    
        self.tile_set1.blit_tile(self.screen,(5,5),(0,0))
        self.tile_set1.blit_tile(self.screen,(6,5),(1200,0))
        self.tile_set1.blit_tile(self.screen,(6,6),(1200,640))
        self.tile_set1.blit_tile(self.screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set1.blit_tile(self.screen,(3,6),((i+1)*80,0))
            self.tile_set1.blit_tile(self.screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set1.blit_tile(self.screen,(4,5),(0,(j+1)*80))
                self.tile_set1.blit_tile(self.screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set2.blit_tile(self.screen,(9,2),(0,320))
        self.tile_set1.blit_tile(self.screen,(1,6),(0,240))
        self.tile_set1.blit_tile(self.screen,(4,4),(0,400))
        self.tile_set2.blit_tile(self.screen,(7,4),(560,640))
        self.tile_set2.blit_tile(self.screen,(8,4),(640,640))
        self.tile_set1.blit_tile(self.screen,(2,4),(720,640))
        self.tile_set1.blit_tile(self.screen,(4,4),(480,640))
        self.tile_set1.blit_tile(self.screen,(12,5),(800,160)) #sol insalubre hg
        self.tile_set1.blit_tile(self.screen,(13,5),(880,160)) #sol insalubre hd
        self.tile_set1.blit_tile(self.screen,(12,6),(800,240)) #sol insalubre bg
        self.tile_set1.blit_tile(self.screen,(13,6),(880,240)) #sol insalubre bd
        self.tile_set1.blit_tile(self.screen,(12,5),(160,480)) #sol insalubre1
        self.tile_set1.blit_tile(self.screen,(13,5),(240,480)) #sol insalubre2
        self.tile_set1.blit_tile(self.screen,(12,6),(160,556)) #sol insalubre3
        self.tile_set1.blit_tile(self.screen,(13,6),(240,556)) #sol insalubre4
        self.tile_set1.blit_tile(self.screen,(2,3),(320,0)) #mur trou1
        self.tile_set1.blit_tile(self.screen,(2,3),(400,0)) #mur trou1;1
        self.tile_set1.blit_tile(self.screen,(2,3),(880,0)) #mur trou2
        self.tile_set1.blit_tile(self.screen,(7,3),(1040,0)) #mur cassé1
        self.tile_set1.blit_tile(self.screen,(14,4),(160,160)) #sol cassé1
        self.tile_set1.blit_tile(self.screen,(15,4),(800,400)) #sol cassé3
        self.tile_set1.blit_tile(self.screen,(15,4),(960,560)) #sol cassé4
        
        self.obstacle1.draw(self.screen) #pillier 1
        self.obstacle2.draw(self.screen) #pillier 2
        self.obstacle3.draw(self.screen) #pillier 3
        
        
         
        


        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()

        # animations
        side_torch_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            side_torch_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\torch\side_torch_{i}.png')

        side_torch1 = image.animated_sprite(side_torch_paths, (80, 240))
        side_torch2 = image.animated_sprite(side_torch_paths, (80, 400))

        torch_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            torch_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\torch\torch_{i}.png')

        torch1 = image.animated_sprite(torch_paths, (1125, 45))
        torch2 = image.animated_sprite(torch_paths, (80, 45))
        torch3 = image.animated_sprite(torch_paths, (80, 520))

        self.map_assets.add(torch1,torch2,torch3)
        self.map_assets.add(side_torch1,side_torch2)

class map4(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()
        enemy1 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (160,80), (32,25), speed = 20, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy2 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (500,80), (32,25), speed = 20, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy3 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (800,80), (32,25), speed = 20, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy4 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (1024,80), (32,25), speed = 20, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy5 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (1120,80), (32,25), speed = 20, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        
        self.enemies_group.add(enemy1, enemy2, enemy3, enemy4, enemy5)


        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)


        #entrer et sortie
        self.porte_Nord = porte(pygame.rect.Rect(560,0,160,80),200,self)
        
        self.porte_Est =  porte(pygame.rect.Rect(1120,320,80,80),900,self)

        self.porte_Ouest = None

        self.porte_Sud = None


        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(18):
            for j in range(8):
                self.tile_set1.load(i,j)
            for j in range(11):
                self.tile_set2.load(i,j)
        
        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        
        self.obstacle1 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 10), (16,32), (0,0),4)#pillier 1
        self.obstacle2 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 10), (16,32), (0,0),4)#pillier 2
        self.obstacle3 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 480), (16,32), (0,0),4)#pillier 3
        self.obstacle4 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 480), (16,32), (0,0),4)#pillier 4
        
        
        self.tile_set1.blit_tile(self.screen,(5,5),(0,0))
        self.tile_set1.blit_tile(self.screen,(6,5),(1200,0))
        self.tile_set1.blit_tile(self.screen,(6,6),(1200,640))
        self.tile_set1.blit_tile(self.screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set1.blit_tile(self.screen,(3,6),((i+1)*80,0))
            self.tile_set1.blit_tile(self.screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set1.blit_tile(self.screen,(4,5),(0,(j+1)*80))
                self.tile_set1.blit_tile(self.screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set1.blit_tile(self.screen,(5,3),(560,0))# porte g
        self.tile_set1.blit_tile(self.screen,(6,3),(640,0))#porte d
        self.tile_set2.blit_tile(self.screen,(9,3),(1200,320))
        self.tile_set1.blit_tile(self.screen,(0,6),(1200,240))
        self.tile_set1.blit_tile(self.screen,(2,4),(1200,400))
        self.obstacle1.draw(self.screen) #pillier 1
        self.obstacle2.draw(self.screen) #pillier 2
        self.obstacle3.draw(self.screen) #pillier 3
        self.obstacle4.draw(self.screen) #pillier 4
        self.tile_set1.blit_tile(self.screen,(12,5),(800,160)) #sol insalubre hg
        self.tile_set1.blit_tile(self.screen,(13,5),(880,160)) #sol insalubre hd
        self.tile_set1.blit_tile(self.screen,(12,6),(800,240)) #sol insalubre bg
        self.tile_set1.blit_tile(self.screen,(13,6),(880,240)) #sol insalubre bd
        self.tile_set1.blit_tile(self.screen,(12,5),(160,480)) #sol insalubre1
        self.tile_set1.blit_tile(self.screen,(13,5),(240,480)) #sol insalubre2
        self.tile_set1.blit_tile(self.screen,(12,6),(160,556)) #sol insalubre3
        self.tile_set1.blit_tile(self.screen,(13,6),(240,556)) #sol insalubre4
        self.tile_set1.blit_tile(self.screen,(2,3),(320,0)) #mur trou1
        self.tile_set1.blit_tile(self.screen,(2,3),(400,0)) #mur trou1;1
        self.tile_set1.blit_tile(self.screen,(2,3),(880,0)) #mur trou2
        self.tile_set1.blit_tile(self.screen,(7,3),(1040,0)) #mur cassé1
        self.tile_set1.blit_tile(self.screen,(14,4),(160,160)) #sol cassé1
        self.tile_set1.blit_tile(self.screen,(15,4),(800,400)) #sol cassé3
        self.tile_set1.blit_tile(self.screen,(15,4),(960,560)) #sol cassé4


        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()


        side_torch_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            side_torch_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\torch\side_torch_{i}.png')

        side_torch1 = image.animated_sprite(side_torch_paths, (1137, 240), zoom = 6, reverse=True)
        side_torch2 = image.animated_sprite(side_torch_paths, (1137, 400), zoom = 6, reverse=True)

        torch_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            torch_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\torch\torch_{i}.png')

        torch1 = image.animated_sprite(torch_paths, (1125, 45))
        torch2 = image.animated_sprite(torch_paths, (80, 45))
        torch3 = image.animated_sprite(torch_paths, (80, 520))
        torch4 = image.animated_sprite(torch_paths, (1125, 520))

        self.map_assets.add(torch1,torch2,torch3,torch4)

        self.map_assets.add(side_torch1,side_torch2)




class map5(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()
        enemy1 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (160,80), (32,25), speed = 7, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy2 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (500,80), (32,25), speed = 7, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy3 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (800,240), (32,25), speed = 7, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy4 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (1024,480), (32,25), speed = 7, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy5 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (1120,920), (32,25), speed = 7, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        
        self.enemies_group.add(enemy1, enemy2, enemy3, enemy4, enemy5)
        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)


        #entrer et sortie
        self.porte_Nord = porte(pygame.rect.Rect(560,0,160,80),200,self)
        
        self.porte_Est =  None

        self.porte_Ouest = porte(pygame.rect.Rect(80,320,80,80),250,self)

        self.porte_Sud = None

        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(18):
            for j in range(8):
                self.tile_set1.load(i,j)
            for j in range(11):
                self.tile_set2.load(i,j)
        
        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        self.obstacle1 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 10), (16,32), (0,0),4)#pillier 1
        self.obstacle2 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 20), (16,32), (0,0),4)#pillier 2
        self.obstacle3 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 480), (16,32), (0,0),4)#pillier 3
        self.obstacle4 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 480), (16,32), (0,0),4)#pillier 4
        self.obstacle5 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (480, 10), (16,32), (0,0),4)#pillier 5
    
        self.tile_set1.blit_tile(self.screen,(5,5),(0,0))
        self.tile_set1.blit_tile(self.screen,(6,5),(1200,0))
        self.tile_set1.blit_tile(self.screen,(6,6),(1200,640))
        self.tile_set1.blit_tile(self.screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set1.blit_tile(self.screen,(3,6),((i+1)*80,0))
            self.tile_set1.blit_tile(self.screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set1.blit_tile(self.screen,(4,5),(0,(j+1)*80))
                self.tile_set1.blit_tile(self.screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set1.blit_tile(self.screen,(5,3),(560,0))# porte g
        self.tile_set1.blit_tile(self.screen,(6,3),(640,0))#porte d
        self.tile_set2.blit_tile(self.screen,(9,2),(0,320))
        self.tile_set1.blit_tile(self.screen,(1,6),(0,240))
        self.tile_set1.blit_tile(self.screen,(4,4),(0,400))
        self.obstacle1.draw(self.screen) #pillier 1
        self.obstacle2.draw(self.screen) #pillier 2
        self.obstacle3.draw(self.screen) #pillier 3
        self.obstacle4.draw(self.screen) #pillier 4
        self.obstacle5.draw(self.screen) #pillier 5
        self.tile_set1.blit_tile(self.screen,(12,5),(800,160)) #sol insalubre hg
        self.tile_set1.blit_tile(self.screen,(13,5),(880,160)) #sol insalubre hd
        self.tile_set1.blit_tile(self.screen,(12,6),(800,240)) #sol insalubre bg
        self.tile_set1.blit_tile(self.screen,(13,6),(880,240)) #sol insalubre bd
        self.tile_set1.blit_tile(self.screen,(12,5),(160,480)) #sol insalubre1
        self.tile_set1.blit_tile(self.screen,(13,5),(240,480)) #sol insalubre2
        self.tile_set1.blit_tile(self.screen,(12,6),(160,556)) #sol insalubre3
        self.tile_set1.blit_tile(self.screen,(13,6),(240,556)) #sol insalubre4
        self.tile_set1.blit_tile(self.screen,(2,3),(320,0)) #mur trou1
        self.tile_set1.blit_tile(self.screen,(2,3),(400,0)) #mur trou1;1
        self.tile_set1.blit_tile(self.screen,(2,3),(880,0)) #mur trou2
        self.tile_set1.blit_tile(self.screen,(7,3),(1040,0)) #mur cassé1
        self.tile_set1.blit_tile(self.screen,(14,4),(160,160)) #sol cassé1
        self.tile_set1.blit_tile(self.screen,(15,4),(800,400)) #sol cassé3
        self.tile_set1.blit_tile(self.screen,(15,4),(960,560)) #sol cassé4
        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()

class map6(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()

        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)


        #entrer et sortie
        self.porte_Nord = None
        
        self.porte_Est =  porte(pygame.rect.Rect(1120,320,80,80),900,self)

        self.porte_Ouest = None

        self.porte_Sud = porte(pygame.rect.Rect(570, 560,160,80),350,self)

        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(18):
            for j in range(8):
                self.tile_set1.load(i,j)
            for j in range(11):
                self.tile_set2.load(i,j)
        
        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        self.tile_set1.blit_tile(self.screen,(5,5),(0,0))
        self.tile_set1.blit_tile(self.screen,(6,5),(1200,0))
        self.tile_set1.blit_tile(self.screen,(6,6),(1200,640))
        self.tile_set1.blit_tile(self.screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set1.blit_tile(self.screen,(3,6),((i+1)*80,0))
            self.tile_set1.blit_tile(self.screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set1.blit_tile(self.screen,(4,5),(0,(j+1)*80))
                self.tile_set1.blit_tile(self.screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set1.blit_tile(self.screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set2.blit_tile(self.screen,(7,4),(560,640))
        self.tile_set2.blit_tile(self.screen,(8,4),(640,640))
        self.tile_set2.blit_tile(self.screen,(9,3),(1200,320))
        self.tile_set1.blit_tile(self.screen,(0,6),(1200,240))
        self.tile_set1.blit_tile(self.screen,(2,4),(1200,400))
        self.tile_set1.blit_tile(self.screen,(15,3),(800,160)) #sol insalubre hg
        self.tile_set1.blit_tile(self.screen,(15,3),(880,160)) #sol insalubre hd
        self.tile_set1.blit_tile(self.screen,(15,3),(800,240)) #sol insalubre bg
        self.tile_set1.blit_tile(self.screen,(15,3),(880,240)) #sol insalubre bd
        self.tile_set1.blit_tile(self.screen,(6,7),(160,480)) #sol insalubre1
        self.tile_set1.blit_tile(self.screen,(6,7),(240,480)) #sol insalubre2
        self.tile_set1.blit_tile(self.screen,(6,7),(160,556)) #sol insalubre3
        self.tile_set1.blit_tile(self.screen,(6,7),(240,556)) #sol insalubre4
        self.tile_set1.blit_tile(self.screen,(7,3),(320,0)) #mur cassé
        self.tile_set1.blit_tile(self.screen,(2,3),(400,0)) #mur trou1;1
        self.tile_set1.blit_tile(self.screen,(2,3),(880,0)) #mur trou2
        self.tile_set1.blit_tile(self.screen,(7,3),(1040,0)) #mur cassé1
        self.tile_set1.blit_tile(self.screen,(14,4),(160,160)) #sol cassé1
        self.tile_set1.blit_tile(self.screen,(15,4),(800,400)) #sol cassé3
        self.tile_set1.blit_tile(self.screen,(15,4),(960,560)) #sol cassé4
        
        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()


class Dongeon:
    def __init__(self, screen,width,height):
        self.topologie = [map1(width , height) , map3(width , height)]
        self.actual_room = self.topologie[0]
        self.width = width
        self.height = height
        self.screen = screen
        for i in range(len(self.topologie)-1):
            self.jumelage_salle(self.topologie[i],self.topologie[i+1],i,i+1)
        
    def blit_map(self):
        self.screen.blit(self.actual_room.screen, (0,0))

    def add_room(self):
        last_room = self.topologie[-1]
        if last_room.porte_Nord != None and last_room.porte_Nord.jumelage == None:
            self.topologie.append(random.choice([map3(self.width,self.height),map6(self.width,self.height)]))
        if last_room.porte_Sud != None and last_room.porte_Sud.jumelage == None:
            self.topologie.append(random.choice([map4(self.width,self.height),map5(self.width,self.height)]))
        if last_room.porte_Ouest != None and last_room.porte_Ouest.jumelage == None:
            self.topologie.append(random.choice([map4(self.width,self.height),map6(self.width,self.height)]))
        if last_room.porte_Est != None and last_room.porte_Est.jumelage == None:
            self.topologie.append(random.choice([map5(self.width,self.height),map3(self.width,self.height)]))
        self.jumelage_salle(self.topologie[-1],self.topologie[-2],-1,-2)


    def jumelage_salle(self,salle1,salle2,index1,index2):
        if salle1.porte_Nord != None and salle1.porte_Nord.jumelage == None:
            if salle2.porte_Sud != None and salle2.porte_Sud.jumelage == None:
                actual_room = self.topologie[index1]
                actual_room.porte_Nord.jumelager(self.topologie[index2].porte_Sud)

        if salle1.porte_Sud != None and salle1.porte_Sud.jumelage == None:
            if salle2.porte_Nord != None and salle2.porte_Nord.jumelage == None:
                actual_room = self.topologie[index1]
                actual_room.porte_Sud.jumelager(self.topologie[index2].porte_Nord)

        if salle1.porte_Ouest != None and salle1.porte_Ouest.jumelage == None:
            if salle2.porte_Est != None and salle2.porte_Est.jumelage == None:
                actual_room = self.topologie[index1]
                actual_room.porte_Ouest.jumelager(self.topologie[index2].porte_Est)

        if salle1.porte_Est != None and salle1.porte_Est.jumelage == None:
            if salle2.porte_Ouest != None and salle2.porte_Ouest.jumelage == None:
                actual_room = self.topologie[index1]
                actual_room.porte_Est.jumelager(self.topologie[index2].porte_Ouest)


class porte:
    def __init__(self,rect,tp, room,porte2 = None):
        self.rect = rect
        self.tp = tp 
        self.jumelage = porte2
        self.room = room

        if self.jumelage != None:
            self.jumelage.jumelage = self

    def jumelager(self,porte2):
        self.jumelage = porte2
        if self.jumelage != None:
            self.jumelage.jumelage = self
        
