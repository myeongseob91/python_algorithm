n = int(input())

for i in range(n):
    nn = int(input())
    uname = ""
    ucount = 0
    for j in range(nn):
        y,k = input().split(" ")
        
        if uname == "":
            uname = y
            ucount = k
        elif int(ucount) < int(k):
            uname = y
            ucount = k
    
    print(uname)


            

