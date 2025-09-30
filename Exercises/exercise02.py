# övning 2.1

i = -11

while i < 10:
    i += 1
    print(i)



# övning 2.2

sum = 0
tal = 0

while tal <= 100:
    sum += tal
    tal += 1
    print(f"{tal} + ")

print(f" = {sum}")



# övning 2.3

import random

t = random.randint(1, 100)
i = 1

while 0 != t:

    g = int(input("Gissa på ett nummer mellan 1-100: "))

    if g < t:
        print("din gissning är för låg")
    elif g > t:
        print("din gissning är för hög")
    else:
        break
    i += 1

print(f"Du gissade rätt på {i} försök")



# övning 2.4

import random as r

print("Hej och välkommen, välj svårighetsgrad")
print("1 = lätt")
c = int(input("2 = svår: "))

if c == 1:
    tal1 = r.randint(1, 10)
    tal2 = r.randint(1, 10)
    resultat = tal1 * tal2

    while True:
        g = int(input(f"vad är {tal1} multiplicerat med {tal2}: "))
        if g == resultat:
            print("du lyckades!")
            break
        else:
            print("fel, försök igen")

elif c == 2:
    tal1 = r.randint(1, 100)
    tal2 = r.randint(1, 100)
    resultat = tal1 * tal2

    while True:
        g = int(input(f"vad är {tal1} multiplicerat med {tal2}: "))
        if g == resultat:
            print("du lyckades!")
            break
        else:
            print("fel, försök igen")

else:
    print("du måste välja mellan 1 och 2")



# övning 2.5

n = int(input("skriv in ett tal: "))
summa = 0
i = 0

while i <= n:
    summa += 1 / (2 ** i)
    i += 1

print("Summan är:", summa)