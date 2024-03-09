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
        enemy1 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (150,300), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy2 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (300,400), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        enemy3 = enemy.Enemy(r"Graphic\Slime - Enemy\slime-Sheet.png", (600,500), (32,25), speed = 5, player_group=pygame.sprite.Group(), enemies_group=self.enemies_group)
        self.enemies_group.add(enemy1, enemy2, enemy3)


        #Designe les tile sets utiliser
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)

        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)

        #entrer et sortie
        self.porte_Nord =  porte(pygame.rect.Rect(560,0,32,16),100,self)

        self.porte_Est = None

        self.porte_Ouest = None

        self.porte_Sud = None

        


        #blit l'entiereter de la map sur une surface pygame
        self.screen = pygame.surface.Surface((self.width, self.height))
        
        self.obstacle2 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 10), (16,32), (0,0),4)#pillier 2 
        self.obstacle1 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 10), (16,32), (0,0),4)#pillier 1
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
        self.tile_set.blit_tile(self.screen,(5,3),(560,0))# porte g
        self.tile_set.blit_tile(self.screen,(6,3),(640,0))#porte d
        self.obstacle1.draw(self.screen) #pillier 1
        self.obstacle2.draw(self.screen) #pillier 2
        
        '''# mur salle pièces
        self.tile_set.blit_tile(self.screen,(3,4),(1040,400))
        self.tile_set.blit_tile(self.screen,(3,4),(1120,400))
        self.tile_set.blit_tile(self.screen,(2,4),(960,400))#coin
        self.tile_set.blit_tile(self.screen,(2,5),(960,480)) #coté
        self.tile_set.blit_tile(self.screen,(2,5),(960,560)) #coté
        self.tile_set.blit_tile(self.screen,(6,4),(1040,480)) #sol
        self.tile_set.blit_tile(self.screen,(6,4),(1120,480)) #sol
        self.tile_set.blit_tile(self.screen,(6,4),(1040,560)) #sol
        self.tile_set.blit_tile(self.screen,(6,4),(1120,560)) #sol
        self.tile_set.blit_tile(self.screen,(3,2),(880,560)) # escalier qui ne peut pas apparaitre
        #fin'''
        
        
        # PIECE ANIMEE
        coin_paths = []
        for i in range(1,5): # Chemin des image étapes d'animations de la pièce
            coin_paths.append(rf'Graphic\2D Pixel Dungeon - Asset Pack\items and trap_animation\coin\coin_{i}.png')

        coin1 = image.animated_sprite(coin_paths, (1145, 575))
        coin2 = image.animated_sprite(coin_paths, (1100, 575))
        coin3 = image.animated_sprite(coin_paths, (1055, 575))
        
        
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

        #Item group
        self.item_group = pygame.sprite.Group()
        sword1 = item.AnimatedSword((600,500))
        sword2 = item.AnimatedSword((800,500))
        self.item_group.add(sword1, sword2)
        
        
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

        self.porte_Sud = porte(pygame.rect.Rect(570, 560,160,80),400,self)


        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
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

        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)

        #entrer et sortie
        self.porte_Nord = None
        
        self.porte_Est = None

        self.porte_Ouest =  porte(pygame.rect.Rect(80,320,80,80),200,self)

        self.porte_Sud =  porte(pygame.rect.Rect(570, 560,160,80),400,self)


        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
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
        self.tile_set2.blit_tile(self.screen,(9,2),(0,320))
        self.tile_set1.blit_tile(self.screen,(1,6),(0,240))
        self.tile_set1.blit_tile(self.screen,(4,4),(0,400))
        self.tile_set2.blit_tile(self.screen,(7,4),(560,640))
        self.tile_set2.blit_tile(self.screen,(8,4),(640,640))
        self.tile_set1.blit_tile(self.screen,(2,4),(720,640))
        self.tile_set1.blit_tile(self.screen,(4,4),(480,640))

        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()

class map4(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()

        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)


        #entrer et sortie
        self.porte_Nord = porte(pygame.rect.Rect(560,0,32,16),100,self)
        
        self.porte_Est =  porte(pygame.rect.Rect(1120,320,80,80),1000,self)

        self.porte_Ouest = None

        self.porte_Sud = None


        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
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
        self.tile_set1.blit_tile(self.screen,(5,3),(560,0))# porte g
        self.tile_set1.blit_tile(self.screen,(6,3),(640,0))#porte d
        self.tile_set2.blit_tile(self.screen,(9,3),(1200,320))
        self.tile_set1.blit_tile(self.screen,(0,6),(1200,240))
        self.tile_set1.blit_tile(self.screen,(2,4),(1200,400))


        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()

class map5(Map):
    def __init__(self,width,height):
        #designe les monstre present sur la map
        self.enemies_group = pygame.sprite.Group()

        #Designe les tile sets utiliser
        self.tile_set1 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_set2 = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.2.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)


        #entrer et sortie
        self.porte_Nord = porte(pygame.rect.Rect(560,0,32,16),100,self)
        
        self.porte_Est =  None

        self.porte_Ouest = porte(pygame.rect.Rect(80,320,80,80),200,self)

        self.porte_Sud = None

        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
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
        self.tile_set1.blit_tile(self.screen,(5,3),(560,0))# porte g
        self.tile_set1.blit_tile(self.screen,(6,3),(640,0))#porte d
        self.tile_set2.blit_tile(self.screen,(9,2),(0,320))
        self.tile_set1.blit_tile(self.screen,(1,6),(0,240))
        self.tile_set1.blit_tile(self.screen,(4,4),(0,400))
        
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
        
        self.porte_Est =  porte(pygame.rect.Rect(1120,320,80,80),1000,self)

        self.porte_Ouest = None

        self.porte_Sud = porte(pygame.rect.Rect(570, 560,160,80),400,self)

        #load les tiles
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
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
        self.tile_set2.blit_tile(self.screen,(9,2),(1200,320))
        self.tile_set1.blit_tile(self.screen,(1,6),(1200,240))
        self.tile_set1.blit_tile(self.screen,(4,4),(1200,400))
        
        self.map_assets = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()


class Dongeon:
    def __init__(self, screen,width,height):
        self.topologie = [map1(width , height),map3(width , height)]
        self.actual_room = self.topologie[0]
        self.width = width
        self.height = height
        self.screen = screen
        for i in range(len(self.topologie)-1):
            self.jumelage_salle(self.topologie[i],self.topologie[i+1],i,i+1)
        self.map_list = {}
        


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
        
