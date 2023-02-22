# Chapter 3 Exercises: Standard notation and Common Function

- 3.2-1
    Show that if f(n) and g(n) are monotonically increasing functions, then so are
    the functions f(n)+g(n) and f(g(n)) and if f(n) and g(n) are in addition
    nonnegative, then f(n).g(n) is monotonically increasing.
```
if there f and g are monotonically increasing:
    m <= n >>> f(m) <= f(n)
    m <= n >>> g(m) <= g(n)
then also 
    f(m) + g(m) <= f(n) + g(n)
then f(n)+g(n) is also monotonically increasing
and combining first two inequalities produce that:
    f(g(m)) <= f(g(n))
then also f(g(n)) is.
in case of f(n) and g(n) are nonnegative: multipling them give
    f(m).g(m) <= f(n).g(n)
finally with f(n).g(n) is Monotonically Increasing
```
---

- 3.2-2: Prove:
$$a^{log_b{c}} = c^{log_b{a}}$$
log both sides with base b gives:
$$log_b{a^{log_b{c}}} = log_b{c^{log_b{a}}}$$
$${log_b{c}}\times{log_b{a}} = {log_b{a}}\times{log_b{c}}$$
Give both sides to be *Equal*.

---

- 3.2-3: Prove:
$$lg(n!) = \Theta(nlgn)$$
using **Stirling’s approximation** and assume that $\Theta({1\over n})$ is small to be ignored in large values of n:
$$
lg(n!) \approx lg({\sqrt(2\pi n)}({n\over e})^n)\\
     = lg({\sqrt(2\pi n)})+n\times lg(({n\over e}))\\
     = lg({\sqrt(2\pi)})+0.5\times lg({n})+n\times lg({n})-nlg(e)\\
     =\Theta(1)+\Theta(lgn)+\Theta(nlg)-\Theta(n)
     =\Theta(nlgn)
$$
---

- 3.2-6:
Show that the golden ratio and its conjugate both satisfy the equation
$X^2 = X+1$

```
finding the solution of Quad equation given by :
```
$$X_{1,2} = {{-b\pm \sqrt {b^2 - 4\times a c}}\over 2a}$$
by solving the equation above gives the $\color{lightgreen}Golden Ratio $ and it's cong.

---

- 3.2-7:

Prove by induction that the ith Fibonacci number satisfies the equality
$$F_i = {{\alpha^i - \alpha'^i} \over \sqrt 5}$$
```
- first to determine base cases when f0 and f1 are equal to 0,1 respectively,

and assuming it's true for Fk
then by fi = fi-1 + fi-2 for each i > 1
and using previous ex during our proof
give:
```
$${{\alpha^k - \alpha'^k}\over \sqrt 5}+{{{\alpha^{k-1} - \alpha'^{k-1}}\over \sqrt 5}}\\
{{({\alpha^k +\alpha^{k-1}}) - ({\alpha'^k+\alpha'^{k-1}})}\over \sqrt 5}$$
$${{({\alpha^{k-1}})(\alpha +1 ) - ({\alpha'^{k-1}})}(\alpha'+1)\over \sqrt 5}$$
$${{({\alpha^{k-1}})(\alpha^2 ) - ({\alpha'^{k-1}})}(\alpha'^2)\over \sqrt 5}$$
$${{({\alpha^{k+1}}) - ({\alpha'^{k+1}})}\over \sqrt 5}$$

---

- 3.2-8
    Show that k*ln(k) = $\theta(n)$ implies k = $\theta(n/ln(n))$
```
we will use symmetry property of notation to reach it quickly:
```
$$k\times ln(k) = \theta(n)$$
$$n = \theta(k\times ln k)\rarr (1)$$
$$(1)$$
$$ln(n) = \theta(ln(k\times ln k))\rarr (2)$$
```
devide 1/2
and 2 can be rewritten as mul of log.then ignoring ln(ln) term:
```
$${n \over ln(n) }= \theta({{k\times ln k}\over lnk})$$
$${n \over ln(n) }= \theta(k)$$
```
using symmetry again:
```
$$k = \theta(n/ln(n))$$

---

