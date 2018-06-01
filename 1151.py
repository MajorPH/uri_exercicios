n = int(input())
a, b = 0, 1
for k in range(0, n-1):
    print("%d " % a, end='')
    a, b = b, a + b
print(a)
