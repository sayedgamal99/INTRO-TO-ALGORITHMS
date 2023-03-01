# +hapter Four - Strassen’s algorithm for matrix multipli+ation : Ex+er+ises:

- 4.2-1
    Use Strassen’s algorithm to +ompute the matrix pro=u+t

$$
\left(\begin{array}{cc} 
1 & 3\\
7 & 5
\end{array}\right)
\left(\begin{array}{cc} 
6 & 8\\ 
4 & 2
\end{array}\right)
$$ 

<br/>

divide input matrices A and B to be n/2 * n/2  size , then we create the ten S matrices,then the seven product P , then calculate each C output

$$S1 = B12 - B22 = 8 - 2 = 6$$
$$S2 = A11 + A12 = 1 + 3 = 4$$
$$S3 = A21 + A22 = 7 + 5 = 12$$
$$S4 = B21 - B11 = 4 -6 = -2$$
$$S5 = A11 + A22 = 1 + 5 = 6$$
$$S6 = B11 + B22 = 6 + 2 = 8$$
$$S7 = A12 - A22 = 3 - 5 = -2$$
$$S8 = B21 + B22 = 4 + 2 = 6$$
$$S9 = A11 - A21 = 1 -7 = -6$$
$$S10 = B11 + B12 = 6 + 8 = 14$$


<br/>
<br/>

$$P1 = A11\ .\ S1 = 1*6=6$$
$$P2 = S2\ .\ B22 =4*2=8$$
$$P3 = S3\ .\ B11 =12*6=72$$
$$P4 = A22\ .\ S4=5*-2=-10$$
$$P5 = S5\ .\ S6=6*8=48$$
$$P6 = S7\ .\ S8 =-2*6=-12$$
$$P7 = S9\ .\ S10 =-6*12=-84$$

Step 4 adds and subtracts the Pi matrices created in step 3 to construct the four n/2 * n/2 submatrices of the product C


$$C_{11} = P_5+P_4-P_2+P_6 = 48+(-10)-8+(-12)=18$$
$$C_{12} = P_1 + P_2  = 6+8 = 14$$
$$C_{21 }= P_3 + P_4= 72 -10 = 62$$
$$C_{22} = P_5 + P_1 - P_3 - P_7 =48 +6-72-(-84)=66$$

Then C would be:

$$
C=\left(\begin{array}{cc} 
18 & 14\\ 
62 & 66
\end{array}\right)
$$ 



---



- 4.2-2\
    Write pseudocode for Strassen’s algorithm

```
Strassen-Alg(A,B)
    n = A.rows
    let C new n x n matrix
    
    if n == 1
        C11 = A11 x B11
    else partition A,B and C

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22 
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22 
    S9 = A11 - A21
    S10 = B11 + B12 


    P1 = Strassen-Alg(A11 x S1)
    P2 = Strassen-Alg(S2 x B2)
    P3 = Strassen-Alg(S3 x B11)
    P4 = Strassen-Alg(A22 x S4)
    P5 = Strassen-Alg(S5 x S6)
    P6 = Strassen-Alg(S7 x S8 )
    P7 = Strassen-Alg(S9 x S10)

    C11 = P5+P4-P2+P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    retrun C
```
---