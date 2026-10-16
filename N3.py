n = int(input())

count = 0 
temp = n 

while temp > 0:
    digit = temp % 10

    if digit % 2 == 1:
        count += digit

    temp = temp // 10

print(count)