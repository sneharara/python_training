n=[2,2,1,1,1,2,2]
d={}
for v in n:
    if v in d:
        d[v]+1
    else:
        d[v]=1    
for key in d:
    if d[key]>len(n)//2:
       print(key)
