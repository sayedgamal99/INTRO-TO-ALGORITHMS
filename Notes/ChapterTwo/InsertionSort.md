# Chapter Two: Insertion Sort
#### This chapter contain insertion sort as *sorting* Algorithms to be disscussed, this kind of sorting algorithms has the advantage when  it is applied to small group of numbers.. as mentioned in perverios chapter exercices this algorithms has the advantage when __n atmost some Tens of numbers__
## Time complexity is around  __cn^2__ 
when c is constant propotional with n.


---
>Note: All Arrays in this book are __1__ based not __0__ based for index
- This is pseudocode for insertion sort:
```
insertion_sort(A,n)
for i = 2 to n
    key = A[i]
    j = i - 1
    while j>0 and A[j]>key
        A[j+1] = A[j]
        j -=1
    A[j+1] = key

```
- loop invariants must be true:

    - before the loop starts
    - before each iteration 
---
---