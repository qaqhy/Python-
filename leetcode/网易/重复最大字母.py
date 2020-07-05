import sys
s = sys.stdin.readline().strip()
d = {}
for i in enumerate(s):
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1
n = max(d.values())
print(len(s)-2*n)
