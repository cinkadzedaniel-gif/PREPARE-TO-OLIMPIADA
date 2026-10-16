import sys
x, y, z, w = map(int, sys.stdin.read().split())

s = x + y + z - w

print(s)