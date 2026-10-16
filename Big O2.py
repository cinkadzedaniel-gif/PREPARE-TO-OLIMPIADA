n = int(input())
a_list = list(map(int, input().split()))

unique_list = set(a_list)
sorted_list = sorted(unique_list)

print(*sorted_list)