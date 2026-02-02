#using range function as iterable 
r=range(10)
r=iter(r)
while True:
   try:
    d=next(r)
    print(d)
   except StopIteration as e:
      break 