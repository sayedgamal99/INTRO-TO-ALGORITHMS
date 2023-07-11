
def max_heapify(A,heapsize,i):
    left = 2*i+1
    right = left+1
    largest = i
    if left<heapsize and A[left]>A[i]:
        largest = left
    if right<heapsize and A[right]>A[largest]:
        largest = right
    if largest!= i :
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,heapsize,largest)
    

def Build_maxHeap(A):
    heapsize = len(A)
    for i in range(len(A)//2-1,-1,-1):
        max_heapify(A,heapsize,i)

def Heap_Sort(A):
    Build_maxHeap(A)
    for i in range(len(A)-1,-1,-1):
        A[0],A[i] = A[i],A[0]
        max_heapify(A,i,0)
    return A



print(Heap_Sort([16,4,453,345,76,23,1,9,-87,5,34]))