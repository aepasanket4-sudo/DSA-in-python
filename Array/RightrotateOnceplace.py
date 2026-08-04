nums = [-6,5,3,9,4,0,10,7]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp    
print(nums)