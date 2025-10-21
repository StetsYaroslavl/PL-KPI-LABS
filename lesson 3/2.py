#2. Порахувати кількість чисел, що діляться на 2 або 5.

import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)
a=0
nom=[]
for i in range(20):
    q=l[a]
    d=q%2*(q%5)
    if d==0:
        nom.append(q)
    a+=1
print(len(nom))
