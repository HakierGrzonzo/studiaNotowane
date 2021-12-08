nums = list([list([x.rjust(6, " ") for x in w.split("\n")]) for w in [
r"""
  ___  
 / _ \ 
| | | |
| |_| |
 \___/ 
""",
r"""       
 _ 
/ |
| |
| |
|_|
""",
r"""       
 ____  
|___ \ 
  __) |
 / __/ 
|_____|
""",
r"""       
 _____ 
|___ / 
  |_ \ 
 ___) |
|____/ 
""",
r"""       
 _  _   
| || |  
| || |_ 
|__   _|
   |_|  
""",
r"""       
 ____  
| ___| 
|___ \ 
 ___) |
|____/ 
""",
r"""       
  __   
 / /_  
| '_ \ 
| (_) |
 \___/ 
""",
r"""       
 _____ 
|___  |
   / / 
  / /  
 /_/   
""",
r"""       
  ___  
 ( _ ) 
 / _ \ 
| (_) |
 \___/ 
""",
r"""       
  ___  
 / _ \ 
| (_) |
 \__, |
   /_/ 
"""
]])

def bigprint(num):
    num = str(num)
    res = [""] * 6
    for c in num:
        big = nums[int(c)]
        for i in range(1, 6):
            res[i] += big[i]
    return "\n".join(res[1:])
if __name__ == "__main__":
    print(bigprint(int(input("Podaj liczbę: "))))
