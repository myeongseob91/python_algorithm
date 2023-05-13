str = input()

if len(str) == 1:
    print('1')
else:
    aaa = int(len(str) / 2)

    aa = 0

    for i in range(aaa):
        if str[i] == str[(len(str))-(i+1)]:
            aa = 1
        elif str[i] != str[(len(str))-(i+1)]:
            aa = 0
            break

        

    print(aa)