# Chapter Two Exercises:
### 1- Insertion sort:
- 2-1

    -Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the
    array A = {31 41 59 26 41 58}

    ```
insertion_sort(A,n)
    for i = 2 to n
        key = A[i]
        j = i - 1
        while j>0 and A[j]>key
            A[j+1] = A[j]
            j -=1
        A[j+1] = key
    opertations on the array result:
    index 1  2  3  4  5  6
    1 - {26 _31 _41 _59 41 58}
    2 - {26 31 41 41 _59 58 } 
    3 - {26 31 41 41 58 _59}
    ```
>Note: the __'_'__ indicated to shifted number.
---
- 2-2

    - 2.1-2
    Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order

```
insertion_sort(A,n):
    for i = 2 to n
        key = A[i]
        j = i - 1
        while j>0 and A[j]<key
            A[j+1] = A[j]
            j -=1
        A[j+1] = key

```
    >Notice that it the approx the same procedure to increasing sorting.

- 2-3
     
     Write pseudocode for linear search, which scans through the sequence, looking
    for v. Using a loop invariant, prove that your algorithm is 
        
```
linear_s(A,v):
    output = NIL
    for i = 1 to n
        if A[i] == v:
            output = i
    return output

```