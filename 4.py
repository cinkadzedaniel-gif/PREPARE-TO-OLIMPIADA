import sys
a,b, c, d = map(int, sys.stdin.read().split())

ab = a *10 + b
ba = b * 10 + a
cd = c * 10 + d
dc = d *10 + c
ad = a * 10 + d
da = d * 10 + a 
bc = b * 10 + c
cb = c * 10 + b


if (ab >= 10 and cd >= 10) or (ba >= 10 and dc >= 10)  or (ad >= 10 and bc >= 10) or (da >= 10 and cb >= 10):
    print("YES")

else:
    print("NO")
