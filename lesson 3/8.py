#8. Порахувати суму додатних чисел.

import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)

a=0
nom=0
for i in range(20):
    q=l[a]
    if q>0:
        nom+=q
    a+=1
print(nom)
