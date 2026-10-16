s = input()

a = 0 
b = 0

for sym in s :
    if sym == "A":
        a += 1
    if sym == "B":
        b += 1

print(f"{a}:{b}")