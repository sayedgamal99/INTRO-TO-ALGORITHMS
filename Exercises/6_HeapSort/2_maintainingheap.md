# Chapter 6 : Exercises 
## Part two : maintaining heap property:


<br>

### 6.2-1
#### Using Figure 6.2 as a model, illustrate the operation of MAX-HEAPIFY A(A,3) on the array  $A[27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]$


```
# using max-heapify pseudocode the following happens in it:
max-heapify(A,3)
largest = 6
swap(A[6],A[3])
max-heapify(A,6)
largest = 12
largest = 13
swap(A[6],A[13])
max-heapify(A,13)
```


### The operations on A:

- 1- $A[27, 17, 10, 16, 13, 3, 1, 5, 7, 12, 4, 8, 9, 0]$
- 2- $A[27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]$


---

### 6.2-2
#### Starting with the procedure MAX-HEAPIFY, write pseudocode for the procedure MIN-HEAPIFY(A,i), which performs the corresponding manipulation on a min-heap. How does the running time of MIN-HEAPIFY compare to that of MAXHEAPIFY?

<br>


```
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
- Running time of Min-Heapify(A,i) as same as Max-Heapify is $\color{white}T(n) = O(lgn)$

---

### 6.2-3

#### What is the effect of calling MAX-HEAPIFY(A,i) when the element A[i] is larger than its children?

- This result no changes 


---

### 6.2-4

#### What is the effect of calling MAX-HEAPIFY(A,i) for i > A.heap-size/2?

- This results no changes since A[A.heap-size/2] is leaf node .. has no children to calc Left,Right.


---

### 6.2-5
#### Write an efficient MAX-HEAPIFY that uses an iterative control construct (a loop) instead of recursion.

```
Max-Heapify(A,i)
    while i <= A.heap-size/2
        l = Left(i)        
        r = Right(i)    
        i = largest    
        if l <= A.heap-size and A[l]>A[i]
            largest = l
        if r <= A.heap-size and A[r]>A[largest]
            largest = r
        if largest != i
            swap(A[i],A[largest])
        else 
            return A
```

---