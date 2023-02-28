import time,random,math
def BruteForce(nums):
        max_sum = nums[0]
        left = 0
        right = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum>=max_sum:
                    max_sum = sum
                    left = i
                    right = j
        return(left,right,max_sum)

def Find_maxSubArray(low,high,A):
    if high == low+1:
        return (low,low,A[low])
    else:
        mid = (low+high)//2

    leftlow,lefthigh,leftsum=Find_maxSubArray(low,mid,A)
    rightlow,righthigh,rightsum=Find_maxSubArray(mid,high,A)
    crosslow,crosshigh,crosssum=Find_crossing_maxSum(low,mid,high,A)
    if leftsum>= rightsum and leftsum>=crosssum:
        return (leftlow,lefthigh,leftsum)
    elif rightsum>= leftsum and rightsum>=crosssum:
        return (rightlow,righthigh,rightsum)
    else:
        return (crosslow,crosshigh,crosssum)


def Find_crossing_maxSum(low,mid,high,A):
    leftsum = -math.inf
    maxleft,maxright=0,len(A)-1
    summ = 0
    for i in reversed(range(low,mid)):
        summ +=A[i]
        if summ>leftsum:
            leftsum=summ
            maxleft=i
    rightsum = -math.inf
    summ = 0
    for j in range(mid,high):
        summ+=A[j]
        if summ>rightsum:
            rightsum=summ
            maxright=j
    return(maxleft,maxright,(leftsum+rightsum))
    
def maxSubArray(nums) -> int:
    return((Find_maxSubArray(0,len(nums),nums)[2]))

for input_size in range(2,100):
    arr = [random.randint(-100,100) for _ in range(input_size)]
    start = time.time()

    for _ in range(20):
        bf = BruteForce(arr)
    bf_time = time.time() - start

    start = time.time()
    for _ in range(20):
        rc = maxSubArray(arr)
    rc_time = time.time() - start
  
    if bf_time > rc_time:
        print(f"Cross over point = {input_size}")
        break
