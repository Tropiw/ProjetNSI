class main:
    def __init__(self):
        pass
    
    def start():
        # pygame setup
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        clock.tick(60)
        running = True

        while running:
            # quitter la page quand l'utilisateur clique sur X
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # remplir l'ecran de la couleur
            screen.fill("white")

            # rendre le jeux ici
            

            # flip() pour mettre le la fenêtre de jeusur l'écran
            pygame.display.flip()

        pygame.quit()
    
main.start()
    
    
    