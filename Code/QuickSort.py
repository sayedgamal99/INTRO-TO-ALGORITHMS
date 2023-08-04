class Sort:
    def __init__(self,A,increasing = True):
        self.A = A
        self.increasing = increasing
    def QuickSort(self,p,r):
        if p<r:
            q = self.Partation(p,r)
            self.QuickSort(p,q)
            self.QuickSort(q+1,r)

    def Partation(self,p,r):
        x = self.A[r-1]
        i = p-1

        for j in range(p,r-1):
            if (self.A[j]<= x  if self.increasing else self.A[j] > x ):
                i+=1
                self.A[i],self.A[j] = self.A[j],self.A[i]
        self.A[i+1],self.A[r-1] = self.A[r-1],self.A[i+1]
        return i+1
    


A = [13,19,9,5,12,8,7,4,21,2,6,11]

print('\nAscending order')
Sort(A,increasing=True).QuickSort(0,len(A))
print(A)
print('='*42)
print('descending order')
Sort(A,increasing=False).QuickSort(0,len(A))
print(A)