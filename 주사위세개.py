A,B,C = map(int, input().split(" "))
money = 0

# 셋다 같은경우
if A == B and B == C and A == C:
    money = int(10000) + (int(A)* int(1000))
# 0과 1이 같은 경우    
if A == B and B != C and A != C:
    money = int(1000) + (int(A)  * int(100))

# 1과 2가 같은 경우    
if B == C and A != C and A != B:
    money = int(1000) + (int(B) * int(100))

# 0과 2가 같은 경우    
if A == C and A != B and B!=C:
    money = int(1000) + (int(C)  * int(100))

# 셋다 다를 경우
if A != B and B != C and A!= C:
    list = [A,B,C]
    list.sort(reverse=True)
    money = int(list[0]) * (100)

print(money)