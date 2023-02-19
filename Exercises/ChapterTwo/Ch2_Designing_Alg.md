# Chapter Two Exercises: Designing Algorithms


- 2.3-1:
    - Using Figure 2.4 as a model, illustrate the operation of merge sort on the array
    A{3, 41, 52, 26, 38, 57, 9, 49}

each step of the following is a *level* of <font color = 'green'>**merge sort**</font> from bottom to up
```
1- [3],[41],[52],[26],[38],[57],[9],[49]
2- [3,41],[26,52],[38,57],[9,49]
3- [3,26,41,52],[9,38,49,57]
4- [3,9,26,38,41,49,52,57]

```
---
- 2.3-2\
    Rewrite the MERGE procedure so that it does not use sentinels, instead stopping
    once either array L or R has had all its elements copied back to A and then copying
    the remainder of the other array back into A
```
Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r -q
    L[n1],R[n2]
    for i = 1 to n1:
        L[i] = A[p+i-1]
    for j=1 to n2:
        R[j] = A[q+j]
    i = 1
    j = 1
    for k = 1 to r:
        if i > n1:
            ii = k
            while ii <=r and j<=n2:
                A[ii] = R[j]
                j+=1
            break
        if j > n2:
            ii =k
            while ii<=r and i<=n1 :
                A[ii] = L[i]
                i+=1
            break
        if L[i]<=R[j]:
            A[k]=L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1

```
[Check Implementation](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/MergeSort.py)

---
- 2.3-5
    Referring back to the searching problem (see Exercise 2.1-3), observe that if the
    sequence A is sorted, we can check the midpoint of the sequence against v and
    eliminate half of the sequence from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion of the
    sequence each time. Write pseudocode, either iterative or recursive, for binary
    search. Argue that the worst-case running time of binary search is $\theta(lgn)$.
```
def LINSEA(A,V):
    n = len(A)
    l,r = 0,n-1
    while l <=r :
        mid = ((l+r)/2)
        if A[mid] == V:
            return mid
        else if A[mid]<V:
            l = mid +1
        else if A[mid]>V:
            r = mid-1
    return "Not Found"
```
---
<font color = 'green'>*Implementation* :</font>

[Check Code](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/BinarySearch.py)

---

