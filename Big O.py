import sys
n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.read().split()))

count = 0

for i in range (1,n):

    if a_list[1] > a_list[i-1]:
        count += 1

print(count)