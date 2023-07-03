# Chapter 6 : Heap Sort
### Part 3 : Building Max Heap

## Brief
- We can use Max-Heapify( from previous section) procedure to convert the array A[1..n] in $\color{white}\text{bottom-up manner}$ into $\color{white}{max-Heap}$
- Elements in A[n//2 +1 .. n] are all leaves of the tree.

## Procedure
```
Build-MaxHeap(A)
    A.heap-size = A.length
    for i = (n//2) down to 1
        Max-Heapify(A,i)
```

<p align="center">
  <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/build_maxheap.png?raw=true" alt="alt text">
</p>


## Running Time: $\color{white}{O(n)}$
- we can build max-heap from an array in linear time

> proof p159

---