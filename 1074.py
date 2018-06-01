n = int(input())
for i in range(0, n):
    x = int(input())
    if x == 0:
        print("NULL")
    elif x%2 == 0:
        if x > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif x > 0:
        print("ODD POSITIVE")
    else:
        print("ODD NEGATIVE")
