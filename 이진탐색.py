## 이진탐색
## 이진탐색은 정렬이 되어있는 데이터를 기반으로 수행가능
## 4를 찾는 소스코드 작성

array = [0,2,4,6,8,10,12,14,16,18]
#array = [0,2,4,6,8,10,12,14,16]

def binary_search(array,target,start,end):
    mid = int((start + end) / 2)

    if target < array[mid]:
        binary_search(array,target,start,mid-1)
    elif target > array[mid]:
        binary_search(array,target,mid+1,end)
    else:
        print(f'index is {mid}')
    
 
binary_search(array,4,0,9)


