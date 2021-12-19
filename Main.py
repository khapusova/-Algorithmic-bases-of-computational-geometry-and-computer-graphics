import math
def show(x,y):
    plt.figure(figsize=(540 / 96, 960 / 96), dpi=96)
    plt.scatter(x, y)
    plt.show()
def new_coord(X, Y,x0=480,y0 = 480, a= math.radians(40)):
    Y1,X1 =[],[]
    for x,y in zip(X,Y):
        X1.append(x*math.cos(a)-math.sin(a)*y+480)
        Y1.append(math.sin(a)*x+y*math.cos(a)+480)
    return [X1,Y1]

import matplotlib.pyplot as plt
file = open("/home/diana/Desktop/DS3.txt", 'r')
list = file.readlines()
x = [int(list[a].split(" ")[0]) for a in range(len(list))]
y = [int(list[a].split(" ")[1]) for a in range(len(list))]
show(new_coord(x,y)[0], new_coord(x,y)[1])
