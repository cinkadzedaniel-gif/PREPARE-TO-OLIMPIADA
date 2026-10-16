masv = list(map(int, input().split()))

masv.sort()

rizn = masv[-1] - masv[0]

print(rizn)