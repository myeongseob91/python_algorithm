n = input()
list = list(n)
totalScore = 10

for index, value in enumerate(list):
    if index ==0:
        continue
    
    if list[index] != list[index-1]:
        totalScore += 10
    else:
        totalScore += 5

print(totalScore)