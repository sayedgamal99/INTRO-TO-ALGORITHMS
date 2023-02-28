# Chapter Four - Divide and Conquer: Excercises:

- 4.1-1:
    What does FIND-MAXIMUM-SUBARRAY return when all elements of A are negative?

    ```
    it will return largest element in the array since all are negative no sense of computing sum on it.!
    ```

---

- 4.1-2:
    Write pseudocode for the brute-force method of solving the maximum-subarray
    problem. Your procedure should run in, $\Theta(n^2)$ time

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

----



- 4.1-3
    Implement both the brute-force and recursive algorithms for the maximumsubarray problem on your own computer. What problem size n0 gives the crossover
    point at which the recursive algorithm beats the brute-force algorithm? Then,
    change the base case of the recursive algorithm to use the brute-force algorithm
    whenever the problem size is less than n0. Does that change the crossover point?

- the brute-force take $\Theta(n^2)$ then for sure it will give 
    time limit excedded in all problems, any way the implementation here:


[Check Code](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/MaximumSubArray_Bruteforce.py)

*and for sure of working brute-force check the reason of failing this submission.*

[Check Leet Code Submission](https://leetcode.com/submissions/detail/906497741/)

<br/>
<br/>

- Recursive Solution take only $\Theta(nlgn)$


[Check Code](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/MaximumSubArray_recursion.py)


[Check Leet Code Submission](https://leetcode.com/problems/maximum-subarray/submissions/906571035/)

<br/>

### And for time comparing :


[see MaximumSubArray_timeComparing](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/MaximumSubArray_timeComparing.py)




---


- 4.1-4
    Suppose we change the definition of the maximum-subarray problem to allow the result to be an empty subarray, where the sum of the values of an empty subarray is 0.
    How would you change any of the algorithms that do not allow empty
    subarrays to permit an empty subarray to be the result?


        - it would be when all elements are negative elements
        - i would change the max-sum to be zero and if all are negative 
        we stay at our zero to be maximum and then the indices doesn't chanfge from our initialization.


---

- 4.1-5
    develop a nonrecursive, linear-time algorithm for the maximum-subarray problem.

```
This is wondurful Linear approch!
```



[see LinearApproach](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Code/MaximumSubArray_Linear.py)

---

### Some Results, LookUp for results and compare:

<br/>
<br/>



![alt text](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/leet1?raw=true)


<br/>
<br/>
<br/>
<br/>


![alt text](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/codeforces1?raw=true)