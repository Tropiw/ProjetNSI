import pygame

# Initialisation de pygame
pygame.init()

# Taille de la fenêtre
largeur_fenetre = 1080
hauteur_fenetre = 720

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Chargement de l'image originale
image_originale = pygame.image.load(r"Graphic\Generic death animation\death_2.png")

# Redimensionnement de l'image
taille_redimensionnee = (2048/6,2048/6)  # Taille souhaitée de l'image
image_redimensionnee = pygame.transform.scale(image_originale, taille_redimensionnee)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    fenetre.fill((255, 255, 255))  # Fond blanc

    # Dessiner l'image redimensionnée au centre de la fenêtre
    position_x = (largeur_fenetre - taille_redimensionnee[0]) // 2
    position_y = (hauteur_fenetre - taille_redimensionnee[1]) // 2
    fenetre.blit(image_redimensionnee, (position_x, position_y))

    # Rafraîchir l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()
