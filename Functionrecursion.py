# sum of 1 to n [parameterized]

'''def func(sum,i,n):
    if i >n:
        print(sum)
        return
    func(sum+i,i+1,n)
    
func(0,1,4)'''

# sum of 1 to n [functional]
# create a flow
# create the base condition


'''def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

print(func(5))'''


# Factorial of n number

'''def func(n):
    if n == 1 or n == 0:
        return 1
    return n * func(n-1)

print(func(5))'''


# reverse an array using recursion

'''def func(nums,left,right):
    if left >= right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    func(nums,left+1,right-1)

nums =[5,9,8,3,6,7,1,4,2]
func(nums,2,6)

print(nums)'''

# TC = n/2 = O(n)

# using while loop

'''def revArray(nums,l,r):
    while l != r or l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    return nums

nums =[5,9,8,3,6,7,1,4,2]

revArray(nums,2,6)

print(nums)'''