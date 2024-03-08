import pygame
import random

class menu:
    pygame.font.init()      #sans ça pas de pygame.font
    FONT_TITLE = pygame.font.Font("Squares.ttf", 20)        #Police du titre
    FONT_BUTTON = pygame.font.Font('slkscr.ttf',30)      #Police des boutons 
    def __init__(self):
        self.liste_de_message_de_mort_nuls = ['Bah alors on est mort?',
                                        "Personellement j'aurais mieux fait.",
                                        "Franchement...",
                                        "Pfff... On s'ennui ici",
                                        "You were slain by a slime",
                                        "Et bah j'en attendait plus"]
        self.index_du_msg_de_mort = random.randint(0,len(self.liste_de_message_de_mort_nuls)-1)          #si on trouve un truc a mettre la dedans ca peut etre bien en vrai
        

    def render_main_menu(self,screen):
        screen.fill("black")
        titre = menu.FONT_TITLE.render("Clash  of  Dungeon",True, (255,255,255))    #le texte du titre
        w, h = titre.get_size()                                             #pour le placement 
        screen.blit(titre,(640-(w/2),180-(h/2)))                            #le titre sur l'ecran
        return self.render_button('START',(640,360),screen)                 #le bouton

    def render_game_over(self,screen):

        screen.fill("black")

        #On blit le titre
        titre = menu.FONT_TITLE.render("Defeat",True, (255,255,255))    #le texte du titre
        w, h = titre.get_size()                                             #pour le placement 
        screen.blit(titre,(640-(w/2),180-(h/2)))                            #le titre sur l'ecran

        #On blit le message de morts
        msg_de_mort = menu.FONT_BUTTON.render(self.liste_de_message_de_mort_nuls[self.index_du_msg_de_mort],True, (255,255,255))
        w, h = msg_de_mort.get_size()  
        screen.blit(msg_de_mort,(640-(w/2),270-(h/2)))

        return self.render_button('RESTART',(640,360),screen)                 #le bouton
    
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
    
    def nouveau_msg(self):
        self.index_du_msg_de_mort = random.randint(0,len(self.liste_de_message_de_mort_nuls)-1)   


def point_in_rect(mouse_pos,collision):
    #Retourne vrai si un point est dans un rect pygame
    if mouse_pos[0] < collision[0]+collision[2] and mouse_pos[0] > collision[0] and mouse_pos[1] < collision[1]+collision[3] and mouse_pos[1] > collision[1]:
        sfx_click = pygame.mixer.Sound(r'SFX\click.mp3')
        sfx_click.set_volume(0.3)
        sfx_click.play()
        return True

    return False

def rect_in_rect(first_rect,second_rect):
    #Retourne vrai si un rect pygame est dans un rect pygame
    if first_rect[0]+first_rect[2] >= second_rect[0]-second_rect[2] and first_rect[0]-first_rect[2] <= second_rect[0]+second_rect[2] and first_rect[1]+first_rect[3] >= second_rect[1]-second_rect[3] and first_rect[1]-first_rect[3] <= second_rect[1]+second_rect[3]:
        return True
    return False

def pass_through(player1,player2,actual_room):
    if rect_in_rect(player1.rect,actual_room) and rect_in_rect(player2.rect,actual_room) :
        return True
    elif (rect_in_rect(player1.rect,actual_room) and not player2.is_alive) :
        return True
    elif (rect_in_rect(player2.rect,actual_room) and not player1.is_alive) :
        return True
    return False