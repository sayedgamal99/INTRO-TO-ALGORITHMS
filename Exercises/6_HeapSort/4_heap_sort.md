# Chapter 6 : Exercises

## Part four : Heap Sort:

<br>

### 6.4-1
- Using illustrate the operation of HEAPSORT on the array A[5, 13, 2, 25, 7, 17, 20, 8, 4].

```
build max-heap:

[5, 13, 20, 25, 7, 17, 2, 8, 4]
[5, 25, 20, 13, 7, 17, 2, 8, 4]
[25, 5, 20, 13, 7, 17, 2, 8, 4]
[25, 13, 20, 5, 7, 17, 2, 8, 4]
[25, 13, 20, 8, 7, 17, 2, 5, 4]

sorting:

[4, 13, 20, 8, 7, 17, 2, 5, 25]
[20, 13, 4, 8, 7, 17, 2, 5, 25]
[20, 13, 17, 8, 7, 4, 2, 5, 25]
[5, 13, 17, 8, 7, 4, 2, 20, 25]
[17, 13, 5, 8, 7, 4, 2, 20, 25]
[2, 13, 5, 8, 7, 4, 17, 20, 25]
[13, 2, 5, 8, 7, 4, 17, 20, 25]
[13, 8, 5, 2, 7, 4, 17, 20, 25]
[4, 8, 5, 2, 7, 13, 17, 20, 25]
[8, 4, 5, 2, 7, 13, 17, 20, 25]
[8, 7, 5, 2, 4, 13, 17, 20, 25]
[4, 7, 5, 2, 8, 13, 17, 20, 25]
[7, 4, 5, 2, 8, 13, 17, 20, 25]
[2, 4, 5, 7, 8, 13, 17, 20, 25]
[5, 4, 2, 7, 8, 13, 17, 20, 25]
[2, 4, 5, 7, 8, 13, 17, 20, 25]
[4, 2, 5, 7, 8, 13, 17, 20, 25]
[2, 4, 5, 7, 8, 13, 17, 20, 25]

```

---

### 6.4-2
- Argue the correctness of HEAPSORT using the following loop invariant: At the start of each iteration of the for loop of lines 2–5, the subarray A[1..i] is a max-heap containing the i smallest elements of A[1..n], and the subarray A[i+1..n] contains the n - i largest elements of A[1..n], sorted.

    - Recall Heap Sort Algorithm build in top of max-heapify funciton

[Check Algorithm](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/HeapSort.py)

```python

def Heap_Sort(A):
    Build_maxHeap(A)
    for i in range(len(A)-1,-1,-1):
        A[0],A[i] = A[i],A[0]
        print(A)
        max_heapify(A,i,0)
    return A

```

```
1- after building maxheap: we have in first iteration max-heap property satisfied.
2- first iteration we get last element and swap it with first element(max element becuase of max-heap property).
3- after swaping we violate max-heap property, so we need to max-heapify it again to put first element in it's proper place.
4- at each new iteration max-heap property satisfied because of max-heapify system.
5- i decreases at each iteration, so we get each time (max) of ramaining element (first element of heap), becuase we have max-heapify satisfies.
6- i elements are i smallest elements in A at each time, but not sorted.
7- remaining elements are n-i element and they are sorted.
```


---

### 6.4-3
#### What is the running time of HEAPSORT on an array A of length n that is already sorted in increasing order? What about decreasing order?



- Recall that running time of heap sort depend on it's smaller functions running time. 
    - Max-heapify $O(lgn)$
    - build max-heap $O(nlgn)$

so when A is **Sorted** max-heapify will take always $O(lgn)$, and then build max-heap will take $O(nlgn)$.\
total sorting will take $O(nlgn)$

when A is **decreasing order sorted**: max-heap property satisfied, so max-heapify would take $O(1)$ at beginning,\
build max-heap would take $O(n)$,\
then total sorting would take $O(nlgn)$, because when we sorting we get last element and replace with A[0] which is violate max-heap property, then it would take usual time of 
max-heapify $O(lgn)$ to fix that then get next element and so on.
total sorting would be $O(nlgn)$

---
