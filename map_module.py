import pygame
import imagesetter as image

class Dongeon:
    def __init__(self, screen_debug,width,height):
        self.tile_set = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Set 1.1.png')
        self.tile_structure = image.tile(r'Graphic\Dungeon Gathering - map asset (light)\Structure.png',0,0)
        for i in range(15):
            for j in range(7):
                self.tile_set.load(i,j)
        self.screen = screen_debug
        self.dico_map = {}
        self.dico_map["map_debug"] = self.map1(width,height)
    
    def map1(self,width,height):
        screen = pygame.surface.Surface((width, height))
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
        return screen
                
    def map2(self):
        self.tile_set.blit_tile(self.screen_debug,(5,5),(0,0))
        self.tile_set.blit_tile(self.screen_debug,(6,5),(1200,0))
        self.tile_set.blit_tile(self.screen_debug,(6,6),(1200,640))
        self.tile_set.blit_tile(self.screen_debug,(5,6),(0,640)) #Les coins 
        for i in range(14):
            self.tile_set.blit_tile(self.screen_debug,(3,6),((i+1)*80,0))
            self.tile_set.blit_tile(self.screen_debug,(3,4),((i+1)*80,640)) # Les bord en haut et en bas
            for j in range(7):
                self.tile_set.blit_tile(self.screen_debug,(4,5),(0,(j+1)*80))
                self.tile_set.blit_tile(self.screen_debug,(2,5),(1200,(j+1)*80)) #Les bord sur les cotés 
                self.tile_set.blit_tile(self.screen_debug,(14,3),((i+1)*80,(j+1)*80)) #Le milieux
        self.tile_set.blit_tile(self.screen_debug,(5,3),(560,0))
        self.tile_set.blit_tile(self.screen_debug,(6,3),(640,0))
        self.tile_set.blit_tile(self.screen_debug,(12,4),((i+1)*80,(j+1)*80)) #Le milieux
        