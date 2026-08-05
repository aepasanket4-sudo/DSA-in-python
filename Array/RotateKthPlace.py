nums = [-6,5,3,9,4,0,10,7]
k = 3
n = len(nums)
# rotation = n%k

# for i in range(0,rotation):
#     e = nums.pop()
#     nums.insert(0,e)
    
# print(nums)

# Better 

# nums[:] = nums[n-k:] + nums[:n-k]

# print(nums)

# Without Slicing :-

nums = [3,5,8,10,2,6,4,9]

def Rotate_kth(nums,left,right):
    while left< right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1
    return nums
n = len(nums)

Rotate_kth(nums,n-k,n-1)
Rotate_kth(nums,0,n-k-1)
print(Rotate_kth(nums,0,n-1))
