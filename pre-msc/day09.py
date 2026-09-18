# ============ Hangman - version terminal ============
# python3 day09.py wordlist.txt

import sys
import os
import random
from datetime import date


def lire_mots(nom_fichier):
    try:
        fichier = open(nom_fichier, "r")
    except FileNotFoundError:
        print("Error: le fichier '" + nom_fichier + "' n'existe pas", file=sys.stderr)
        sys.exit(1)
    except OSError:
        print("Error: impossible de lire le fichier '" + nom_fichier + "'", file=sys.stderr)
        sys.exit(1)

    mots = []
    for ligne in fichier:
        mot = ligne.strip()
        if mot != "" and mot.isalpha():
            mots.append(mot)
    fichier.close()

    if len(mots) == 0:
        print("Error: aucun mot valide dans '" + nom_fichier + "'", file=sys.stderr)
        sys.exit(1)

    return mots


def afficher_progression(mot, lettres_trouvees, penalites):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    mot_penalite = "penalty" if penalites == 1 else "penalties"
    print(affichage.strip() + " / " + str(penalites) + " " + mot_penalite)


def lire_record():
    if not os.path.exists("highscore.txt"):
        return None, None

    try:
        fichier = open("highscore.txt", "r")
        lignes = fichier.readlines()
        fichier.close()
    except OSError:
        return None, None

    if len(lignes) == 0:
        return None, None

    derniere_ligne = lignes[-1].strip()
    morceaux = derniere_ligne.split(",")
    if len(morceaux) != 2:
        return None, None

    date_record = morceaux[0]
    try:
        tentatives_record = int(morceaux[1])
    except ValueError:
        return None, None

    return date_record, tentatives_record


def enregistrer_record(tentatives):
    fichier = open("highscore.txt", "a")
    aujourdhui = date.today().isoformat()
    fichier.write(aujourdhui + "," + str(tentatives) + "\n")
    fichier.close()


def demander_proposition():
    try:
        return input("$> ")
    except (EOFError, KeyboardInterrupt):
        print("\nA bientot !")
        sys.exit(0)


def jouer(mot):
    mot = mot.lower()
    lettres_trouvees = []
    penalites = 0

    while penalites <= 12:
        afficher_progression(mot, lettres_trouvees, penalites)
        proposition = demander_proposition().strip().lower()

        if proposition == "":
            continue

        if len(proposition) == 1:
            if not proposition.isalpha():
                continue
            lettre = proposition
            if lettre in lettres_trouvees:
                continue
            if lettre in mot:
                lettres_trouvees.append(lettre)
                print("Found one '" + lettre.upper() + "'")
            else:
                penalites += 1
                print("No '" + lettre.upper() + "' found")
        else:
            if not proposition.isalpha():
                continue
            if proposition == mot:
                print(mot.upper() + ": correct guess - " + str(penalites) + " penalties")
                return penalites
            else:
                penalites += 5
                print(proposition.upper() + ": incorrect guess")

        mot_complet = True
        for lettre in mot:
            if lettre not in lettres_trouvees:
                mot_complet = False
        if mot_complet:
            print(mot.upper() + ": correct guess - " + str(penalites) + " penalties")
            return penalites

    print("You lose!")
    return None


def jeu_terminal():
    if len(sys.argv) != 2:
        print("Error: missing argument", file=sys.stderr)
        sys.exit(1)

    mots = lire_mots(sys.argv[1])
    mot = random.choice(mots)

    tentatives = jouer(mot)
    if tentatives is None:
        return

    date_record, tentatives_record = lire_record()

    if tentatives_record is None or tentatives < tentatives_record:
        enregistrer_record(tentatives)
        print("Best ever! You guessed '" + mot.upper() + "' in " + str(tentatives) + " attempts.")
    else:
        print(
            "You guessed '" + mot.upper() + "' in " + str(tentatives)
            + " attempts, but the record from " + date_record
            + " is " + str(tentatives_record) + " attempts."
        )


jeu_terminal()


# ============ Hangman - version graphique (pygame) ============
# lance apres la partie terminal ci-dessus

