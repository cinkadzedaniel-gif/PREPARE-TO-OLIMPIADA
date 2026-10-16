import sys
a, b, k = map(int, sys.stdin.readline().split())

if k >= a + b:
    print("YES")

else:
    print("NO")