import sys


n, m = sys.stdin.readline().strip().split(' ')
n, m = int(n), int(m)
for _ in range(n):
    strs = sys.stdin.readline().strip()
    sn = len(strs)
    flag = ''
    fs = []
    for _ in range(m):
        for i, s in enumerate(strs):
            if s != flag:
                fs.append([i, i])
                flag = s
            else:
                fs[-1][1] = i+1
        for i in range(len(fs)-1, -1, -1):
            strs = strs[:fs[i][0]] + strs[fs[i][1]:]
        print(strs)