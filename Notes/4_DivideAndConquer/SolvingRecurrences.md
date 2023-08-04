# Chapter Four : Divide and conquer
## Solving Recurrences with 3 methods:
<br>

### Starting with substitution method :
- It has mainly two steps:
     1. Guess the solution for the recurrence
     2. prove it's true for this solution using **Mathematical inducaiton**

<br>

-   Way to make a good guess is to prove loose upper and lower bounds on
    the recurrence and then reduce the range of uncertainty. For example, we might
    start with a lower bound of T(n) = $\Omega(n)$ for the recurrence (4.19), since we
    have the term n in the recurrence, and we can prove an initial upper bound of
    T(n) = $O(n^2)$. Then, we can gradually lower the upper bound and raise the
    lower bound until we converge on the correct, asymptotically **tight** solution of
    $T(n) = \Theta(nlgn)$

> Recurrence 4.19:

$${T}(n) = 2T(\lfloor n/2 \rfloor) + n$$

<br>
<br>
<br>


#### We can also use Changing variables to ease the solution:

- As we can see some kind of difficult recurrence like :

$$T(n) = 2T(\sqrt n ) + lgn$$

assuming $n=2^m$ it't will blow up the whole recurrence to some easy kind of recurrences:

$$T(n) = 2T(2^{m/2}) + m$$
changing the whole story to be $S(m)$ instead of $T(2^m)$
$$S(m) = 2S(m/2) + m$$
## wow!

- now we know the exact solution for that recurrence, in other cases we can guess directly how the solution is!

    this is recurrence describes the **running time** of **merge sort** which runs in $O(mlgm)$

    we must rechange the varibles to it's original to be: *lgn instead of m*

    Resulting $O(lgn lg lgn)$.



### Conclusion :
    For this kind of methods to solve the recurrence and get the running time of recursive algorithm, we can use the substitution method above as 
    a quick way to solve wide range of recurrences, BUT we must care about it's failer of proving using math induction,

        IMPORTANT:
            use this method if you has a good background of recurrences and has seen alot of them before, else you maight guess more than once 
            wrong to reach good guess, Avoid this method if you worry about your math induction skills.


<br>
<br>
<br>
<br>

---











