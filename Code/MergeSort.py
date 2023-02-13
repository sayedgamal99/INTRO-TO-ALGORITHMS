def Merge(A,p,q,r):
    n1 = q-p
    n2 = r -q
    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = A[i]
    for j in range(n2):
        R[j] = A[j+q]
    i = 0
    j = 0
    for k in range(r):
        if i == n1:
            ii = k
            while ii <r and j<n2:
                A[ii] = R[j]
                j+=1
            break
        if j == n2:
            ii =k
            while ii<r and i<n1 :
                A[ii] = L[i]
                i+=1
            break
        if L[i]<=R[j]:
            A[k]=L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1
    return (A)

print(Merge([1,2,3,55,5,12,33,66],0,4,8))