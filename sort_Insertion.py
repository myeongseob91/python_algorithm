
list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(list)):
    # 첫번째 원소는 건너뜀
    if i == 0:
        continue
    
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            list[j] , list[j-1] = list[j-1], list[j]
        else:
            break
print(list)

        
        


