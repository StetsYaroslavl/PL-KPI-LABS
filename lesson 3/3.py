
import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)
a=20
for i in range(20):
    q=l[a]
    if q>100:
        l.remove(q)
        l.append(100)
    a-=1
print(l)
