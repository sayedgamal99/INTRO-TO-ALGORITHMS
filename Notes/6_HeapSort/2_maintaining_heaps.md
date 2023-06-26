# Chapter 6 : Heap Sort

## 2 - Maintaining the heap property: 

<br>


<p align="center">
  <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/maintainingheapproperty.png?raw=true" alt="alt text">
</p>

- The following procedure maintain max-heap as above figure :

```
Max-Heapify(A,i)
    l = Left(i)         # recall that we get Left(i) by : Left(i) = 2i
    r = Right(i)        # Right(i) = 2i+1
    if l <= A.heap-size and A[l]>A[i]
        largest = l
    else 
        largest = i
    if r <= A.heap-size and A[r]>A[largest]
        largest = r
    if largest != i
        swap(A[i],A[largest])
        Max_Heapify(A,largest)
```


## Running time :

- The running time of above Max-Heapify is solved as :

$$\color{white}{T(n) = O(lgn) = O(h)}$$

---