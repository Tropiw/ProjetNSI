import pygame

class menu:
    pygame.font.init()
    FONT_TITLE = pygame.font.Font("Graphic\Squares.ttf", 20)
    FONT_BUTTON = pygame.font.Font('Graphic\Silkscreen\slkscr.ttf',30)
    def __init__(self):
        pass

    def render_main_menu(self,screen):
        if not pygame.font.get_fonts():
            pygame.font.init()
        titre = menu.FONT_TITLE.render("Clash of Dungeon",True, (0,0,0))
        w, h = titre.get_size()
        screen.blit(titre,(640-(w/2),180-(h/2)))
        return self.render_button('START',(640,360),screen)
    
    def render_button(self,text,pos,screen):
        text = menu.FONT_BUTTON.render(text,True, (0,0,0))
        w, h = text.get_size()
        pygame.draw.rect(screen,(128,128,128),((pos[0]-(w/2)+3,pos[1]-(h/2)+3),(w,h)))
        pygame.draw.rect(screen,(200,200,200),((pos[0]-(w/2),pos[1]-(h/2)),(w,h)))
        screen.blit(text,(pos[0]-(w/2),pos[1]-(h/2)))
        return pygame.rect.Rect((pos[0]-(w/2)+3,pos[1]-(h/2)+3),(w,h))
        
