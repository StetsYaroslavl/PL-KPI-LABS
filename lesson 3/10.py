import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)

a1=0
nom1=[]
k=0
for i in range(20):
    q1=l[a1]
    d1=q1 %2
    if d1==0:
        nom1.append(q1)
        k=k+q1
    a1+=1
avr=k/len(nom1)

a=0
nom=[]
for i in range(20):
    q=l[a]
    if q==avr:
        nom.append(q)
    a+=1
print(len(nom))