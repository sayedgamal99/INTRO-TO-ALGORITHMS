# Chapter 6 : Exercises

## Part Five : Priority Queue:

<br>


[Check Implemetation Max Heap Priority Queue](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/PriorityQueue_MaxHeap.py)

### 6.5-1
#### Illustrate the operation of HEAP-EXTRACT-MAX on the heap A [15, 13, 9, 5, 12, 8, 7, 4, 0, 6,2,1]

<p align='center'>
    <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/priorityQEx1heap.png?raw=true" alt='alt text'>
</p>

```
A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6,2,1]
1.0- A = [1 , 13, 9, 5, 12, 8, 7, 4, 0, 6,2]
    1.1- A = [13 , 1, 9, 5, 12, 8, 7, 4, 0, 6,2]
    1.2- A = [13 , 12, 9, 5, 1, 8, 7, 4, 0, 6,2]
    1.3- A = [13 , 12, 9, 5, 6, 8, 7, 4, 0, 1,2]
```

here is a gif to notice the operations:

<p align='center'>
    <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/extract_max_heap.gif?raw=true" alt='alt text'>
</p>


---

### 6.5-2 
#### Illustrate the operation of MAX-HEAP-INSERT(A,10) on the heap A [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

```
A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6,2,1]
1 - A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6,2,1,-inf]
2 - A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6,2,1,10]
    2.1 A = [15, 13, 9, 5, 12, 10, 7, 4, 0, 6,2,1,8]
    2.2 A = [15, 13, 10, 5, 12, 9, 7, 4, 0, 6,2,1,8]

```

here is another gif to notice $INSERT(A,10)$ operations:

<p align='center'>
    <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/priorityqueue_insert.gif?raw=true" alt='alt text'>
</p>



---


### 6.5-3
#### Write pseudocode for the procedures HEAP-MINIMUM, HEAP-EXTRACT-MIN,HEAP-DECREASE-KEY, and MIN-HEAP-INSERT that implement a min-priority queue with a min-heap.


- Below is implementation of Min-Heap-Priority-Queue:

[Check Implemetation Min Heap Priority Queue](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/PriorityQueue_MinHeap.py)

<br>

```python
Min-Heapify(A,i)
    l = Left(i)
    r = l+1
    if l <= A.heap-size and A[l]<A[i]
        mini = l
    else 
        mini = i
    if r <= A.heap-size and A[r]<A[mini]
        mini = r
    if mini != i 
        swap(A[i],A[mini])
        Min-Heapify(A,mini)
```

```py
Heap-Minimum(A)
    if A.heap-size!=0
        return A[1]
```
```py
Heap-Extract-Min(A)
    if A.heap-size<1
        error 'heap under flow'
    Min = A[1]
    A[1] = A[A.heap-size]
    A.heap-size-=1
    Min-Heapify(A,1)
    return Min
```
```py
Heap-Decrease-Key(A,i,key)
    if A[i]<key
        error 'new key is bigger than current key'
    A[i] = key
    while i>1 and A[i]<A[Parent(i)]:
        exchange(A[i],A[Parent(i)])
        i = Parent(i)
```
```py
Heap-Insert(A,key)
    A.heap-size+=1
    A[A.heap-size]= float('inf')
    Heap-Decrease-Key(A,A.heap-size,key)
```

---

<br>

### 6.5-6
#### Each exchange operation on line 5 of HEAP-INCREASE-KEY typically requires three assignments. Show how to use the idea of the inner loop of INSERTION SORT to reduce the three assignments down to just one assignment.

```py
insertion_sort(A,n)
for i = 2 to n
    key = A[i]
    j = i - 1
    while j>0 and A[j]>key
        A[j+1] = A[j]
        j -=1
    A[j+1] = key

```

```py
Heap-Increase-Key(A,i,key)
    if A[i]>key
        error 'new key is smaller than current key'
    A[i] = key
    while i>1 and A[i]>A[Parent(i)]:
        # the three assignments:
        temp = A[i]
        A[i] = A[Parent(i)]
        A[Parent(i)] = temp

        i = Parent(i)
```
- Using the idea of insertion sort:

```py
Heap-Increase-Key(A,i,key)
    if A[i]>key
        error 'new key is smaller than current key'
    A[i] = key
    while i>1 and key>A[Parent(i)]:
        # just one line:
        A[i] = A[Parent(i)]

        i = Parent(i)
    A[i] = key
```


<br>

---

<br>

### 6.5-7
#### Show how to implement a first-in, first-out queue with a priority queue. Show how to implement a stack with a priority queue.

```
we can use some mapping to map the items pushed in and popped out and the 
priority would do all operations on the mapping items.

```

#### `Check Implementations`:

- [Stack (First input First output)](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/PriorityQueue_Stack.py)
- [Queue (First input Last output)](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/PriorityQueue_FIFO_Queue.py)

<br>

---

<br>

### 6.5-8
#### The operation HEAP-DELETE(A,i) deletes the item in node i from heap A. Givean implementation of HEAP-DELETE that runs in $O(lgn)$ time for an n-element max-heap.

>assuming working in max-heap:

```py
Heap-Delete(A,i)

    Heap-Increase-Key(A,i,float('inf'))
    A[1] = A[A.heap-size]
    A.heap-size-=1
    Max-Heapify(A,1)

```

- Running time is $\color{green}{O(lgn)}$.



<br>

---

<br>

### 6.5-9
#### Give an $O(nlgk)$ time algorithm to merge k sorted lists into one sorted list, where n is the total number of elements in all the input lists. (Hint: Use a min-heap for k-way merging).

- [Check Implementation](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/PriorityQueue_merge_K_lists.py)

<br>

```
We always using a min-heap created from all beginning numbers of all k lists.
that would make our heap doing min-heap property in O(lgk) time.
and we easily can retreive minimum element which would be in top.
we do that for all n numbers making algorithm run in O(nlgk) time.
```


---