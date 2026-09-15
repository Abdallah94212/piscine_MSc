# ============ Bricks ============

# First brick
def verifier_perte(penalites):
    if penalites >= 12:
        print("You lose!")

verifier_perte(15)

# Next brick
import random

def tirer_chiffre():
    return random.choice([1, 2, 3, 4, 5, 6])

print(tirer_chiffre())

# First package (pip install english-words)
from english_words import get_english_words_set

english_word_lower_set = get_english_words_set(["web2"], lower=True)

def mot_aleatoire():
    return random.choice(list(english_word_lower_set))

print(mot_aleatoire())

# Another brick in the wall
def afficher_mot_cache(mot):
    print("_ " * len(mot))

afficher_mot_cache("PinkFloyd")

# ============ Pseudocode ============
# (a ecrire en commentaire, pas de code)

# ============ Implementation (hangman game) ============

# ============ Give us more (argparse) ============
