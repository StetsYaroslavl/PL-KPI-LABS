a1 = int(input("Введіть число: "))
a = a1
l = []
b = 10
while b // a != 0:
    c1 = b // a
    c = b // c1
    a = a - c
    if c // 2 : 
        l.append(c)
    b *= 10
print("l ", l)