# CH 7 : Quick Sort

### 7.1-1
#### Illustrate the operation of PARTITION on the array A = A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11].

```
A = [9, 19, 13, 5, 12, 8, 7, 4, 21, 2, 6, 11]
A = [9, 5, 13, 19, 12, 8, 7, 4, 21, 2, 6, 11]
A = [9, 5, 8, 19, 12, 13, 7, 4, 21, 2, 6, 11]
A = [9, 5, 8, 7, 12, 13, 19, 4, 21, 2, 6, 11]
A = [9, 5, 8, 7, 4, 13, 19, 12, 21, 2, 6, 11]
A = [9, 5, 8, 7, 4, 2, 19, 12, 21, 13, 6, 11]
A = [9, 5, 8, 7, 4, 2, 6, 12, 21, 13, 19, 11]
A = [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12]
```

---


### 7.1-2
#### What value of q does PARTITION return when all elements in the array A[p..r] have the same value? Modify PARTITION so that q = $\left \lfloor{(p+r)/2}\right \rfloor$ when all elements in the array A[p..r] have the same value.

```
It will return the last value of A, since the condition satisfied all time,
and A[i] would be swapped with A[r] (i = r)
then returned q = r.
```
```py
modified Partation funciton would be:

Partation(A,p,r)
    x = A[r]
    i = p-1
    for j = p to r-1
        if A[j] <= x
            i+=1
            swap(A[i],A[j])
    if i+1 == r
        return (p+r)//2
    else    
        swap(A[i+1],A[r])
        return i+1
```

---


### 7.1-3
#### Give a brief argument that the running time of PARTITION on a subarray of size n is $\Theta(n)$.

```
Since Partation function would be always iterate to all elements in subarray A[p..r] (p,r passed to it)
and length of subarray would be always n or less in recursive calls.
the running time of it would be just linear.
```

---


### 7.1-4
#### How would you modify QUICKSORT to sort into nonincreasing order?

```
we can modify the condition of if statement.
from : if A[j] <= x
to : if A[j] > x
and it would sort the Array in decreasing order.
```

> Note: Implementation of Quick Sort, could do the both ways, by specifying second parameter to be $\color{steelblue}False$ or don't specify it.

### Implementation:

[`Check Implementation`](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/QuickSort.py)


---
