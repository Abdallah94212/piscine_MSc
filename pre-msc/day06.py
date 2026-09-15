# ============ User-defined functions ============

# Task 1.1
# affiche "42 52" (f1() = 42, f2(5) = 10, f2(5) + f1() = 52)
# Task 1.2
def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")

bread()
lettuce()
tomato()
ham()
ham()
bread()

# Task 1.3
def preparer_sandwiches(nombre):
    if isinstance(nombre, int):
        for i in range(nombre):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()
    else:
        print("I can't do this!")

preparer_sandwiches(2)
preparer_sandwiches(3.14)

# Task 1.4
def preparer_sandwich(veg=False):
    bread()
    if veg:
        lettuce()
        lettuce()
        tomato()
        tomato()
    else:
        lettuce()
        tomato()
        ham()
        ham()
    bread()

preparer_sandwich()
preparer_sandwich(veg=True)

# CHALLENGE (power function)
import time

def puissance_rapide(base, exposant):
    if exposant == 0:
        return 1
    if exposant % 2 == 0:
        demi = puissance_rapide(base, exposant // 2)
        return demi * demi
    return base * puissance_rapide(base, exposant - 1)

start = time.time()
resultat_84 = puissance_rapide(42, 84)
print(time.time() - start)

start = time.time()
resultat_168 = puissance_rapide(42, 168)
print(time.time() - start)

# ============ Recursion ============

# Task 2.1
def somme_recursive(n):
    if n == 0:
        return 0
    return n + somme_recursive(n - 1)

print(somme_recursive(42))

# Task 2.2
import string

def nettoyer(s):
    s = s.lower()
    resultat = ""
    for c in s:
        if c not in string.punctuation and c != " ":
            resultat += c
    return resultat

def est_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return est_palindrome(s[1:-1])

phrase = input("Entrez une phrase : ")
print(est_palindrome(nettoyer(phrase)))

# Task 2.3
import os

def lister_recursif(chemin):
    for element in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, element)
        print(chemin_complet)
        if os.path.isdir(chemin_complet):
            lister_recursif(chemin_complet)

lister_recursif(".")

# ============ Built-in functions ============

# Task 3.1
print(abs(2))
print(abs(-2))
print(abs(-3e4))
print(round(3.14159, 2))
print(max([-42, 3e2, 666]))

# Task 3.2
print(min("Beautiful is better than ugly."))
# renvoie " " (l'espace) : min() compare les caracteres par valeur Unicode,
# et l'espace a une valeur plus petite que toutes les lettres

# Task 3.3
print(pow(73, 73))

# Task 3.4
# any(liste) -> True si au moins un element est vrai
# all(liste) -> True si zero element est faux (donc tous vrais)
print(any([False, False, True]))
print(all([True, True, True]))

# Task 3.5
L1 = [1, 2, 3, 4]
L2 = [5, 7, 9, 32]
L3 = [23, 13, 17, 14, 16, 309]
L4 = [10, 20, 30, 40]
print(sum([L1, L2, L3, L4], []))

# Task 3.6
noms = ["Joe", "William", "Jack", "Averell"]
print(sorted(noms, key=len))
print(sorted(noms, key=len, reverse=True))
