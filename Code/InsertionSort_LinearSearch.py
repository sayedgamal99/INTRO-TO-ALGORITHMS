A = [3,32,5,65,76,8,99,999,1]
def linear_s(A:list,v:int):
    for i in range(len(A)):
        if A[i] == v:
            return i
print(linear_s(A,99))