# CH 7 : Quick Sort


### This algorithm take many advantages like:



- Running Time is $\color{steelblue}O(nlgn)$.
- A Divide and Conquer approach used.
- Consumes no extra memory since sorting is $\color{steelblue}\text{in-place}$.

### Quick Sort Algorithm

```py
Quick-Sort(A,p,r)
    q =  Partation(A,p,r)
    Quick-Sort(A,p,q-1)
    Quick-Sort(A,q+1,r)
```

```py
Partation(A,p,r)
    x = A[r]
    i = p-1
    for j = p to r-1
        if A[j] <= x
            i+=1
            exchange(A[i],A[j])
    exchange(A[i+1],A[r])
    return i+1
```

### How it works?
```
In brief, we try to sort the array A in place by swapping elements.

The algorithm picks an element to use as the pivot element,
such that all elements before it are less than its value, and all elements after it are higher than its value.

Let x at position r be the pivot element.
We segment the array A into 3 regions at the end:
(elements less than x, pivot element, elements higher than x)

As we try to segment the elements, we check for each value along the way,
if it belongs to the lower-value group of numbers or the higher-value 
group. We do swapping all the way to reach the result, then (recursively)
do that to get our sorted array.

```

<br>


### Visualize it:

<p align ='center'>
    <img src='https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/QuickSort2.png?raw=true' alt="alt text">
</p>



### Example:
<p align ='center'>
    <img src='https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/QuickSort1.png?raw=true' alt="alt text">
</p>



---