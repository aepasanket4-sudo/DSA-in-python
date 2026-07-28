# Q. m ke elements n me kitni baar arhe hai

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

# worstcase
'''for num in m:
    count = 0
    for x in n:
        if x == num:
            count+=1
    print(count)'''
    
'''hash_list = [0]*11

for num in n:
    hash_list[num]+=1  

for num in m:
    if num<1 or num > 10:
        print(0)
    else:
        print(hash_list[num])'''
        
'''freq_dic = {}
for i in range(0,len(n)):
    freq_dic[n[i]] = freq_dic.get(n[i],0)+1
for i in range(0,len(m)):
    if m[i] in freq_dic:
        print(freq_dic[m[i]])
    else:
        print(0)
        '''
        
