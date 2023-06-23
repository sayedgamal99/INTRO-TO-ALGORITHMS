# Chapter Five - Indicator Random Varibale : Excercises:


### 5.2-1
- In HIRE-ASSISTANT, assuming that the candidates are presented in a random order,   what is the probability that you hire exactly one time? What is the probability
  that you hire exactly n times?

```
Hiring one time must when best candidate come first..
```
$$\text{leaving }(n-1)! \text{ ordering for the rest of them}\\
P={(n-1)!\over (n)!} = {1\over n}$$

```
Hiring all of them must when them come in increasing order, and it would be exactly one order of the n! possible orders..
```
$$P={1\over n!}$$

---

<br>
<br>


### 5.1-2 
- Describe an implementation of the procedure RANDOM(a,b) that only makes calls to RANDOM(0,1).?

    - The idea is using binary representation to form numbers.
```
RANDOM(a,b)
  n = log_2(b)
  A = [1..n] #new list of length n
  while true
    for i = 0 to n
      A[i] = RANDOM(0,1)

    if A if a binary representation for a number which is between a and b
      return A
```

---