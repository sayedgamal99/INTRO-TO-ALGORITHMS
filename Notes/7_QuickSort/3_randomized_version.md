# CH 7 : Quick Sort



### Quick Sort Algorithm : Randomized Version

```py
Randomized-Quick-Sort(A,p,r)
    if p<r
        q =  Randomized-Partation(A,p,r)
        Randomized-Quick-Sort(A,p,q-1)
        Randomized-Quick-Sort(A,q+1,r)
```
```py
Randomized-Partation(A,p,r)
    x = RANDOM(p,r)
    swap(A[x],A[r])
    return Paratation(A,p,r)
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
