dane = open("pomiary.txt").read()

distance = 5

for line in dane.replace("   ", "\t").strip().split("\n")[1:]:
    if line == "--":
        distance = 3
        continue
    t1, t2 = [float(x) for x in line.replace(",", ".").split("\t")]
    out = "{:.3f}\t& {:.3f}\t& {:.3f}\t& {:.3f} \t\\\\\\hline".format(
            t1,
            t2,
            t1 - t2,
            distance / ((t1 - t2) /2) )
    print(out.replace(".", ","))
