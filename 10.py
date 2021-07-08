def thislist(nums):
    new_list=[]
    for i in nums:
        if i%2==0:
            new_list.append(i)
    return new_list
print(thislist([1,2,3,4,5,6,7,8]))
        