def thislist(nums):
    new_list=[]
    for i in nums:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(thislist([1,1,2,3,3,3,4,5]))