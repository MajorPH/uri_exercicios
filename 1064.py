pos = 0
m = 0
for i in range(0, 6):
    x = float(input())
    if x > 0:
        pos += 1
        m += x
m = m/pos
print("%d valores positivos\n%.1f" %(pos, m))
