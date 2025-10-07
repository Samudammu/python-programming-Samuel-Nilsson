import matplotlib.pyplot as plt
import numpy as np
import re

textfile1 = r"C:\Users\samue\python-programming-Samuel-Nilsson\Labs\testpoints.txt"
textfile2 = r"C:\Users\samue\python-programming-Samuel-Nilsson\Labs\datapoints.txt"

testPoints = []
dataPoints = []

# Läs in testpunkter (x, y)
with open(textfile1, "r") as file:
    for line in file:
        line = line.strip()
        if not line or line.lower().startswith("test points"):
            continue

        # Tar bort text mellan parenteser
        match = re.search(r"\(([^)]+)\)", line)
        if match:
            coords = match.group(1)
            x_str, y_str = coords.split(",")
            x, y = float(x_str.strip()), float(y_str.strip())
            testPoints.append((x, y))

# Läs in datapunkter (x, y, label)
with open(textfile2, "r") as file:
    next(file)
    for line in file:
        line = line.strip()
        if not line:
            continue
        row = [item.strip() for item in line.split(",")]
        if len(row) >= 3:
            x, y, label = float(row[0]), float(row[1]), int(row[2])
            dataPoints.append((x, y, label))

def eucdist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Klassificering med k närmaste grannar (k-NN)
def classify_point(point, data, k=10):
    distances = [(eucdist(point, (x, y)), label) for x, y, label in data]
    distances.sort(key=lambda d: d[0])
    k_nearest = distances[:k]

    labels = [label for _, label in k_nearest]
    majority = max(set(labels), key=labels.count)

    return majority

# Klassificera alla testpunkter
for tp in testPoints:
    predicted_label = classify_point(tp, dataPoints, k=10)
    print(f"Punkt {tp} klassificeras som: {predicted_label}")

# Visualisering
plt.figure(figsize=(8,6))

for x, y, label in dataPoints:
    if label == 0:
        plt.scatter(x, y, color="red", label="Pichu" if "Pichu" not in plt.gca().get_legend_handles_labels()[1] else "")
    else:
        plt.scatter(x, y, color="yellow", label="Pikachu" if "Pikachu" not in plt.gca().get_legend_handles_labels()[1] else "")

for x, y in testPoints:
    plt.scatter(x, y, color="blue", marker="x", s=100, label="Testpunkt" if "Testpunkt" not in plt.gca().get_legend_handles_labels()[1] else "")

plt.xlabel("Bredd (cm)")
plt.ylabel("Längd (cm)")
plt.title("Klassificering av Pichu och Pikachu (k=10)")
plt.grid(True)
plt.legend()
plt.show()

# Användaren får mata in egna mått för att se vilken pokemon det är
def get_user_input():
    while True:
        try:
            x = float(input("Ange bredden på din pokemon i cm: "))
            y = float(input("Ange längden på din pokemon i cm: "))

            if x < 0 or y < 0:
                print("Fel: Bredd/längd kan inte vara negativ. Försök igen.")
                continue

            return (x, y)
        except ValueError:
            print("Fel: Du måste mata in ett numeriskt värde.")

user_point = get_user_input()
predicted_label = classify_point(user_point, dataPoints, k=1)

if predicted_label == 0:
    print("Det är en Pichu")
else:
    print("Det är en Pikachu")