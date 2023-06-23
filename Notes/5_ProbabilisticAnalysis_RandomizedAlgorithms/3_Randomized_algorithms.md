# Chapter Five : Probabilistic Analysis and Randomized Algorithms

## Part three : Randomized Algorithms

<br>

- Instead of assuming a distribution
  of inputs, we impose a distribution. In particular, before running the algorithm,
  we $\color{white}\text{randomly permute}$ the candidates in order to enforce the property that every
  $\color{green}\text{permutation is equally likely}$.

```
HIRE-ASSISTANT(n)
    randomly permute list of candidates     # the only change from previous
    best = 0
    for i = 1 to n
        interview candidate i
        if candidate i is better than best candidate
            best = i
            hire candidate i
```

- since the random permutation makes the $\color{green}\text{input order irrelevant}$. The randomized
  algorithm performs badly only if the random-number generator produces an “unlucky” permutation.
  For the hiring problem, the only change needed in the code is to randomly permute the array.

> There is two methods for doing that:

## 1-Permute random array

- In this method we re-ordering the array in way it would satisfied our need:
  - Approach for re-ordering the list of candidates:
    - randomly -using random generator- give each candidate a rank which we will use it as key to sorting the candidates based on it.

```
Permute-By-Sorting(A)
    n = A.length()
    P = [1..n] # new list
    for i = 1 to n:
        P[i] = RANDOM(1,n^3)
    sort A using P as sort keys

```

- Assuming RANDOM work in $O(1)$ time we can describe the permutation of candidates as $\Omega(nlogn)$ if we use comparison sort.

---

<br>
<br>

## 2- Permute in-place

- Second method for permuting the list of candidates is doing it in place.
  - That would happen in $\color{green}{\text{Linear}}$ time complexity $O(n)$

```
Randomize-In-Place(A)
    n = A.length()
    for i = 1 to n:
        swap A[i] with A[RANDOM(i,n)]

```

---
