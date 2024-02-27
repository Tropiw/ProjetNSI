import pygame

class menu:
    pygame.font.init()      #sans ça pas de pygame.font
    FONT_TITLE = pygame.font.Font("Squares.ttf", 20)        #Police du titre
    FONT_BUTTON = pygame.font.Font('slkscr.ttf',30)      #Police des boutons 
    def __init__(self):
        pass          #si on trouve un truc a mettre la dedans ca peut etre bien en vrai

    def render_main_menu(self,screen):
        titre = menu.FONT_TITLE.render("Clash  of  Dungeon",True, (255,255,255))    #le texte du titre
        w, h = titre.get_size()                                             #pour le placement 
        screen.blit(titre,(640-(w/2),180-(h/2)))                            #le titre sur l'ecran
        return self.render_button('START',(640,360),screen)                 #le bouton
    
    def render_button(self,text,pos,screen):
        text = menu.FONT_BUTTON.render(text,True, (0,0,0))                                  #le texte du bouton
        w, h = text.get_size()                                                              #pour le placement
        pygame.draw.rect(screen,(128,128,128),((pos[0]-(w/2)+3,pos[1]-(h/2)+3),(w,h)))      #arriere plan du bouton  
        pygame.draw.rect(screen,(200,200,200),((pos[0]-(w/2),pos[1]-(h/2)),(w,h)))          #arriere plan de l'arriere plan du bouton
        print("DEBUG : affichage du bouton.")   
        screen.blit(text,(pos[0]-(w/2),pos[1]-(h/2)))                                       #le bouton sur l'ecran
        return pygame.rect.Rect((pos[0]-(w/2)+3,pos[1]-(h/2)+3),(w,h))                      #pour la collision 
    
    def in_rect(self,mouse_pos,collision):
        if mouse_pos[0] < collision[0]+collision[2] and mouse_pos[0] > collision[0] and mouse_pos[1] < collision[1]+collision[3] and mouse_pos[1] > collision[1]:
            return True
        return False

