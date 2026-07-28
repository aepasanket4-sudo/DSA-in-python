'''def pali(s):
    n = len(s)
    l = 0
    r = n - 1
    while l < r :
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

s = 'nitin'

print(pali(s))'''

def pali(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return pali(s,left+1,right-1)

s = 'nayan'
print(pali(s,0,len(s)-1))