# this is factorial using recusrion

def factorial(n):
    if n == 0:
        return(1)
    else:
        return(n*factorial(n-1))
    
print(factorial(7))

# multiplication using recusrion

def mul(m,n):
    if n == 1:
        return(m)
    else:
        return(m + mul(m,n-1))
    
print(mul(5,4))