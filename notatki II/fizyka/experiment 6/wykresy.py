import matplotlib.pyplot as plt
import numpy as np


figScale = .35


accel = plt.figure(figsize=(figScale * 16, figScale * 11))

plt.title(r"Kwadrat $t^2$ czasu spadku a wysokość $H$")

dataT = [x.split("\t") for x in """
0,091	0,040
0,135	0,061
0,178	0,034
0,220	0,040
0,301	0,036
""".strip().replace(",", ".").split("\n")]

dataH = [x.split(" ") for x in """
52.4 0.1
75 0.1
85 0.1
111,3 0,1
148,7 0,15
""".strip().replace(",", ".").split("\n")]

t = [float(x[0]) for x in dataT]
ut = [float(x[1]) for x in dataT]
h = [float(x[0]) for x in dataH]
uh = [float(x[1]) for x in dataH]

plt.grid()
plt.errorbar(h, t, ut, uh, 'none', capsize=4)

trendline = np.linspace(min(h) - 10, max(h) + 10, 1000)
plt.plot(trendline, trendline * 0.002176 - 0.02078)
plt.ylabel(r"$t^2$ [$s^2$]")
plt.xlabel(r"$H$ [$cm$]")
plt.savefig("HfromT.pgf")
plt.close()
