# Chapter 6 : Exercises

## Part two : maintaining heap property:

<br>

### 6.3-1

- Using Figure 6.3 as a model, illustrate the operation of BUILD-MAX-HEAP on the array $A[5, 3, 17, 10, 84, 19, 6, 22, 9]$.

```
1 - A[5, 3, 17, 22, 84, 19, 6, 10, 9]
2 - A[5, 3, 19, 22, 84, 17, 6, 10, 9]
3 - A[5, 84, 19, 22, 3, 17, 6, 10, 9]
4 - A[84, 5, 19, 22, 3, 17, 6, 10, 9]
5 - A[84, 22, 19, 5, 3, 17, 6, 10, 9]
5 - A[84, 22, 19, 10, 3, 17, 6, 5, 9]
```

- Gif explaining what happenning:

<p align="center">
  <img src="https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/buildmaxheap.gif?raw=true" alt="alt text">
</p>

---

### 6.3-2

- Why do we want the loop index i in line 2 of BUILD-MAX-HEAP to decrease from n//2 to 1 rather than increase from 1 to n//2?
  - up-bottom appraoch wouldn't satisfy heap property. Ex: A[2,1,1,3]

---
