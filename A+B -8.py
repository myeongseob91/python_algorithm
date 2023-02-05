# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
# Case #3: 3 + 4 = 7
# Case #4: 9 + 8 = 17
# Case #5: 5 + 2 = 7

loopCount = int(input())

for i in range(loopCount):
    a,b = map(int, input().split())
    str = 'Case #{ii}: {c} + {d} = {e}'
    print(str.format(ii=i+1,c=a,d=b,e=a+b))