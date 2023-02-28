def Linear_maximumSubArray(nums):
    maxsumever =-999999
    sum=0
    l,r = 0,0
    current_l = 0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum >maxsumever:
            maxsumever = sum
            left = current_l
            right = i
        if sum<0:
            sum =0
            current_l = i+1


        
    return (left,right,maxsumever)



A = [int(x) for x in input().split()]
print(Linear_maximumSubArray(A))