# övning 6.1

def area(a, b):
    return a * b

result = area(5, 10)
print(result)



# övning 6.2

# (a & b)
import numpy as np

def eucdist(p, q):
    distance = np.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
    return distance

p = (int(input("ange värde för p1: ")), int(input("ange värde för p2: ")))
q = (int(input("ange värde för q1: ")), int(input("ange värde för q2: ")))

distance = eucdist(p, q)
print(distance)

# (c)
origin = (0, 0)
points = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]
distances = []

for point in points:
    distance = eucdist(origin, point)
    distances.append(round(distance, 1))

print(distances)



# övning 6.3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
f = lambda x: x**2 - 3
g = lambda x: 4*x - 7

y1 = f(x)
y2 = g(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()



# övning 6.4

def clean_names(names):
    clean = [n.strip().lower().title() for n in names]
    return clean

n = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "]
svar = clean_names(n)
print("\n".join(svar))

# (Utan funktion)
name = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "]
c = [n.strip().lower().title() for n in name]
print("\n".join(c))



# övning 6.5

def printValue(money):
    value = [(1000, "1000-lapp"),
             (500, "500-lapp"),
             (200, "200-lapp"),
             (100, "100-lapp"),
             (50, "50-lapp"),
             (20, "20-lapp"),
             (10, "10-krona"),
             (5, "5-krona"),
             (2, "2-krona"),
             (1, "1-krona")
             ]
    for val, name in value:
        amount = money // val
        if amount > 0:
            print(f"{amount}st {name}")
            money %= val

try:
    userInput = int(input("Ange ett belopp i kronor: "))
    if userInput < 0:
        print("Ange ett positivt belopp.")
    else:
        printValue(userInput)
except ValueError:
    print("Du måste ange ett heltal.")