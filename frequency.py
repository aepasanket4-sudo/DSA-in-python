nums = [5,6,7,7,1,9,111,1,1,5,1,1]

'''Freq_map = {}
for i in range(0,len(nums)):
    if nums[i] in Freq_map:
        Freq_map[nums[i]] += 1
    else:
            Freq_map[nums[i]]=1
            
print(Freq_map)'''


# method 2 
hashmap = {}
n = len(nums)
for i in range(0,n):
    hashmap[nums[i]] = hashmap.get(nums[i],0)+1
print(hashmap)