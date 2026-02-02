p=[7,1,5,3,6,4]
b=p[0]
pf=0
for i in range(1,len(p)):
    if b<p[i]:
        pf=max(pf,(p[i]-b))
    if b>p[i]:
        b=p[i] 
print(pf)          