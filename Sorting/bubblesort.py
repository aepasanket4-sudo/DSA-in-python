'''nums = [5,1,6,8,2,4,9]

n = len(nums)

for i in range (n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)'''

# Worst / Average case 
# Tc = n(n+1)/2 -> n**2
# SC = O(n)


# Now Best Case 

nums = [1, 2, 4, 5, 6, 8, 9]

n = len(nums)

for i in range(n - 2,-1,-1):
    is_swap: False
    for j in range(0,i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1],nums[j]
            is_swap = True
    if is_swap == False:
        break
    
# TC -> O(n)
# SC -> O(1)
