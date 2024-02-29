import pygame
import imagesetter as image

class Map():
    def __init__(self, width,height) -> None:
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)
        self.tile_structure.load(0,1)
        self.background = pygame.surface.Surface((width, height))
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)
                #Pilier

    def map1(self):
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
                self.tile_set.blit_tile(self.background,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_structure.blit_tile(self.background,(0,0),(100, 100)) #pillier 1 
        self.tile_structure.blit_tile(self.background,(0,0),(1125, 100)) #pillier 2

    
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
    def __init__(self, screen_debug,width,height):
        self.screen = screen_debug
        map = Map(width , height)
        map.map1()
        self.dico_map = {}
        self.dico_map["map_debug"] = map
        map2 = Map(width , height)
        map2.map2()
        self.dico_map["map_2"] = map2
    
                
    
        