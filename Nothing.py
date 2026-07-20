lst1 = list(range(1,11))
# print(lst1)
lst2 = lst1

lst1 = lst2[1:5] + [1] +['hello']
# print(lst1)
# print(lst2)

# it is used to search the position and print it 
def findpos(l,v):
    (pos,i) = (-1,0)
    for x in l:
        if x == v:
            pos = i
            break
        i = i + 1
    print(pos)
    
findpos(lst1,9)
print(lst1)