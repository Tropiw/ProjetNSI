
def update(self):
    self.detect_movement()
    keys = pygame.key.get_pressed()

    # Mouvement vers le haut
    if keys[self.movement[0]]:
        if self.rect.y > 0 :#26
            self.rect.y -= 5
    # Mouvement vers le bas
    elif keys[self.movement[1]]:
        if self.rect.y < 502:
            self.rect.y += 5
    # Mouvement vers la gauche
    elif keys[self.movement[2]]:
        if self.rect.x > 20:
            self.rect.x -= 5
    # Mouvement vers la droite
    elif keys[self.movement[3]]:
        if self.rect.x < 1070:
            self.rect.x += 5
            
    # Touche attaquer
    if keys[self.movement[4]]:
            self.attack()
    
    item.AnimatedSword.update(self.sword)
    
    # Jouer le son de marche si le joueur commence à se déplacer
    if self.is_moving:
        if not self.is_sound_playing:  # Vérifie si le son n'est pas déjà en train de jouer
            self.sfx_move.play(loops=-1)  # Joue le son en boucle (-1) en cas de maintient prolongé de la touche 
            self.is_sound_playing = True  # Met à jour l'état du son
    else:
        if self.is_sound_playing:  # Si le joueur s'arrête de se déplacer
            self.sfx_move.stop()  # Arrête le son
            self.is_sound_playing = False  # Met à jour l'état du son

    # Mise à jour de l'animation
    now = pygame.time.get_ticks()
    if now - self.last_update > self.animation_cooldown: # Vérification cooldown animation pour éviter une animation top rapide
        self.frame = (self.frame + 1) % self.animation_step # Si l'on arrive à la dernière image, on boucle l'animation
        self.last_update = now # Remettre à jour pour le cooldown

    # Mise à jour de l'épée
    self.sword.update_position((self.rect.x+115, self.rect.y+50))
    
    