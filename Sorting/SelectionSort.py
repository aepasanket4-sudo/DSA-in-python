def SelectionSort(nums):
    n = len(nums)
    for i in range(0,n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
        
nums = [5,3,6,7,4,2,8,1]
SelectionSort(nums)

print(nums)
    