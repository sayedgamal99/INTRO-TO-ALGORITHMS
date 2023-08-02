import heapq as heap

def merge_k_sorted_lists(lists):
    H = []
    result = []
    for ind,list in enumerate(lists):
        if list:heap.heappush(H,(list[0],ind,0))
    while(H):
        val,ind,el_ind = heap.heappop(H)
        result.append(val)
        if el_ind+1 < len(lists[ind]): heap.heappush(H,(lists[ind][el_ind+1],ind,el_ind+1))
    return result



lists1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
result1 = merge_k_sorted_lists(lists1)
print(result1) 
