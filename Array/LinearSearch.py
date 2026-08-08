nums = [55,32,-97,99,3,67]
def LinearSearch(nums,target):
    n = len(nums)
    
    for i in range(0,n):
        if nums[i] == target:
            return i
    return -1 

print(LinearSearch(nums,99))
    