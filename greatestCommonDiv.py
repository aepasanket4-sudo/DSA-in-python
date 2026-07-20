#!Simple GCD Code : - 

'''def Greatest_Common_div(a,b):
    fn = []
    fm = []
    for i in range(1,a+1):
        if a%i==0:
            fn.append(i)
    for j in range(1,b+1):
        if b%j==0:
            fm.append(j)
    CommonFact = []
    for k in fn:
        if k in fm:
            CommonFact.append(k)
    print(CommonFact[-1])
            
m = int(input('Enter the number: '))
n = int(input('Enter the number: '))

Greatest_Common_div(m,n)'''

#!NAive GCD : - 

#Even better

'''def gcd(m,n):
    cf = []
    for i in range(1,min(m,n)+1):
        if   (m%i)==0 and (n%i)==0:
            cf.append(i)
    
    print(cf[-1])
m = int(input('Enter the number: '))
n = int(input('Enter the number: '))

gcd(m,n)'''

# Without USing a list 

'''def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            mrcf = i
    
    print(mrcf)
m = int(input('Enter the number: '))
n = int(input('Enter the number: '))

gcd(m,n)'''


# Scanning Backwards

def gcd(m,n):
    i = min(m,n)
    while i > 0:
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i = i - 1
m = int(input('Enter the number: '))
n = int(input('Enter the number: '))

gcd(m,n)

#! Euclid's GCD : -
