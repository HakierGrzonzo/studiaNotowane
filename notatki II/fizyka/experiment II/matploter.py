import matplotlib.pyplot as plt
import numpy as np

graphScale = .9

x = [36, 50, 64]
xerr = 1

y1 = [0.350, 0.423, 0.418]
y1err = [0.0022, 0.0020, 0.0019]
y2 = [0.493, 0.485, 0.477]
y2err = [0.0017, 0.0020, 0.0021]

plt.figure(figsize=(7 * graphScale, 4 * graphScale))
plt.subplot(1, 2, 1)
plt.xlabel("Powierzchnia [$cm^2$]")
plt.ylabel("$f_s$")
plt.title("Powierzchnia a $f_s$ dla \\texttt{tektura + tektura}")
#plt.plot(x, y1, color="orange")
plt.errorbar(x, y1, y1err, xerr, 'none', capsize=2)
plt.grid()
plt.ylim([0, .8])

plt.subplot(1, 2, 2)
plt.xlabel("Powierzchnia [$cm^2$]")
plt.ylabel("$f_s$")
plt.title("Powierzchnia a $f_s$ dla \\texttt{folia + folia}")
#plt.plot(x, y2, color="orange")
plt.errorbar(x, y2, y2err, xerr, 'none', capsize=2)
plt.grid()
plt.ylim([0, .8])
plt.tight_layout()

plt.savefig("someGraph.pgf")
#plt.show()
