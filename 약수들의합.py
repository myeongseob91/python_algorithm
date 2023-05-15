while True:
    s = int(input())
    if s == -1:
        break

    
    #s = int(input())
    lists = []
    for i in range(s):
        if i == 0:
            continue
        
        if int(s%i) == 0:
            lists.append(i)
        
    sum_lists = sum(lists)

    if sum_lists != s:
        print(str(s) + ' is NOT perfect.')
    else:
        nSum = ''
        for index in range(len(lists)):
            if len(lists)-1 != index:
                nSum = nSum + str(lists[index]) + ' + '
            else:
                nSum = nSum + str(lists[index])

        print(str(s) + ' = ' + str(nSum))




