import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

cub = (n - 2) * (m - 2)
mega = (n * m) - cub

print(mega)
