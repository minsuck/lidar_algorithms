import matplotlib.pyplot as plt
import numpy as np
import math
import mydbscan as dbs

"""
tic = math.radians(360/505)
n = 505
point = []


f = open("lidar.txt", 'r')
line = f.readline()
lidars = line.split(", ")
result = [lidars[i * n:(i + 1) * n] for i in range((len(lidars) + n - 1) // n )]
f.close()

frame = result[5]
for i in range(len(frame)):
  try:
    float_number = round(float(frame[i]), 5)
  except ValueError:
    continue
  if float_number >= 0.1:
    x = float_number*math.cos(i*tic)
    y = float_number*math.sin(i*tic)
    point.append([x,y])

X = np.array(point, float)

#plt.scatter(X[:,0], X[:,1])
#plt.show()

def display_result(labels, title):
    result_dict = dict()
    for idx, label in enumerate(labels):
        if label not in result_dict.keys():
            result_dict[label] = list()
            result_dict[label].append([ X[idx, 0], X[idx, 1]])
        else:
            result_dict[label].append([ X[idx, 0], X[idx, 1]])

    for key, value in result_dict.items():
        print(key, len(value))

    for key, value in result_dict.items():
        data = np.array(value)
        plt.scatter(data[:,0], data[:,1], label=f"{key}")
    plt.title(title)
    plt.legend()
    plt.show()
    
my_dbscan = dbs.MyDBSCAN(eps=0.5, min_points=5)
labels = my_dbscan.fit(X)
display_result(labels, "My DBSCAN")

"""
obj = [[1, 350, 0.0, 0.0],
        [-1, 55, -77.43024406305427, 75.92814313361473],
        [2, 29, -26.40512657506032, 5.27480273646435],
        [3, 9, -182.17159416996867, -34.52791667752086],
        [4, 32, 89.30275897558145, -3.7202408191781093],
        [5, 18, 54.28736240288558, 42.15965478457976],
        [6, 12, 11.551704252251037, 129.20762431071662]]
    
plt.xlim(-10,10)
plt.ylim(-16.5,0)
for o in obj:
  #plt.scatter(o[1], o[2], label=f"{o[0]}")
  objx = o[2]
  objy = o[3]
  objz = 0
  
  fl = 3.79 # focal lenght
  camx = 0
  camy = -10 + fl
  camz = 10
  
  leny = -10
  lenx = ((leny - objy) / (camy - objy) * (camx - objx) + objx) * -1
  lenz = ((leny - objy) / (camy - objy) * (camz - objz) + objz) * -1
  print(o[0], lenx, lenz)
  plt.scatter(lenx, lenz, label=f"{o[0]}")
    
plt.title("title")
plt.legend()
plt.show()