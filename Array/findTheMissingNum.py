num = [0,1,7,4,5,2,6,8,9]
'''n = len(num)
for i in range(0,n):
    if i not in num:
        print(i)
        num.append(i)'''
        
# better solution
'''n = len(num)
freq = {}

for i in range(0,n+1):
    freq[i] = 0

for nums in num:
    freq[nums] = 1
    
for k,v in freq.items():
    if v == 0:
        print(k)'''
        
# optimal solution

n = len(num)

print(int((n*(n+1)/2)-sum(num)))