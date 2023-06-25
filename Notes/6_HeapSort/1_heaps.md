# Chapter 6 : Heap Sort

## 1- Heaps: 

<br>

- Heap data structure object we can see as $\color{white}\text{complete binary tree}$

<br>

<p align="center">
  <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/max_heap.png?raw=true" alt="alt text">
</p>


## indexing:


$$
Parent(i) = \big\lfloor {i/2}\big\rfloor \space | \space \newline
Left(i) = 2i \space \rightarrow \text{left child of (i)} \space | \space \newline
Right(i) = 2i+1 \space \rightarrow \text{right child of (i)}
$$

> $i/2$ can be calculated by shifting $\color{white}\text{binary representation}$ of i by one position to the $\color{white}\text{right}$.

> $2i$ also reached out by shifting i to $\color{white}\text{left}$ one position.


### Max-Heap
- This is a heap in which : the value of the nood is at most the value of it's parent. 
$$A[parnet(i)]>=A[i].$$

### Min-Heap
$$A[parnet(i)]<=A[i].$$

