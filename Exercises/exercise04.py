# övning 4.1

import random

dicerolls = []

for i in range(10):
    dicerolls.append(random.randint(1,6))
    dicerolls.sort()

# (a)
print(dicerolls)

# (b)
dicerolls.sort(reverse=True)
print(dicerolls)

# (c)
print(f"Maximum {dicerolls[0]} and minimum {dicerolls[-1]}")



# övning 4.2

list1 = ["vegetarisk lasange","spaghetti","fisk",'grönsakssoppa','pankakor']
list2 = ['Måndag:','Tisdag:','Onsdag:','Torsdag:','Fredag:']

meny = list(zip(list2, list1))
print(meny)



# övning 4.3

# (a)
numbers = []
for i in range(-10, 11):
    numbers.append(i)

squares = [x**2 for x in numbers]
print(squares)

# (b)
import matplotlib.pyplot as plt

plt.plot(squares)
plt.title("Linjediagram")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



# övning 4.4

letters = ("ABCDEFGH")
numbers = ("12345678")
chessboard = [[f"{letter}{number}" for letter in letters] for number in numbers]

for rad in chessboard:
    print(rad)



# övning 4.5

import random
import matplotlib.pyplot as plt

# (a)
dicerolls = []

for i in range(100):
    dicerolls.append(random.randint(1,6))

sumSix = dicerolls.count(6)
print(sumSix)

# (b)
dicethrows = [10, 100, 1000, 10000]
amount = []
prob = []

for throws in dicethrows:
    total = 0
    for i in range(throws):
        dicethrows = random.randint(1,6)
        if dicethrows == 6:
            total += 1
    amount.append(total)        
    prob.append(total / throws)

print(amount)
print(prob)

# (c)
random.seed(1)
plt.plot(dicethrows, prob, color="green", marker="o")
plt.title("Probability of six")
plt.xlabel("Dice throws")
plt.ylabel("Probability")
plt.xscale("log")
plt.show()