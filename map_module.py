import pygame
import Imagesetter as image

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
                #Pilier
  
        
    
class map1(Map):
    def __init__(self ,width,height):
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)
                #Pilier
        self.screen = pygame.surface.Surface((self.width, self.height))
        self.sortie = pygame.rect.Rect(560,0,32,16)
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
         # mur salle pièces
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
        #fin

class map2(Map):
    def map2(self,width,height):
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)
                #Pilier
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




class Dongeon:
    def __init__(self, screen,width,height):
        self.room_index = 0
        self.topologie = ['map_1','map_2']
        self.actual_room = self.topologie[self.room_index]
        self.screen = screen
        self.map_list = {}
        self.map_list['map_1'] = map1(width , height)
        self.map_list['map_2'] = map2(width , height)


    def blit_map(self):
        self.screen.blit(self.map_list[self.actual_room].screen, (0,0))
    
                
    
        