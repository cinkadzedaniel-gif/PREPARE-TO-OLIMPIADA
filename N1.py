n = int(input())

sum = 0 
temp = n

while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        sum = sum + 1

    temp = temp // 10

print(sum)