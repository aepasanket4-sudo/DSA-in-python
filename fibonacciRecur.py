'''n = 5
n1,n2 = 0,1

while n!=0:
    next = n1+n2
    n1 = n2
    n2 = next
    n-=1
    print(n1,end=" ")'''
    
def fibo(n):
    if n == 0 or n ==1:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(6))