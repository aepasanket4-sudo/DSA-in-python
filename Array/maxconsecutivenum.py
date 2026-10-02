nums = [1,1,0,0,0,1,1,1,1,0,1,0]

n = len(nums)
c = 0
max_count = 0
for i in range(0,n):
    if nums[i]==1:
        c+=1
    else:
        max_count = max(max_count,c)
        c = 0
print(max(max_count,c))

# Time Complecity = O(n)
  