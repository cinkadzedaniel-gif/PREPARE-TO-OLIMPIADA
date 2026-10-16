n = int(input("Введіть число:"))

max_digit = 0
temp = n

while temp > 0:
    digit = temp % 10

    if digit > max_digit:
        max_digit = digit

    temp = temp // 10

print(max_digit)