nums = [5,9,1,2,4,15,6,3]
'''target = 13
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+ nums[j] == target:
                print(i,j)
                break'''

n = len(nums)
hashmap = {}
target = 13
for i in range(0,n):
    remaining = target - nums[i]
    if remaining in hashmap:
        print(hashmap[remaining],i)
    hashmap[nums[i]] = i

