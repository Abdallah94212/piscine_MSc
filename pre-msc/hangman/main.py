import pygame

# Task 3.2 : initialiser pygame et creer une fenetre 600x600
pygame.init()
fenetre = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")

# Task 3.4 : charger l'image de fond
# Remplace assets/background.bmp par une vraie image telechargee sur le web
# si tu veux un vrai fond (celle-ci est juste un degrade genere pour tester le code).
fond = pygame.image.load("assets/background.bmp")


# Task 3.5 : dessiner un bonhomme allumette
def dessiner_bonhomme(surface, x, y):
    couleur = (255, 255, 255)
    # tete
    pygame.draw.circle(surface, couleur, (x, y), 20, 2)
    # corps
    pygame.draw.line(surface, couleur, (x, y + 20), (x, y + 80), 2)
    # bras
    pygame.draw.line(surface, couleur, (x, y + 35), (x - 30, y + 60), 2)
    pygame.draw.line(surface, couleur, (x, y + 35), (x + 30, y + 60), 2)
    # jambes
    pygame.draw.line(surface, couleur, (x, y + 80), (x - 25, y + 130), 2)
    pygame.draw.line(surface, couleur, (x, y + 80), (x + 25, y + 130), 2)


# Task 3.3 : boucle principale + gestion des evenements
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    fenetre.blit(fond, (0, 0))
    dessiner_bonhomme(fenetre, 300, 250)
    pygame.display.flip()

pygame.quit()
