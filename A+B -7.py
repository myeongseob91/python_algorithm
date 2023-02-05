# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

#배운것
#출력 포맷팅 % -> 정확한 형을 알아야 사용할수있다. 
#str.format 편하지만 긴문자열을 사용할때 장황하다
#python3.6 부터 f-string이 나왔다.

count = int(input());
a = []
for i in range(0, count):
    a.append(str(input()))

i = 1
for inputStr in a:
    A,B = map(int, inputStr.split(" "))
    print(str("Case #") + str(i) + str(": ") + str(A+B)); 
    i = i+1;



# Try1
# count = int(input());

# for i in range(0,count):
#     A,B = map(int , input().split(" "))
#     print(str("Case #") + str(i) + str(": ") + str(A+B));



# t = int(input())
# for x in range(1,t+1):
#     a,b = map(int, input().split())
#     print("Case #" + str(x) + ":",a+b)

# n = int(input())
# for x in range(n):
#     a, b = map(int, input().split())
#     print("Case #%d: %d" %(x+1, a+b))










