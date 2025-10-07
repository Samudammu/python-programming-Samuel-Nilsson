import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Läser in filen utan header och ger kolumnerna x eller y
data = pd.read_csv(
    r"C:\Users\samue\python-programming-Samuel-Nilsson\Labs\Lab3\unlabelled_data.csv",
    header=None,
    names=["x", "y"])

# Ger k negativ lutning
# Väljer m så att linjen går genom mitten av punkterna och klassificerar dem
k = -0.5
m = data['y'].mean() - k * data['x'].mean()
data['label'] = np.where(data['y'] > k * data['x'] + m, 1, 0)

# Rita med färg efter klass
plt.scatter(data[data['label']==0]['x'], data[data['label']==0]['y'], color='blue', label='Klass 0')
plt.scatter(data[data['label']==1]['x'], data[data['label']==1]['y'], color='green', label='Klass 1')
plt.plot(data['x'], k * data['x'] + m, color='red', label=f"y = {k:.2f}x + {m:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Labelled data")
plt.legend()
plt.show()

# Skapar en ny csv fil där punkterna är Labelled 0 eller 1
data.to_csv(r"C:\Users\samue\python-programming-Samuel-Nilsson\Labs\Lab3\labelled_data.csv",
            index=False)