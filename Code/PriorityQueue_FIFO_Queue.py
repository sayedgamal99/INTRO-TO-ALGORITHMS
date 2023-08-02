"""
This is implementation for Queue First in First ouput using priority queue
with mapping values.
you can sea changes to priority queue as comments showing below.
"""

class Queue:
    def __init__(self):
        self.heap_size = 0
        self.minheap = [0]*10000
        self.map = {}
        self.maxi = 0

    def Min_Heapify(self,i):
        l = 2*i +1
        r = l+1
        mini = i
        if l <= self.heap_size and self.minheap[l]<self.minheap[i]:
            mini = l
        if r <= self.heap_size and self.minheap[r]<self.minheap[mini]:
            mini = r
        if mini != i:
            self.minheap[i],self.minheap[mini] = self.minheap[mini],self.minheap[i]
            self.Min_Heapify(mini)


    def Heap_Minimum(self):
        return self.map[self.minheap[0]] if self.heap_size!=0 else None


    def Heap_Extract_Min(self):
        if self.heap_size<1:
            print('heap under flow')
            return None
        Min = self.map[self.minheap[0]]     #mapping lines
        self.minheap[0] = self.minheap[self.heap_size-1]
        self.heap_size-=1
        if self.heap_size==0:self.maxi = 0      #mapping lines
        self.Min_Heapify(0)
        return Min


    def Heap_Decrease_Key(self,i,key):
        if self.minheap[i]<key:
            print('new key is bigger than current key')
            return None
        self.minheap[i] = key
        while i>0 and self.minheap[i]<self.minheap[((i-1)//2)]:
            self.minheap[i],self.minheap[((i-1)//2)] = self.minheap[((i-1)//2)],self.minheap[i]
            i = ((i-1)//2)


    def Heap_Insert(self,key):
        self.heap_size+=1
        self.minheap[self.heap_size-1]= float('inf')
        self.maxi+=1    #mapping lines
        self.map[self.maxi]=key     #mapping lines
        self.Heap_Decrease_Key(self.heap_size-1,self.maxi)


Q = Queue()
k = int(input())
while(k):
    k-=1
    op = input().strip().split()
    if op[0] == 'push':
        Q.Heap_Insert(int(op[1]))
    if op[0] == 'pop':
        mini = Q.Heap_Extract_Min()
        # if mini is not None :print(mini)
    if op[0] == 'top':
        mi = Q.Heap_Minimum()
        if mi is not None : print(mi)
        else : print("Empty Queue")
    
