# Chapter Three Exercises: Asymptotic Notations


- 3.1 :
    - Let f(n) and g(n) be asymptotically nonnegative functions. Using the basic definition of ‚theta-notation, prove that max(f(n),g(n))=theta(f(n)+g(n))

```f(n)<=f(n)+g(n)``` and  ```g(n)<=f(n)+g(n)```,
then
$$\max(g(n),f(n)) = O(g(n)+f(n))$$
```0.5(f(n)+g(n))<=max(g(n)+f(n))```
$$\max(g(n),f(n)) = \Omega(g(n)+f(n))$$
then from theorem 3.1:
$$\max(g(n),f(n)) = \Theta(g(n)+f(n))$$


----

- 3.2:

    Show that for any real constants a and b, where b>0,\
    $(n+a)^b = \Theta(n^b)$:\
    
        - Left hand side produce b terms, and the highest order of them would be Constant*n^b.
        by reducing the terms to highest order and ignoring the constant it will be.
---

- 3.3:

    Explain why the statement, “The running time of algorithm A is at least O(n) is
    meaningless?

    The "big-oh" represent $\color{green} upper bound$
    for the running time.. or we can say sometimes it represent worst-case: Clearly it can't has any higher running time.
---
- 3.4:

    is 

$$2^{n+1} = O(2^n)? \ \ \  2^{2n}= O(2^n)?$$

The First one is True.
$$2^{n} \times 2 =O(2^n)$$
The Second is not True.
$$2^{n} \times 2^{n} \neq O(2^n)$$
    
---
- 3.7\
    Prove that O(g(n)) intersection w(g(n)) is the empty set.

since we seen that o(g(n)) is $\color{lightgreen}upper bound$
to g(n) excluded cg(n)=o((g(n))),\
$\lim_{n=inf} {f(g)\over g(n)} = 0$\
and we seen that $\omega$(g(n)) is $\color{lightgreen}lower bound$\
to g(n) excluded cg(n)=$\omega$((g(n))),\
$\lim_{n=inf} {f(g)\over g(n)} = inf$\
we can write above as:
$$C_1g(n) < f(n) <C_1g(n).$$
which has no solution leeds to $\color{lightblue}Empty Set$
then 
$$o(g(n)) \bigcap \omega(g(n)) is\  \emptyset.$$


---

- 3.8: give definitions for omega(n) and theta(n):

$$
\Omega(g(n,m))=[f(n,m):there\ exist\ positve\ constants\ C_1,\ after\ n_0\ and\ m_0\ such\ that\
0\leq C_1g(n,m) \leq f(n,m)]
$$

$$
\Theta(g(n,m))=[f(n,m):there\ exist\ positve\ constants\ C_1,C_2\ after\ n_0\ and\ m_0\ such\ that\
0\leq C_1g(n,m) \leq f(n,m)\leq C_2g(n,m)]
$$

>i replaced {} with [].

---
