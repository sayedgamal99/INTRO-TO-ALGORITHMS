# Chapter 6 : Heap Sort

### Part 4 : Heap Sort Algorithm

## <font color ='white'> Algorithm </font>

```
Heap-Sort(A)
    Build-MaxHeap(A)
    for i = A.length down to 2
        swap(A[1],A[i])
        A.heap-size-=1
        Max-Heapify(A,1)
```

<br>

## $\color{white}O(nlogn)$<font color='white'> is Running Time for Heap Sort</font>

<br>

<p align ='center'>
    <img src='https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/Heapsort.png?raw=true' alt="alt text">
</p>
