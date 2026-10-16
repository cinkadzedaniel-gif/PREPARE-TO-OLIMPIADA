import sys

list = list(map(int, sys.stdin.readline().split()))

print("Список", list)
print("Сума елементів", sum(list) )
print("Максимальне число", max(list))