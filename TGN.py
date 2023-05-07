n = int(input())

for i in range(n):

    A,B,C = map(int, input().split(" "))
    
    if A + C > B:
        print('do not advertise')
    elif A + C < B:
        print('advertise')
    else:
        print('does not matter')
        
# advertise
# does not matter
# do not advertise
