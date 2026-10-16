import sys

a,b,c,d = map(int, sys.stdin.read().split())

ab = a * 10 +b
ba = b *10 + a
cd= c * 10 + d
dc =d * 10 + c
#Другий спосіб
ad = a * 10 + d
da = d * 10 +a
bc = b * 10 +c
cb = c * 10 + b
#Третій спосіб
ac = a * 10 + c 
ca = c * 10 + a
bd = b * 10 + d
db = d * 10 + b


if (ab >= 10 and cd >= 10 and ab % 2 == 0 and cd % 2 == 0) or (ba >= 10 and dc >= 10 and ba % 2 == 0 and dc % 2 == 0):
    print("YES")

elif (ad  >= 10 and bc >= 10 and ad % 2 == 0 and bc % 2 == 0 ) or (da >= 10 and cb >= 10 and da %2 == 0 and cb % 2 == 0):
    print("YES")

elif (ac  >= 10 and bd >= 10 and ac % 2 == 0 and bd % 2 == 0 ) or (ca >= 10 and db >= 10 and ca %2 == 0 and db % 2 == 0):
    print("YES")

else:
    print("NO")