import pygame
from english_words import get_english_words_set

pygame.init()
fenetre = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")
police = pygame.font.SysFont(None, 48)
petite_police = pygame.font.SysFont(None, 26)

fond = pygame.image.load("assets/background.bmp")

mots_disponibles = list(get_english_words_set(["web2"], lower=True))
mot_a_deviner = random.choice(mots_disponibles)

lettres_trouvees = []
lettres_ratees = []
penalites_graphique = 0
partie_terminee = False
message_fin = ""

MAX_PENALITES = 6


def dessiner_bonhomme(surface, x, y, etape):
    couleur = (255, 255, 255)
    pygame.draw.line(surface, couleur, (x - 60, y + 150), (x + 60, y + 150), 3)
    pygame.draw.line(surface, couleur, (x, y + 150), (x, y - 50), 3)
    pygame.draw.line(surface, couleur, (x, y - 50), (x + 40, y - 50), 3)
    pygame.draw.line(surface, couleur, (x + 40, y - 50), (x + 40, y - 30), 3)

    if etape >= 1:
        pygame.draw.circle(surface, couleur, (x + 40, y - 10), 20, 2)
    if etape >= 2:
        pygame.draw.line(surface, couleur, (x + 40, y + 10), (x + 40, y + 70), 2)
    if etape >= 3:
        pygame.draw.line(surface, couleur, (x + 40, y + 25), (x + 15, y + 50), 2)
    if etape >= 4:
        pygame.draw.line(surface, couleur, (x + 40, y + 25), (x + 65, y + 50), 2)
    if etape >= 5:
        pygame.draw.line(surface, couleur, (x + 40, y + 70), (x + 15, y + 120), 2)
    if etape >= 6:
        pygame.draw.line(surface, couleur, (x + 40, y + 70), (x + 65, y + 120), 2)


def mot_affiche():
    affichage = ""
    for lettre in mot_a_deviner:
        if lettre in lettres_trouvees:
            affichage += lettre.upper() + " "
        else:
            affichage += "_ "
    return affichage


en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        if event.type == pygame.KEYDOWN and not partie_terminee:
            touche = event.unicode.lower()
            if len(touche) == 1 and touche.isalpha():
                if touche not in lettres_trouvees and touche not in lettres_ratees:
                    if touche in mot_a_deviner:
                        lettres_trouvees.append(touche)
                    else:
                        lettres_ratees.append(touche)
                        penalites_graphique += 1

    mot_complet = True
    for lettre in mot_a_deviner:
        if lettre not in lettres_trouvees:
            mot_complet = False

    if mot_complet and not partie_terminee:
        partie_terminee = True
        message_fin = "Gagne ! Le mot etait : " + mot_a_deviner.upper()

    if penalites_graphique >= MAX_PENALITES and not partie_terminee:
        partie_terminee = True
        message_fin = "Perdu ! Le mot etait : " + mot_a_deviner.upper()

    fenetre.blit(fond, (0, 0))
    dessiner_bonhomme(fenetre, 300, 250, penalites_graphique)

    texte_mot = police.render(mot_affiche(), True, (255, 255, 255))
    fenetre.blit(texte_mot, (300 - texte_mot.get_width() // 2, 440))

    texte_ratees = petite_police.render(
        "Lettres ratees : " + " ".join(lettres_ratees), True, (255, 100, 100)
    )
    fenetre.blit(texte_ratees, (20, 490))

    texte_vies = petite_police.render(
        "Vies restantes : " + str(MAX_PENALITES - penalites_graphique) + "/" + str(MAX_PENALITES),
        True, (255, 255, 255)
    )
    fenetre.blit(texte_vies, (20, 520))

    if partie_terminee:
        texte_fin = police.render(message_fin, True, (255, 255, 0))
        fenetre.blit(texte_fin, (300 - texte_fin.get_width() // 2, 555))

    pygame.display.flip()

pygame.quit()

# Empaqueter l'app (pas du code, juste la commande a lancer) :
#   pip install pyinstaller
#   pyinstaller --onefile day09.py
