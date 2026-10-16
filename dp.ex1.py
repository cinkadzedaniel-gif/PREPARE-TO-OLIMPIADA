n = int(input())
odn = list(map(int,input().split()))
bog = list(map(int, input().split()))

sum=0

for i in range(1, n + 1 ):
    if odn[i] < bog[i]:
        sum +=i
        
    elif bog[i] < odn[i]:
        sum +=i
        break
    
print(sum)
        