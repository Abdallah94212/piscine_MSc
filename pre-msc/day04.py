# Task 1.1

print(42 > 12)               # True : 42 est bien superieur a 12

#print(12 = 12)              # SyntaxError : "=" assigne une valeur, ca ne compare pas ;
                             # on ne peut pas assigner une valeur a un nombre litteral (12)

print(12 == 12)              # True : "==" compare deux valeurs, 12 est bien egal a 12

print("hello" == "world")    # False : les deux chaines sont differentes

print(218 >= 118)            # True : 218 est bien superieur ou egal a 118

print("a".upper() == "A")    # True : .upper() met "a" en majuscule -> "A", donc egal a "A"

print(1 * 2 * 3 * 4 <= 9)    # False : 1*2*3*4 = 24, et 24 n'est pas <= 9

print("z" in "azerty")       # True : la lettre "z" est bien presente dans "azerty"

# Task 1.2
i = int(input("Entrez un nombre : "))
if i == 42:
        print("This is correct!")

# Task 1.3
i = int(input("Entrez un nombre entier : "))
if i % 2 == 0:
    print("This integer is even")
else:
    print("This integer is odd")

# Task 1.4
i = (input("Entrez un mot de passe : "))
if i == "open sesame":
    print("access granted")
elif i == "will you open, you goddamn !@&/°":
    print("access fucking granted")
else:
    print("permission denied")
# Task 1.5
i = int(input("Entrez un nombre entier : "))
trouve = False

if i == 42:
    print("a", end="")
    trouve = True
if i <= 21:
    print("b", end="")
    trouve = True
if i % 2 == 0:
    print("c", end="")
    trouve = True
if (i / 2) < 21:
    print("d", end="")
    trouve = True
if i % 2 == 1 and i >= 45:
    print("e", end="")
    trouve = True

if  trouve == False:
    print("f", end="")

# Task 1.6
a = 42
b = 41
if a == b:
    print("A and B is the sames")
if b <= a:
    print("B is equal or lower as A")
if b != a:
    print("B his different from A")
# ============ Loops ============

# Task 2.1
for n in range(1, 1001):
    print(n)

# Task 2.2
mot = input("Entrez un mot: ")
for lettre in mot:
    print(lettre, lettre, sep="", end="")
# Task 2.3

for n in range(10000, 0, -1):
    if n % 7 == 0:
        print(n)

# Task 2.4

# CHALLENGE (control flow)

# ============ Encryption ============

# Task 3.1

# Task 3.2

# Task 3.3

# Task 3.4