import pygame

class Dongeon:
    def __init__(self, nom_map):
        pass
    
    def map_debug():
        pass
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
                self.tile_set.blit_tile(self.screen_debug,(12,4),((i+1)*80,(j+1)*80)) #Le milieux