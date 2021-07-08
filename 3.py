def mult(nums):
    total=1
    for i in nums:
        total*=i
    return total
print(mult([8,2,3,-1,7]))