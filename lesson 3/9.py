import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)

a=20
nom=[]
for i in range(20):
    q=l[a]
    nom.append(q)
    a-=1
print(nom)