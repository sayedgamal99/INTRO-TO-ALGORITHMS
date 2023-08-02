"""
This is implementation for Stack First in Last ouput using priority queue
with mapping values.
you can sea changes to priority queue as comments showing below.
"""


class Queue:
    def __init__(self):
        self.heap_size = 0
        self.heap = [0] * 10000001
        self.map = {}   #mapping lines
        self.maxi = 0   #mapping lines

    def max_heapify(self, i):
        left = (2 * i )+ 1
        right = left + 1

        largest = i
        if (left < self.heap_size) and (self.heap[i] < self.heap[left]):
            largest = left
        if (right < self.heap_size) and (self.heap[largest] < self.heap[right]):
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def Heap_maximum(self):
        return self.map[self.heap[0]]

    def Heap_Extract_max(self):
        # max_val = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        if self.heap_size==0:self.maxi=0

    def Heap_Insert(self, key):
        self.heap_size += 1
        self.maxi+=1    # mapping lines
        self.map[self.maxi]=key     #mapping lines
        self.heap[self.heap_size - 1] = self.maxi   
        i = self.heap_size-1
        while (i > 0) and (self.maxi > self.heap[(i - 1) // 2]):
            self.heap[i] = self.heap[(i-1)//2]
            i = (i - 1) // 2
        self.heap[i] = self.maxi


# =========================================================

Q = Queue()
k = int(input())

while k:
    k -= 1

    operation = input().strip().split()
    # print(operation)


    if operation[0] == 'push':
        Q.Heap_Insert(int(operation[-1]))

    elif operation[0] == 'pop':
        if Q.heap_size == 0:
            print("IT IS JUST EMPTY")
        else:
            Q.Heap_Extract_max()

    elif operation[0] == 'top':
        if Q.heap_size==0:
            print("IT IS JUST EMPTY")
        else:
            print(Q.Heap_maximum())
        


