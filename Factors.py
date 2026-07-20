def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return factorlist
    

def IsPrime(n):
    return(factors(n)==[1,n])
    
   
# IsPrime(17) # it is return TRUE
# IsPrime(1) it will return FALSE

# this code is for upto which number we want prime number 
def PrimesUpto(n):
    Primelist = []
    for i in range(1,n+1):
        if IsPrime(i):
            Primelist = Primelist + [i]
    return(Primelist)
        
# PrimesUpto(50) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# This is for how many primenumber we want 
def nPrime(n):
    (count,i,plist) = (0,1,[])
    while(count<n):
        if IsPrime(i):
            (count,plist) = (count+1,plist+[i])
        i = i + 1
    print(plist)
    
# nPrime(10)# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]