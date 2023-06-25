
from bisect import bisect, bisect_left


#list = [1,2,3,4,4,4,5,6,7,8,8,9,10,11,12] # 3
#list = [1,2,3,5,6,7,8,8,9,10,11,12] # 3
list = [5,4,7,8,9,0,1,2] # 3


print(bisect_left(list,6))