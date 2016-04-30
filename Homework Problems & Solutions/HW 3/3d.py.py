import matplotlib.pyplot as plt
import numpy as np
import math
list1 = []
list2 = []
list4 = []
k = 1
c = 0
c1 = 10
c2 = 5
fk1 = []
fk2 = []


while (k < 3000):
    list1.append(k)
    list2.append(k * math.log(k))
    k = k + 500
    fk1.append(c1 * k)
    fk2.append( c2 * k)
    
while (c <= len(list1)):
    list4.append(3 * c)
    c = c + 10    

line1 = fk1
line2 = fk2
line3 = list1


groups = (len(list1))
index = np.arange(groups)           
plt.plot(line1)
plt.plot(line2)
plt.plot(line3)
plt.ylabel("klogk")
plt.xlabel("k")

plt.xticks(index, list1, rotation=90)
plt.xticks(index, list2)

plt.margins(0.025)
plt.show()