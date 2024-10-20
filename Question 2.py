def subarray_or(A):
    or_set = set()
    current = {0}
    
    for num in A:
        current = {num | x for x in current} | {num}
        or_set |= current
    
    return max(or_set)


A1 = [1, 4, 6]
A2 = [10, 100, 1000]

print("The OR of all subarrays for A1 is:", subarray_or(A1)) 
print("The OR of all subarrays for A2 is:", subarray_or(A2))  
