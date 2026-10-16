import sys
n, m, k = map(int, sys.stdin.readline().split())

if k >= n + m:
    print("YES")
else:
    print("NO")