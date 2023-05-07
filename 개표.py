
n = int(input())

nn = input()

lists = list(nn)

totalCount = 0

for list in lists:
    if list == 'A':
        totalCount += 1
    elif list == 'B':
        totalCount -= 1

if totalCount > 0:
    print('A')
elif totalCount < 0:
    print('B')
else:
    print('Tie')
    

