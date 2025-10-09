
import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)

a=0
nom=[]
k=0
for i in range(20):
    q=l[a]
    d=q%2
    if d!=0:
        nom.append(q)
        k=k+q
    a+=1
avr=k/len(nom)
print(avr)