# Appendix A Exercises:
## A1:
-----
1. A1
    - A1-1 :
        - Simple formula for $$\sum_{k=1}^n {(2k -1)}$$
        $$=  2\sum_{k=1}^n {k} -  \sum_{k=1}^n {1}$$
        $$= 2* n{(n+1)\ \over2} - n$$
        $$=n^2.$$
    - A1-2:
        - show that $$\sum_{k=1}^n {1 \ \over {(2k - 1)}} = ln(\sqrt{n} +O(1))$$
        demonator has a seq of 1 3 5 7 .. n and summation = $${1 \ \over1} +{1 \ \over3}+ {1 \ \over5} + ..+ {1 \ \over2n-1}$$
        which we can say = O(1) + half of terms when it was $${1 \ \over1} +{1 \ \over2}+ {1 \ \over3} + ..+ {1 \ \over n}$$
        $$= O(1) + 1/2 (ln(n)) = O(1) + ln \sqrt n$$
    - A1-3:
         
        - show that $$\sum_{k=0}^∞ k^2 x^k = {x(x+1) \ \over (1-x)^3 }$$ for 0<|x|<1\
        we know that 

        $$\sum_{k=0}^{∞} kx^k  =  {x  \ \over (1-x)^2 }$$ 
        if we differentiating both sides and multiply by x we get\
        $$\sum_{k=0}^{∞} k^2 x^k  =  {x(1*(1-x)^2 + x(2(1-x)))  \ \over (1-x)^4 }$$
        $$= {x(1+x)  \ \over (1-x)^3 }$$

    - A1-4:
        
        - show that $$\sum_{k=0}^∞ (k-1)/2^k = 0$$
        we can rewrite it as:\
        $$\sum_{k=0}^∞ k{1\ \over 2^k} - \sum_{k=0}^∞ {1\ \over 2^k}$$
        $$\sum_{k=0}^∞ k({1\ \over 2})^k - \sum_{k=0}^∞ ({1\ \over 2})^k$$
        and the $$\sum_{k=0}^{∞} x^k  =  {1  \ \over (1-x) }$$ for |x| < 1\
        and the $$\sum_{k=0}^{∞} kx^k  =  {x  \ \over (1-x)^2 }$$ \ for |x| < 1
        then we treat x as 1/2 get : \
        $${(1/2)  \ \over (1-(1/2))^2 } -  {1  \ \over (1-(1/2)) } = 2-2 =$$
        


