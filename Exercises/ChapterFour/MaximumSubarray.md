# Chapter Four - Devide and Conquer: Excercises:

- 4.1-1:
    What does FIND-MAXIMUM-SUBARRAY return when all elements of A are negative?

    ```
    it will return largest element in the array since all are negative no sense of computing sum on it.!
    ```

---

- 4.1-2:
    Write pseudocode for the brute-force method of solving the maximum-subarray
    problem. Your procedure should run in ‚$\Theta(n^2)$ time

    ```
    Brute(A):
        max_sum=A[1]
        L,R = 1,1 #indicating to the indices of max-subarray.
        for i = 1 to A.length
            sum = 0
            j = i +1
            while j<=A.length
                sum+=A[j]
                if sum > max_sum
                    max_sum=sum
                    L=i
                    R=j
            j+=1

        return(L,R,max_sum)
    ```