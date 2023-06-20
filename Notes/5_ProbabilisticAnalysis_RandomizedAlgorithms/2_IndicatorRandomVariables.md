# Chapter Five : Probabilistic Analysis and Randomized Algorithms

## Part two : Indicator Random Varivable

<br>

- Indicator random variables provide a convenient method for
    converting between probabilities and expectations.

- sample
    space $S$ and an event $A$. Then the indicator random variable $I\{A\}$ associated with
    event A is defined as

$$
\mathrm{I}\{A\} =\begin{cases}
        1 & \text{if it occurs} \\
        0 & \text{if it doesn't occurs} 
\end{cases}
$$

- The expected value of an indicator random variable
  associated with an event A is equal to the probability that A occurs

$$\text{let }X_A = I\{A\}\\
\text{Then } E[X_A] = P\{A\} \rightarrow (1)$$


- simple example : we let $X_i$ be the indicator
    random variable associated with the event in which the $i^{th}$ flip comes up heads:
    $X_i = I\{\text{the ith flip results in the event Hg\}}$. Let $X$ be the random variable denoting
    the total number of heads in the n coin flips, so that

$$X = \sum\limits_{i=1}^{n} X_i\\
\text{we take the expectation both sides produce: }E[X] = E\left[\sum\limits_{i=1}^{n} X_i \right]\\
\text{and due to linearity of expectation:  } E[X] = \sum\limits_{i=1}^{n}E[X_i ]\\
\text{with eq(1) : }E[X] = \sum\limits_{i=1}^{n}{1\over2}\\
={n\over2}$$

> which would be the same result if we apply the expectation by definition.

<br>

### Analysis of hiring problem using indicator random variable
---

- Let $X_i$ is the indicator random variable which indicates if we hire this candidate or not.. assuming candidates come in random order.

> $E[X_i] = P\{\text{candidate i is hired}\}$ which would be $1/i$

$$X = \sum\limits_{i=1}^{n} X_i\\
E[X] = \sum\limits_{i=1}^{n}E[X_i ]\\
E[X] = \sum\limits_{i=1}^{n}{1\over i}\\
={ln(n) + O(1)}$$

- Which mean that we actually hire $ln(n)$ of candidates on average
    - returning to total cost of HIRE-ASSISTANT it would be $O(ln(n)\times C_h)$
    - when the worst-case was $O(n\times C_h)$



---
