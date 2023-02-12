# Chapter Two Exercises :
### 2- Analysing Algorithms :


- 2.2-1\
    Express the function ${n^3\over1000 }-100n^2-100n+3$ in terms of ‚ theta - notation.

    
    - we can rewrite it as :${1\over1000}*n^3 - 100 * n ^2 - 100*n +3$\
    reduced to $\theta(n^3)$\.

---
- 2.2-2\
    Consider sorting n numbers stored in array A by first finding the smallest element
    of A and exchanging it with the element in A[1]. Then find the second smallest
    element of A, and exchange it with A[2]. Continue in this manner for the first n-1
    elements of A. Write pseudocode for this algorithm, which is known as selection
    sort. What loop invariant does this algorithm maintain? Why does it need to run
    for only the first n-1 elements, rather than for all n elements? Give the best-case
    and worst-case running times of selection sort in theta - notation.

    - The pseduocode for this approch :
        ```
        A = [99,3,6,1,3]
        themin = A[1]
        for current = 1 to A.length-1           
            for i = current to A.length
                if A[i]< themin
                swap themin and A[i]
            A[current]=themin
        ```
        it needs to run for only n-1 because last item will be the smallest one among remaining items(itself)
        worst case would be $\theta(n^2)$
        best case if it sorted already would be $\theta(n)$.



---
    
- 2.2-3\
    Consider linear search again (see Exercise 2.1-3). How many elements of the input sequence need to be checked on the average, assuming that the element being
    searched for is equally likely to be any element in the array? How about in the
    worst case? What are the average-case and worst-case running times of linear
    search in theta notation? Justify your answers.
        
    - on average half of n ( where n equal to A.length ) will be checked.
    - worst case $\theta(n)$
    - best case $\theta(1)$
    - average case $\theta(n)$
---
- 2.2-4\
    How can you modify any sorting algorithm to have a good best-case running time?

    - i would try to reduce unnesessary nested loops 
    and check for answers during running if it currect it don't need to continue.
