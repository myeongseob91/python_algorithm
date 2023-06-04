
list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(list)):
    #print('')
    maxValueIndex = i
    for j in range(i+1, len(list)):
        #print(j , end=' ')
        if list[maxValueIndex] < list[j]:
            maxValueIndex = j

    
    list[i] , list[maxValueIndex] = list[maxValueIndex], list[i]

print(list)
        



# print(list)



# for i in list:
#     maxValue = 0
#     if len(list) == i:
#         break;

#     for j in list:
#         j = j + i

#         if len(list) - 2 == j:
#             break;

#         if list[j] > list[maxValue]:
#             maxValue = j

#     maxValue = list[j]
#     list[i] = list[j]
#     list[j] = maxValue


# print('정렬 ' + list)


        
        


