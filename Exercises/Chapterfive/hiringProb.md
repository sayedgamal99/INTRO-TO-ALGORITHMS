# Chapter Five - Hiring Problem : Exercises:

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