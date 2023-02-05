
def sort_descinding():
    A = [31,41 ,59 ,26 ,41, 58]
    for i in range(1,6):
        key = A[i]
        j = i -1
        while j>=0 and A[j]<key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
    return A
print(sort_descinding())
