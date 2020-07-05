def func():
    import sys
    x = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    y = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    z = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    a = abs(x[0] - y[0]) ** 2 + abs(x[1] - y[1]) ** 2
    b = abs(z[0] - y[0]) ** 2 + abs(z[1] - y[1]) ** 2
    c = abs(z[0] - x[0]) ** 2 + abs(z[1] - x[1]) ** 2
    if a > b:
        if a > c:
            if a == b + c:
                return "ALMOST"
    # s = [a, b, c]
    # m = max(s)
    # s.remove(m)
    # n = sum(s)
    # if m == n:
    #     return "ALMOST"
    # elif m < n:
