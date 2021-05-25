import matplotlib.pyplot as plt
import numpy as np


figScale = .35


accel = plt.figure(figsize=(figScale * 16, figScale * 11))

plt.title(r"Ciśnienie $P$ a kwadrat zasięgu $z^2$")

dataP = [x.split("\t") for x in """
587,37	19,58
489,47	19,58
440,53	19,58
391,58	19,58
342,63	19,58
""".strip().replace(",", ".").split("\n")]

dataZ = [x.split("\t") for x in """
41,0	 0,48 
31,4	 0,68 
20,9	 0,73 
13,9	 0,53 
9,0	 0,86
""".strip().replace(",", ".").split("\n")]

dataH = [x.split("\t") for x in """
2,449	0,082
2,236	0,089
2,121	0,094
2,000	0,100
1,871	0,107
""".strip().replace(",", ".").split("\n")]

dataz = [x.split(" ") for x in """
6,4 0,24
5,6 0,34
4,57 0,37
3,73 0,27
3,0 0,43
""".strip().replace(",", ".").split("\n")]
z = [float(x[0]) for x in dataZ]
uz = [float(x[1]) for x in dataZ]
z1 = [float(x[0]) for x in dataz]
uz1 = [float(x[1]) for x in dataz]
p = [float(x[0]) for x in dataP]
up = [float(x[1]) for x in dataP]
h = [float(x[0]) for x in dataH]
uh = [float(x[1]) for x in dataH]

plt.grid()
plt.errorbar(p, z, uz, up, 'none', capsize=4)

trendline = np.linspace(min(p) - 50, max(p) + 50, 1000)
plt.plot(trendline, trendline * 0.13677 - 38.3677)
plt.ylabel(r"$z^2$ [$cm^2$]")
plt.xlabel(r"$P$ [$Pa$]")
plt.savefig("PfromZ2.pgf")
plt.close()

accel = plt.figure(figsize=(figScale * 16, figScale * 11))

plt.title(r"zasięg $z$ a wysokość słupa wody $\sqrt{h}$")

plt.tight_layout(pad=3)
plt.grid()
plt.errorbar(h, z1, uz1, uh, 'none', capsize=4)
trendline = np.linspace(min(h) - .3, max(h) + .3, 1000)
plt.plot(trendline, trendline * 6.1176 - 8.404)

plt.ylabel(r"$z$ [$cm$]")
plt.xlabel(r"$\sqrt{h}$ $\left[cm^{\frac{1}{2}}\right]$")
plt.savefig("ZfromH.pgf")
