# Chapter Two : Designing Algorithms
Many useful algorithms are **recursive** in structure: to solve a given problem, they
call themselves recursively one or more times to deal with closely related subproblems. These algorithms typically follow a **divide-and-conquer** approach.

---
### Divide:
- Divide the problem into number of subsequance that are smaller instance of the same problem
### Conquer:
- Conquer the subproblems by solving them recursively.until subproblems sizes small enough to solving each straigh-forward.
### Combine:
- Combine the all solutions for subproblems together to get the whole solution.


---
### Merge-Sort follows Divide and Conquer:
- Divide the problem of size n into two subsequences of n/2 each size.
- Conquer each subsequance by sorting recursively using merge sort.
- combine the two sorted subsequences to produce the sorted solution.
> This **merge-sort** take time $\theta(n)$.

---

#### Pseudocode for merge-sorting:
```
Merge(A,p,q,r):
    n1 = q-r+1
    n2 = r -q
    L[n1],R[n2]
    for i = 1 to n1:
        L[i] = A[p+i-1]
    for j=1 to n2:
        R[j] = A[q+j]
    i = 1
    j = 1
    for k = 1 to r:
        if L[i]<=R[j]:
            A[k]=L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1
        

```
---

### Note:
>To avoid examning the four cases that arise depending on whether than each of p and r is odd and even we use Ceil and Floor.

- Example from above procedure:
    - A[p..q] containing $\lceil {n\over2} \rceil$ elements
     and the A[q+1..r] containing $\lfloor{n\over2} \rfloor$ elements.
    
---



$$\lceil x \rceil$$
This expression denotes the smallest **integer** greater than or equal to X

$$\lfloor x \rfloor$$
This expression denotes the greatest **integer** less than or equal to X




