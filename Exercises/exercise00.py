# övning 0.1

import math

c = 7
a = 5

b = c ** 2 - a ** 2
print(math.sqrt(b))



# övning 0.2

c = 300
t = 365

a = c / t
print(f"Accuracy: {a:.2f}")



# övning 0.3

tp = 2
fp = 2
fn = 11
tn = 985

a = (tp + tn) / (tp + fp + fn + tn)
print(a)



# övning 0.4
 
m = 1
k = (1 - 4) / (0 - 4)
print(f"{k}x + {m}")



# övning 0.5

import math

distans = math.sqrt((-2 - 3) ** 2 + (5 - 4) ** 2)
print(distans)



# övning 0.6

import math

p1 = (2, 1, 4)
p2 = (3, 1, 0)

distans = math.sqrt((p1[0] - p2[0]) **2 + (p1[1] - p2[1]) **2 + (p1[2] - p2[2]) **2)
print(f"{distans} l.u.")