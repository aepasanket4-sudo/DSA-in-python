s = "azyuyyzaaaa"
q = ["d","a","y","u"]

hash_list = [0]*26

for ch in s:
    ascii_val = ord(ch)
    idx = ascii_val -97
    hash_list[idx]+=1
for ch in q:
    ascii_val = ord(ch)
    idx = ascii_val -97
    print(hash_list[idx])