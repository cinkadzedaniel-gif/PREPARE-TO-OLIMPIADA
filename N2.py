n = int(input())

count = 0
temp = n

while temp > 0:
    digit = temp % 10

    if digit > 5:
        count += 1

    temp = temp // 10

print(count)

