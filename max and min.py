k = int(input())

min, max = map(int, input().split())


count = (max  // k) - ((max - 1) // k)

print(count)