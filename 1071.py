x = int(input())
y = int(input())

if x < y:
    p = x
    g = y
else:
    p = y
    g = x

n = 0

for i in range (p+1, g):
    if (i%2) == 1:
        n += i
print(n)
