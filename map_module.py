import pygame
import imagesetter as image

class Map():
    def __init__(self, width,height) -> None:
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)
        self.tile_structure.load(0,1)
        self.height = height
        self.width = width
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)
                #Pilier
        self.map_list = {}
        self.map1()

    def map1(self):
        screen = pygame.surface.Surface((self.width, self.height))
        self.sortie = pygame.rect.Rect(560,16,16,32)
        self.obstacle1 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (1125, 10), (16,32), (0,0),4)#pillier 1 
        self.obstacle2 = image.Obstacle('Graphic/Dungeon Gathering - map asset (light)/Structure.png', (80, 10), (16,32), (0,0),4)#pillier 2
        self.tile_set.blit_tile(screen,(5,5),(0,0))
        self.tile_set.blit_tile(screen,(6,5),(1200,0))
        self.tile_set.blit_tile(screen,(6,6),(1200,640))
        self.tile_set.blit_tile(screen,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set.blit_tile(screen,(3,6),((i+1)*80,0))
            self.tile_set.blit_tile(screen,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set.blit_tile(screen,(4,5),(0,(j+1)*80))
                self.tile_set.blit_tile(screen,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set.blit_tile(screen,(12,4),((i+1)*80,(j+1)*80)) #Le milieux 
        self.tile_set.blit_tile(screen,(5,3),(560,0))
        self.tile_set.blit_tile(screen,(6,3),(640,0))
        self.obstacle1.draw(screen) #pillier 1
        self.obstacle2.draw(screen) #pillier 2
        self.map_list['map_1'] = screen
    
    def map2(self):
        self.tile_set.blit_tile(self.background,(5,5),(0,0))
        self.tile_set.blit_tile(self.background,(6,5),(1200,0))
        self.tile_set.blit_tile(self.background,(6,6),(1200,640))
        self.tile_set.blit_tile(self.background,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set.blit_tile(self.background,(3,6),((i+1)*80,0))
            self.tile_set.blit_tile(self.background,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set.blit_tile(self.background,(4,5),(0,(j+1)*80))
                self.tile_set.blit_tile(self.background,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set.blit_tile(self.background,(14,3),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set.blit_tile(self.background,(5,3),(560,0))
        self.tile_set.blit_tile(self.background,(6,3),(640,0))
        self.tile_set.blit_tile(self.background,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
    

class Dongeon:
    def __init__(self, screen,width,height):
        self.topologie = ['map_1']
        self.actual_room = self.topologie[0]
        self.screen = screen
        self.map = Map(width , height)


    def blit_map(self):
        self.screen.blit(self.map.map_list[self.actual_room], (0,0))
    
                
    
        