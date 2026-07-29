num = [1,2,3,4,5,6,7]
# num = [55,32,-97,99,3,67]
def checkSorted(num):
    for i in range(0,len(num)-1):
        if num[i] > num[i+1]:
            return False
        else:
            return True
        
print(checkSorted(num))

# TC = O(N)
# SC = O(1)

