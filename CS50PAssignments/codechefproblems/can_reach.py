for _ in range(int(input(""))):
    x, y, k = input("").split(" ")
    x = int(x)
    y = int(y)
    k = int(k)

    if x % k == 0 and y % k == 0:
        print("YES")
    else:
        print("NO")
