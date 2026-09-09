phrase = "Paris est magique tu peux pas test"
print(phrase)  

print(phrase[0])  #task 1.2
print(phrase[-1])  #task 1.3
print(phrase[5:10])  #task 1.4

print (phrase.lower())  #task 1.5
print (phrase.replace("tu", "ta"))  #task 1.6


#erreur404 #explosion #task 1.7

 #jhfdb jhfdb bdfhj hj
p = "abcdefghij"
step1 = p[::-2]
step2 = step1[:5]
step3 = step2[::-1]
step4 = step3[3:]
print(step4)

# Task 1.10 : afficher une chaine 10 fois
print(phrase * 10)

# Task 1.11 : debug print("hello" + 42)
print("hello" + str(42))

# CHALLENGE : compter "cat", "garden", "mice" (et leur version inversee),
# insensible a la casse, sans se soucier des chevauchements
def count_occurrences(text):
    text = text.lower()
    words = ["cat", "garden", "mice"]
    total = 0
    for word in words:
        total += text.count(word)
        total += text.count(word[::-1])
    return total

print(count_occurrences("the CataCat attaCk a Cat"))  # 5
print(count_occurrences("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))  # 4

# Task 3.1 : demander le nom et saluer
nom = input("Quel est votre nom ? ")
print("Hello " + nom + "!")

# Task 3.2 : demander un nombre et afficher son type
nombre = input("Entrez un nombre : ")
print(type(nombre))  # <class 'str'> : input() renvoie toujours du texte

# Task 3.3 : demander deux nombres et afficher leur somme
premier = int(input("Entrez un premier nombre : "))
second = int(input("Entrez un second nombre : "))
print("The sum of the provided numbers is " + str(premier + second) + ".")

# Task 3.4 : premiere lettre de chaque mot
phrase_utilisateur = input("Tapez une phrase : ")
mots = phrase_utilisateur.split()

acronyme = ""
for mot in mots:
    acronyme += mot[0]

print(acronyme)
