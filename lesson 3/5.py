
import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)

m=min(l)
a=0
nom=[]
for i in range(20):
    q=l[a]
    if q==m:
        nom.append(q)
    a+=1
print(nom)