# basic recursion
'''def fun(x,n):
    if n == 0:
        return
    print(x)
    fun(x,n-1)
    
fun(15,4)
'''
# 1 to n (head recursion)
# 1.work
# 2.fun call
'''def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,4)'''

# n to 1 (Tail recursion) or Backtracking
# 1.fun call
# 2.work

'''def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
func(1,4)'''

# n to 1 (head recursion)
# 1.work
# 2.fun call

'''def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)
    
fun(4)'''


# 1 to n (Tail recursion) or Backtracking
# 1.fun call
# 2.work
def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)
fun(4)