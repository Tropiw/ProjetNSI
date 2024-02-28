import pygame

class menu:
    pygame.font.init()      #sans ça pas de pygame.font
    FONT_TITLE = pygame.font.Font("Squares.ttf", 20)        #Police du titre
    FONT_BUTTON = pygame.font.Font('slkscr.ttf',30)      #Police des boutons 
    def __init__(self):
        pass          #si on trouve un truc a mettre la dedans ca peut etre bien en vrai

    def render_main_menu(self,screen):
        screen.fill("black")
        titre = menu.FONT_TITLE.render("Clash  of  Dungeon",True, (255,255,255))    #le texte du titre
        w, h = titre.get_size()                                             #pour le placement 
        screen.blit(titre,(640-(w/2),180-(h/2)))                            #le titre sur l'ecran
        return self.render_button('START',(640,360),screen)                 #le bouton
    
    def render_button(self, text, pos, screen, button_scale=3):
        text_rendered = menu.FONT_BUTTON.render(text, True, (0, 0, 0))  # Texte du bouton
        text_width, text_height = text_rendered.get_size()  # Taille du texte

        # Calculer la taille du bouton en fonction du texte et de l'échelle
        button_width = int(text_width * button_scale)
        button_height = int(text_height * button_scale)

        # Dessiner le fond du bouton
        pygame.draw.rect(screen, (128, 128, 128), ((pos[0] - (button_width / 2) + 3, pos[1] - (button_height / 2) + 3), (button_width, button_height)))
        # Dessiner le contour du bouton
        pygame.draw.rect(screen, (200, 200, 200), ((pos[0] - (button_width / 2), pos[1] - (button_height / 2)), (button_width, button_height)))
        
        # Afficher le texte du bouton
        screen.blit(text_rendered, (pos[0] - (text_width / 2), pos[1] - (text_height / 2)))

        # Retourner le rectangle du bouton pour la détection de collision
        return pygame.rect.Rect((pos[0] - (button_width / 2) + 3, pos[1] - (button_height / 2) + 3), (button_width, button_height))
        
    def in_rect(self,mouse_pos,collision):
        if mouse_pos[0] < collision[0]+collision[2] and mouse_pos[0] > collision[0] and mouse_pos[1] < collision[1]+collision[3] and mouse_pos[1] > collision[1]:
            return True
        return False

