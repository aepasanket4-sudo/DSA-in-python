arr = [1,1,1,2,2,3,3,4,5,5,6,9,9,10]
# bruteforce solution 

'''def RemoveDuplicate(arr):
    dash = {}
    for i in range(0,len(arr)):
        dash[arr[i]] = 0

    j = 0
    for k in dash:
        arr[j] = k
        j+=1
        
    return j
print(RemoveDuplicate(arr))'''
def RemoveDuplicate(arr):
    n = len(arr)
    i = 0
    j = i+1

    while j < n :
        if arr[j] != arr[i]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1
    return i+1
print(RemoveDuplicate(arr))