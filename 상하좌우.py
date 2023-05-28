# 5
# R R R U D D
# 3 4
###########
rows = int(input())
input2 = input().split(" ")

dx = []
dy = []

outputX = 1
outputY = 1

for input in input2:

    if input == 'R':
        dx.append(0)
        dy.append(1)
    elif input == 'L':
        dx.append(0)
        dy.append(-1)
    elif input == 'U':
        dx.append(-1)
        dy.append(0)
    elif input == 'D':
        dx.append(1)
        dy.append(0)

for i in range(len(input2)):
    xx = outputX + dx[i]
    yy = outputY + dy[i]

    if xx < 1 or yy < 1 or xx > rows or yy > rows:
        continue

    outputX, outputY = xx, yy
    
print(outputX, outputY)




