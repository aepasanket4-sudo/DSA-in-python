# bruteforce solution
num = [55,32,97,-55,45,32,88,21,97]
'''num.sort()   
print(num[-2])'''

# SC = O(n log n)
# TC = O(1)

# Better solution 
'''largest = float("-inf")
Slargest = float("-inf")

for i in range(0,len(num)):
    largest = max(largest,num[i])

for j in range(0,len(num)):
    if Slargest < num[j] < largest:
        Slargest = num[j]
        
print(Slargest)'''

# TC = O(2N) ~ O(N)
# SC = O(1)

# optimal solution
def SlargestEleArray(num):
    largest = float("-inf")
    Slargest = float("-inf")
    for i in range(0,len(num)):
        if num[i]>largest:
            Slargest = largest 
            largest = num[i]
        elif largest != num[i] and num[i] > Slargest:
            Slargest = num[i]
    return Slargest
        
print(SlargestEleArray(num))

# TC = O(N)
# SC = O(1)

