# Chapter two : Analysing Algorithms 
Most of this book assumes a generic one-processor, random-access machine (RAM) model of computation as the implementation technology, with the 
understanding that algorithms are implemented as computer programs. In the RAM 
model, **instructions execute one after another**, with no concurrent operations. The 
RAM model assumes that **each instruction takes the same amount of time**.

- instructions can be
    - **arthmetic** :\
    (add , substract , multiply , devide , reminder,foor ,ceiling)
    - **data movement** :\
    (load , store, copy)
    - **control** :\
    (conditional and unconditional branch, call and return)

- assume a limit size of each word of data ,for example: if n is the size of data word:
    we assume integers represented by $clg_n$ bits for some constant c>=1
---
### Some notes:
> exponential has no constant time in general instruction but it would be in this book\
> we will treat 2^k as a constant time instruction as long as k is small enough positive number
```
insertion_sort(A,n)                 cost    times
        for i = 2 to n              c1      n
            key = A[i]              c2      n-1
            // insertion A[i] into the sorted sequance A[1..j-1]
            j = i - 1               c3      n-1
            while j>0 and A[j]>key  c4      sum(tj)2 to n
                A[j+1] = A[j]       c5      sum(tj-1)2 to n
                j -=1               c6      sum(tj-1)2 to n
            A[j+1] = key            c7      n-1
```
> Finally it can be written **in BEST CASE** as A*n + B to be **linear Function**
> And the **WORST CASE** can be written as An^2 + Bn +c as**quadratic function** 

We shall now make one more simplifying abstraction: it is the rate of growth,
or order of growth, of the running time that really interests us:
- we consider only leading term of formula (An^2 in worst case)
- we ignore term's constant
to be in the end for the worst case running time for INSERTION SORT:
$$\theta(n^2)$$

> n^2 algorithm, for example, will\
>run more quickly in the worst case than a n^3 algorithm
---