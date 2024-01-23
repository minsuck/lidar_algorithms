from matplotlib import pyplot as plt
import numpy as np
import math

# 1:360=x:2pi 
tic = math.radians(360/505)
# math.radians()
#lidars = np.random.rand(505)

f = open("lidar.txt", 'r')
line = f.readline()
lidars = line.split(',')
n = 505
result = [lidars[i * n:(i + 1) * n] for i in range((len(lidars) + n - 1) // n )]
f.close()

for frame in result:
    x = []
    y = []

    for i in range(n):
        if float(frame[i]) > 0.0:
            x.append(float(frame[i])*math.cos(i*tic))
            y.append(float(frame[i])*math.sin(i*tic))

    plt.figure(figsize=(5,5))
    plt.scatter(x, y)
    plt.show()

