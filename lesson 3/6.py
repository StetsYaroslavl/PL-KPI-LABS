#6. Знайти другий за величиною елемент.

import random
l=[]
for i in range(20):
    l1=random.randint(-100, 200)
    l.append(l1)

k=l
a=0
while True:
    q=l[a]
    ma=max(k)
    if q==ma:
        k.remove(a)
d=max(k)
print(d)
