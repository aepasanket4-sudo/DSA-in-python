def bsearch(seq,v,l,r):
    if (r - l == 0):
        return(False)
    mid = (l+r)//2
    
    if(v == seq[mid]):
        return(True)
    
    if(v < seq[mid]):
        return(bsearch(seq,v,l,mid))
    
    else:
        return(bsearch(seq,v,mid+1,r))
    
    
st = [1, 3, 5, 7, 9, 11, 13]
start = 0
end = len(st)-1
    
value = 11
bsearch(st,value,start,end)