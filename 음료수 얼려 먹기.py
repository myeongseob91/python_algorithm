n, m = map(int, input().split())

graph = []
visited = []
iceCount = 0

def dfs(graph, visited, i,j,same):
    #방문처리
    if visited[i][j] == False:
        visited[i][j] = True
    else:
        ## 이미 방문 했을경우
        return;

    if graph[i][j] == 0:
        if same != True:
            global iceCount
            iceCount  += 1 
        
        #상
        if 0 <= i-1 < n:
            dfs(graph,visited,i-1,j,True)
        #하
        if 0 <= i+1 < n:
            dfs(graph,visited,i+1,j,True)
        #좌
        if 0 <= j-1 < m:
            dfs(graph,visited,i,j-1,True)
        #우
        if 0 <= j+1 < m:
            dfs(graph,visited,i,j+1,True)
        
    
        

for i in range(n):
    aa = list(map(int, input()))
    graph.append(aa)
    visited.append([False] * len(aa))
    
for i in range(n):
    for j in range(len(graph[i])):
        ## 상하좌우 탐색
        dfs(graph,visited,i,j,False)

print(iceCount)

    
# 4 5
# 00110
# 00011
# 11111
# 00000

# -> 

# 3
# graph = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]

# for row in graph:
#     print('')
#     for column in row:
#         print(column, end=' ')



