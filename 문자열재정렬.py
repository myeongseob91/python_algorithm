input = input()
result = []
digitSum = 0

for x in input:
    if x.isalpha():
        result.append(x)
    else:
        digitSum += int(x)

result.sort()

if digitSum != 0:
    result.append(str(digitSum))

print(''.join(result))



# input1 = 'K1KA5CB7'
# input2 = 'ADDIJJJKKLSS20'




# list = list(input1)


# sorted_list = sorted(list, key=lambda x: (not x.isdigit(), x))
# print(sorted_list)

