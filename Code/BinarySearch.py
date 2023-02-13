"""
This is Iterative method for Binary Search.
"""
def LINSEA(A,V):
    n = len(A)
    l,r = 0,n-1
    while l <=r :
        mid = int((l+r)/2)
        if A[mid] == V:
            return mid
        elif A[mid]<V:
            l = mid +1
        elif A[mid]>V:
            r = mid-1
    return "Not Found"
A= [1,2,3,55,2,34,55,-756,43]
A.sort()
print(LINSEA(A,3))