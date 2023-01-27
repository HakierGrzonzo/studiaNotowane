# Relations
## Binary relation

A binary relation over sets X and Y is a new set of ordered pairs (x, y).

A binary relation is a subset of Cartesian product

We write it as $x R y$.

### Non-strict partial order:
If a relation is:
- reflexivity: $a \preceq a$
- transitivity: $a \preceq b$ and $b \preceq c$ then $a \preceq c$
- antisymetry: $a \preceq b$ and $b \preceq a$ then $a = b$

So a relation over set $\{1, 2, 3\}$:
$<(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)>$ is a non-strict partial order over it  

### strict partial order:
- irreflexitivity: (not $a \prec a$)
- transitivity: $a \prec b$ and $b \prec c$ then $a \prec c$
- asymmetry: if $a \prec b$ then not $b \prec a$ (implied by irreflexivity and transitivity)

### Linear (total) order

- reflexivity: $a \preceq a$
- transitivity: $a \preceq b$ and $b \preceq c$ then $a \preceq c$
- antisymetry: $a \preceq b$ and $b \preceq a$ then $a = b$
- strongly connected: if $a \preceq b$ or $b \preceq a$ 

### Examples

- non-strict partial and total order ⇾ $\leq$
- strict partial order ⇾ $<$

#### Sharkovskii's order

Every natural number n can be written as $2^r p$, where p is odd and r is the maximum exponent such that …

$2^r p \prec 2^s q$ if:
- r < s and p > 1
- r = s …

# Graphs
If all pairs f vertices of G, then G is called a connected graph.

A connected component is a maximaly connected subgraph of G.

# Subdivisions
