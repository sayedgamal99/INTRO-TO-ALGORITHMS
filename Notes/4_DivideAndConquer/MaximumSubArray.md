# Chapter Four : Divide and conquer
## - Part one : Maximum Subarray problem


- divide and conquer paradigm:

        we solve a problem recursively, applying three steps at each level of the recursion

        Divide
            the problem into a number of subproblems that are smaller instances 
            of the same problem.
        Conquer 
            the subproblems by solving them recursively. If the subproblem sizes are
            small enough, however, just solve the subproblems in a straightforward manner.
        Combine
            the solutions to the subproblems into the solution for the original problem.



- In recurrences:

        if we call merge_sort on n elements, when n is odd number we end up with 
        subproblems of sizes (ceil(n/2) and floor(n/2))
        and the recurrence describe the worst-case of merge_sort is:

$$
\mathrm{T}(n) =\begin{cases}
        \Theta(1) & \text{if } n = 1\\
        T(\lceil{n/2}\rceil) + T({\lfloor{n/2}\rfloor}) + \Theta(n) & \text{if } n > 1
\end{cases}
$$

- Pseudocode for appling divide-and-conquer on Maximum SubArray problem:
-


```
Find-Max-Crossing-Subarray(A,low,mid,high)
    left_sum = -inf
    sum=0
    for i = mid downto low
        sum = sum + A[i]
        if sum > left_sum
            left_sum = sum
            max_left = i
    right_sum = -inf
    sum = 0
    for j = mid+1 to high
        sum = sum + A[j]
        if sum > right_sum
            right_sum = sum
            max_right = j
    return ( max_left , max_right , left_sum + right_sum )

```
> Notice that previos approch solve the crossing area of array and get the maximum sub-array
> and it's $\color{lightgreen}Running\ time\ is\ \Theta(n)$

```
Find-Maximum-Subarray(A, low , high)
    if high == low 
        return (low,high,A[low])    \\Base case: Only one element
    else
        mid = floor((low+high)/2)

    (left-low,left-high,left-sum)=
        Find-Maximum-Subarray(A,low,mid)
    (right-low,right-high,right-sum)=
        Find-Maximum-Subarray(A,mid+1,high)
    (cross-low,cross-high,cross-sum)=
        Find-Max-Crossing-SubArray(A,low,mid,high)

    if left-sum >= right-sum and left-sum >= cross-sum
        return(left-low,left-high,left-sum)
    elif right-sum >= left-sum and right-sum >= cross-sum
        return(right-low,right-high,right-sum)
    else
        return(cross-low,cross-high,cross-sum)
```
- Analyzing divide-and-conquer algorithm

$$T(n) = \Theta(1)\text{//for base case } + 2T(n/2)\text{//for both left subarray and right } + \Theta(n)\text{//for crossing maximum subarray} + \Theta(1)\text{//for return and control statements}$$

that we can reduce to : with assumption of n is power of 2,


$$
\mathrm{T}(n) =\begin{cases}
        \Theta(1) & \text{if } n = 1\\
        2T(n/2) + \Theta(n) & \text{if } n > 1
\end{cases}
$$

----