import matplotlib.pyplot as plt
import numpy as np
import csv

figScale = .4


accel = plt.figure(figsize=(figScale * 16, figScale * 9))

plt.title(r"Przyspieszenie $a\left(t\right)$")
# import Data

accelData = csv.reader(open("raw data.csv"), delimiter=";")
accelY = []
accelX = []
firstItter = True
for row in accelData:
    if firstItter:
        firstItter = False
        continue
    else:
        xDim = float(row[0].replace(',', "."))
        if 2.5 < xDim < 6.5:
            accelX.append(xDim)
            accelY.append(-float(row[2].replace(',', '.')) - 9.81)
plt.plot(accelX, accelY, color="black")
plt.xlabel(r"Czas $t$ [$s$] $\pm 0,0010s$")
plt.ylabel(r"Przyspieszenie $a$ $\left[\frac{m}{s^2}\right]$ $\pm 0,0048\frac{m}{s^2}$")
plt.grid()
plt.savefig("accel.pgf")
plt.close(accel)

scatterData = """
0    -0,013207226    0    0
0,963244866    -0,32270552    0,821355962    -0,240332673
1,672594825    -0,679549327    1,704939448    -0,46783822
2,536286144    -1,160074775    2,523833054    -0,751279301
3,260604275    -1,565085092    3,307872385    -1,112976246
""".strip().replace(",",".").split("\n")

lin = plt.figure(figsize=(figScale * 16, figScale * 9))
plt.title(r"Linie trendu $z_i\left(T_i\right)$")

y1 = []
x1 = []
y2 = []
x2 = []

for line in scatterData:
    a, b, c, d = [float(x) for x in line.split(" "*4)]
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

firstTrend = np.linspace(min(x1), max(x1), 100)
secondTrend = np.linspace(min(x2), max(x2), 100)


plt.grid()

plt.scatter(x1, y1, 9, color="orange")
plt.scatter(x2, y2, 9, color="blue")

plt.plot(firstTrend, firstTrend * -.48483 + .06956, color="orange", label="Maksima")
plt.plot(secondTrend, secondTrend * -.32832 + .034343, color="blue", label="Minima")
plt.legend()


plt.ylabel(r"$z_i$")
plt.xlabel(r"$T_i$ $\left[s\right]$")
plt.savefig("lin.pgf")
