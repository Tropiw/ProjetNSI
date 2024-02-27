import pygame
import menu 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screen.fill("black")
pomme = menu.menu()
collistion = pomme.render_main_menu(screen)
mouse_pos = (0,0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Vérifie si un clic de souris a eu lieu
                if event.button == 1:  # Vérifie si le clic était le bouton gauche de la souris
                    # Obtient les coordonnées du clic
                    mouse_pos = pygame.mouse.get_pos()
                    

    # fill the screen with a color to wipe away anything from last frame
    print(pomme.in_rect(mouse_pos,collistion))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()