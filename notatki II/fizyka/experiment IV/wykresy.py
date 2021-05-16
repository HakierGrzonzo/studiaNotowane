import matplotlib.pyplot as plt
import numpy as np


figScale = .4


accel = plt.figure(figsize=(figScale * 16, figScale * 9))

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

z = [float(x[0]) for x in dataZ]
uz = [float(x[1]) for x in dataZ]
p = [float(x[0]) for x in dataP]
up = [float(x[1]) for x in dataP]

plt.grid()
plt.errorbar(p, z, uz, up, 'none', capsize=4)

trendline = np.linspace(min(p) - 50, max(p) + 50, 1000)
plt.plot(trendline, trendline * 0.13677 - 38.3677)
plt.ylabel(r"$z^2$ [$cm^2$]")
plt.xlabel(r"$P$ [$Pa$]")
plt.savefig("PfromZ2.pgf")
plt.show()
