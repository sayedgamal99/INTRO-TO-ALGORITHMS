# Chapter Three Notes:

- Once the input size n
    becomes large enough, merge sort, with its $\Theta(nlgn)$ worst-case running time,
    beats insertion sort, whose worst-case running time is $\Theta(n^2)$

- Asymptotic notation can also apply to
    functions that characterize some other aspect of algorithms (the amount of space
    they use, for example), or even to functions that have nothing whatsoever to do
    with algorithms

---



- We shall therefore assume that every
    function used within $\Theta$ -notation is asymptotically nonnegative.
    or any other asymptotic notations as well.

- We shall often
    use the notation $\Theta(1)$ to mean either a constant or a constant function with respect
    to some variable.

-  When we say “the running time is $O(n^2)$ ” Equivalently, we mean that the worst-case running time is $O(n^2)$

- When we say that the running time (no modifier) of an algorithm is $\Omega(g(n))$
    we mean that no matter what particular input of size n is chosen for each value
    of n, the running time on that input is $\color{gold}at\ least\ a\ constant\ times\ g(n)$
    we are giving a $\color{gold}lower\ bound$ on the best-case running time
    of an algorithm. For example, the best-case running time of insertion sort is $\Omega(n)$
    which implies that the running time of insertion sort is $\Omega(n)$ .

- there also $o(n)$ Upper bound notation: 
$$0\leq f(n)<cg(n)$$
which similer to *big oh* $O(n)$ as it's def as:
$$0\leq f(n)\leq cg(n)$$

-  in o-notation, the function f(n) becomes insignificant
    relative to g(n) as n approaches infinity:
$$\displaystyle \lim_{n \to \infty}{f(n)\over g(n)} = 0$$


> The small omega notation (w) is the same idea of (o) notation but it's lower bound

$$\displaystyle \lim_{n \to \infty}{f(n)\over g(n)} = \infty$$

---
## Asymptotic Notations imply some intersting properties:

- Transitivity:

$$f(n) = \Theta(g(n))\ and\ g(n) = \Theta(h(n))\ then\ f(n)=\Theta(h(n))$$
    and this properties valid for all Asymptotic notations.

- Symmetry:
$$f(n) = \Theta(g(n))\ if\ and\ only\ if\ g(n)=\Theta(f(n))$$

- Transpose Symmetry:
$$f(n) = O(g(n))\ if\ and\ only\ if\ g(n)=\Omega(f(n))$$


--- 


Because these properties hold for asymptotic notations, we can draw an analogy
between the asymptotic comparison of two functions f and g and the comparison
of two real numbers a and b:

$f(n) = O(g(n))$ is just like $a\leq b$

$f(n) = \Omega(g(n))$ is just like $a\geq b$

$f(n) = \Theta(g(n))$ is just like $a=b$

$f(n) = o(g(n))$ is just like $a<b$

$f(n) = w(g(n))$ is just like $a>b$




---

> the next figure illustrate the main definition for each of **"Big-oh"**,**"Theta"** and **"Big-Omega"** notations:


![alt text](https://github.com/sayedgamal99/INTRO-TO-ALGORITHMS/blob/main/Exercises/Images/ch3.png?raw=true)


---

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>



#  Standard notations and common functions


- for any integer n:

$$\lceil{n/2}\rceil + \lfloor{n/2}\rfloor = n$$

- The floor function f(x) $\lfloor{x}\rfloor$ is monotonically increasing, as is the ceiling function f(x) $\lceil{x}\rceil$.

for any real number x>=0 and integers a,b>0,

$$\lceil {\lceil{x/a}\rceil \over b} \rceil = \lceil {{x} \over ab} \rceil$$


---

$$a\ mod\ n = a - n\ \lfloor{a/n}\rfloor$$

- Each Fibonacci number is the sum of the two previous ones, yielding the
    sequence

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

$$F_i = {\alpha^i - \alpha'^i\over \sqrt 5}$$
and $\alpha$ is the golden ratio and it's conjugate driven from eq:
$$X^2 = X + 1$$

---