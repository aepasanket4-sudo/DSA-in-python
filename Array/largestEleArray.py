# method 1 
'''nums = [55,32,-97,99,3,67]
def largestEleArray(nums):
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        largest = max(largest,nums[i])
    return largest

print(largestEleArray(nums))
'''

# method 2 

nums = [55,32,-97,99,3,67]
def largestEleArray(nums):
    largest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        largest = max(largest,nums[i])
    return largest

print(largestEleArray(nums))