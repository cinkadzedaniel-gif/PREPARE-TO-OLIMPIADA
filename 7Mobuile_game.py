import sys

n = int(sys.stdin.readline())
zol = list(map(int, sys.stdin.read().split()))

max_coins = 0

for l in range(n):
    for r in range(l,n):
        zvich_atack = r-l+1

        max_coins = max(max_coins, zvich_atack)

    if all (x == 2 for x in zol[l:r +1]):
        super_atack = 2 * (r - l + 1)
        max_coins = max(max_coins, super_atack)


print(max_coins)