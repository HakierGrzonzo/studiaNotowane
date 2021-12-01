[filmik hinduski](https://youtu.be/Fi2spwg7PI8)
[fajne wytłumaczenie](http://ben-tanen.com/adaptive-huffman/)

# Formuła na początkowe wagi:
$$
w = (2 \cdot n) - 1
$$
Gdzie n to ilość symboli.

Na przykład dla alfabetu angielskiego:
$$
n = 26
$$
$$
w = (2 \cdot 26) - 1 = 51
$$

# Fixed code

$m$ - liczba liter
$e, n$ - liczby naturalne

Musi zostać spełniony warunek:
$$
m = 2^e + n,\quad\text{gdzie}\quad 0 \leq n \leq 2^e
$$
Następnie kodujemy literę $a_k$ jako:
- $(e+1)$ bitową wartość $(k-1)$ jeśli $1 \leq k \leq 2n$
- $e$ bitową wartość $(k -n  -1)$ jeśli $k > 2n$