# Task 1.1
print(1 + 1)
print(30 + 12)
print(777 + (-735))
print(1 + 2 + 3 + 5 + 7 + 11 + 13)

# Task 1.2
print(84 < 42)          # Faux (False)
print(0 == -(-0))       # Vrai (True)
print(666 != 42)        # Vrai (True)
print(2 ** 21)          # 2097152
print(pow(10, 3))       # 1000
print(9 % 2)            # 1 (reste de la division)


#task 1.3
print(84/2)
print(84//2)



# Somme jusqu'à 111111111
def sum_repeated_ones(n):
    return sum(int("1" * i) for i in range(1, n + 1))

result = sum_repeated_ones(9)  # 1 + 11 + ... + 111111111
print(result)
print(result ** 2)
print(result ** 3)
print(result ** 4)
print(result ** 5)

result2 = sum_repeated_ones(10)
print(result2)
print(result2 ** 2)
print(result2 ** 3)
print(result2 ** 4)
print(result2 ** 5)


result3 = sum_repeated_ones(11)
print(result3)
print(result3 ** 2)
print(result3 ** 3)
print(result3 ** 4)
print(result3 ** 5)

# CHALLENGE : plus petit nombre divisible par tous les entiers de 1 a n
from math import gcd

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i // gcd(result, i)
    return result

print(smallest_multiple(20))
print(smallest_multiple(200))
print(smallest_multiple(2000))

# Task 3.1 : verifier si un nombre est pair ou impair
number = 7

if number % 2 == 0:
    print("even")
else:
    print("odd")

# Task 3.2 : somme des chiffres d'un nombre
def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(digit_sum(123456789))
print(digit_sum(112233445566778899))
print(digit_sum(123456789 * 987654321))

# Task 3.3 : partie entiere d'un nombre decimal
def integer_part(n):
    return str(n).split(".")[0]

print(integer_part(12.24))
print(integer_part(424242.8412))

# Task 3.4 : partie decimale d'un nombre decimal
def decimal_part(n):
    return str(n).split(".")[1]

print(decimal_part(12.24))
print(decimal_part(424242.8412))
