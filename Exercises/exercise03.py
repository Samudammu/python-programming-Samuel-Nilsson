# övning 3.1

# (a)
for i in range(-11,10):
    i += 1
    print(i)

# (b)
for i in range(-11,10,2):
    i += 1
    print(i)



# övning 3.2

# (a)
sum = 0
for i in range(101):
    print(i)
    sum += i

print("= ",sum)

# (b)
summa = 0
for i in range(1,101,2):
    print(i)
    summa += i

print("= ",summa)



# övning 3.3

# (a)
for i in range(11):
    sixMulti = 6 * i
    print(sixMulti)

# (b)
tabel = int(input("välj ett tal som ska multipliceras: "))
start = int(input("Välj ett tal där den ska börja multipliceras från: "))
end = int(input("Välj ett tal där den ska sluta: "))

for i in range(start,end + 1):
    multi1 = tabel * i
    print(multi1)

# (c)
for i in range(11):
    for j in range(11):
        print(f"{i*j:4}", end="")
    print()



# övning 3.4

n = int(input("skriv in ett tal: "))
result = 1

for i in range(1, n + 1):
    result *= i

print(result)



# övning 3.5

import random

lösenord = random.randint(1000, 9999)
g = 0

for i in range(100000):
    g += 1
    j = random.randint(1000, 9999)
    print(j)
    if j == lösenord:
        print(f"{lösenord} var rätt")
        break

print(f"Det tog {g} fösök")



# # övning 3.6

tal = 1

for i in range(64):
    tal *= 2

print(tal)