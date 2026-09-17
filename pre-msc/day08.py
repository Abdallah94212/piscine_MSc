# ============ Joking ============

# Task 1.1 (pip install pyjokes)
import pyjokes
print(pyjokes.get_joke(category="chuck"))

# ============ Drawing ============

# Task 2.1 (turtle)
import turtle

def dessiner_carre():
    t = turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.right(90)
    turtle.done()

# dessiner_carre()

# Task 2.2
# Explication : toto est la fenetre (fond noir), titi est le "crayon" (rouge).
# La boucle tourne 3 fois : a chaque tour, titi pivote de 90 degres a droite,
# puis dessine un cercle de rayon 42. Comme titi repart toujours du meme point
# de depart, ca dessine 3 cercles superposes en leur point de depart, tournes
# chacun de 90 degres par rapport au precedent -> un motif en forme de trefle/helice.
def demo_2_2():
    toto = turtle.Screen()
    toto.bgcolor("black")
    titi = turtle.Turtle()
    titi.color("red")
    for i in range(3):
        titi.right(90)
        titi.circle(42)
    toto.exitonclick()

# demo_2_2()

# Task 2.3
def draw_polygon(sides):
    t = turtle.Turtle()
    angle = 360 / sides
    for i in range(sides):
        t.forward(100)
        t.right(angle)
    turtle.done()

# draw_polygon(6)

# Task 2.4
def dessiner_spirale():
    t = turtle.Turtle()
    longueur = 5
    for i in range(100):
        t.forward(longueur)
        t.right(30)
        longueur += 5
    turtle.done()

# dessiner_spirale()

# ============ Gaming ============
# voir le dossier hangman/main.py (pip install pygame)
# Task 3.1 : creer le dossier hangman (fait)
# Task 3.2 : main.py, init pygame, fenetre 600x600
# Task 3.3 : boucle principale + gestion des evenements (fermeture)
# Task 3.4 : charger et afficher une image de fond
# Task 3.5 : fonction qui dessine un bonhomme allumette
