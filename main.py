import matplotlib.pyplot as plt
file = open("/home/diana/Desktop/DS3.txt", 'r')
list = file.readlines()
keys = [int(list[a].split(" ")[0]) for a in range(len(list))]
vals = [int(list[a].split(" ")[1]) for a in range(len(list))]
plt.figure(figsize=(540/96, 960/96), dpi=96)
plt. scatter(keys, vals)
plt.show()