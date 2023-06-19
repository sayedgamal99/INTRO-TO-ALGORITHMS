# Chapter Five : Probabilistic Analysis and Randomized Algorithms

## Part one : Hiring Problem

- 
  The cost model for this problem differs from the model described in Chapter 2, We focus not on the running time of HIRE-ASSISTANT, but instead on the costs incurred by interviewing and hiring.

```
HIRE-ASSISTANT(n)
    best = 0
    for i = 1 to n 
        interview candidate i   
        if candidate i is better than best candidate
            best = i
            hire candidate i    
```
> intreviewing candidate costs $C_i$ and hiring candidate consts $C_h$.
- $C_h >>> C_i$ and let $m$ is the number of hiring candidates then the total cost with this algorithm is:

$$\text{Total Cost is: }O(nC_i + mC_h)$$

### Worst Case :
- This happen when all candidates come in increasing order then we hire each new candidate (n) times

$$\text{Total hiring cost : } O(nC_h)$$

### Best Case :
- First Candidate is the BEST one, then we don't hire anyone after him.

$$\text{Total cost : } O(nC_i + C_h)$$


### Probabilistic Analysis 
- In order to perform a probabilistic analysis, we
  must use knowledge of, or make assumptions about, the $\color{lightblue}distribution$ of the inputs.

- In some problems, we cannot describe a reasonable input distribution, and in these cases we cannot use probabilistic analysis.

- For the hiring problem, we can assume that the applicants come in a random order. We assume that we can compare any two candidates and decide which one is better qualified; that is, there is a $\color{lightblue}Total Order$ on the candidates

- **Uniform random permutation** that is, each of the possible $n!$ permutations appears with equal probability.


---

