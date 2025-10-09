num = []
for i in range(1, 501):
    n = i
    a = n%12
    if a == 0:
        num.append(n)
print("Із чисел від 1 до 500 націло на 4 і 6 діляться: ", num)
