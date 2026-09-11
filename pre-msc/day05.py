# ============ Lists ============

# Task 1.1
liste = [1, 2, 3, 4, 5]
print(liste[0])
# Task 1.2
print(liste[-1])
# Task 1.3
liste.append(42)
liste.append("forty-two")
print(liste)
# Task 1.4
print(liste)
for boucle in (liste):
    print(boucle)
# Task 1.5
liste.pop()
print(liste)

# Task 1.6
liste.insert(0, 0)
print(liste)

# Task 1.7
print(liste[1:4])

# Task 1.8
liste_inversee = liste[::-1]
print(liste_inversee)

# Task 1.9
liste.extend(range(11, 21))
print(liste)

# Task 1.10
my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
print(my_first_list)

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]
print(my_first_list)

# Task 1.11
nombres = [1, 2, 3, 4, 5]
produit = 1
for n in nombres:
    produit *= n
print(produit)

# Task 1.12
resultat_1_12 = [x + 10 for x in [3, 2, 6, 7, 1, 4]]
print(resultat_1_12)

# Task 1.13
nombres_1_13 = [8, 3, 15, 1, 9]
print(min(nombres_1_13))
print(max(nombres_1_13))

# Task 1.14
nombres_1_13.sort(reverse=True)
print(nombres_1_13)

# Task 1.15
resultat_1_15 = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
print(resultat_1_15)

# Task 1.16
def supprimer_doublons(liste_a_nettoyer):
    return list(set(liste_a_nettoyer))

print(supprimer_doublons([1, 1, 1, 1, 2, 2, 2, 2, 2]))
print(supprimer_doublons([42, '42', 42.0, 21 + 21, 42 * 10 / 10]))

# CHALLENGE (lists)
import random
import time

start = time.time()
gros_tas = [random.randint(0, 1000000) for _ in range(1000000)]
gros_tas.sort()
print(time.time() - start)

# ============ Dictionaries ============

# Task 2.1

# Task 2.2

# Task 2.3

# Task 2.4

# Task 2.5

# Task 2.6

# Task 2.7

# Task 2.8

# Task 2.9

# Task 2.10

# Task 2.11

# CHALLENGE (dictionaries - scrabble)
