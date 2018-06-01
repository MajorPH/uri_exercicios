d = 0
n = int(input())
for i in range(0, n):
    x = int(input())
    if x in range(10, 21):
        d += 1
print("%d in\n%d out" %(d, n-d))
