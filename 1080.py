y = 0
for i in range(1, 101):
    x = int(input())
    if x > y:
        y = x
        p = i
print("%d\n%d" %(y, p))
