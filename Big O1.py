import sys
n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.read().split()))

god_list = list(set(a_list))
great_list = sorted(god_list)

print(great_list[-2])
   