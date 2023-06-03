graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
#                  1    ,2    ,3     ,4    ,5    ,6    ,7    ,8
visited = [False,False,False,False,False,False,False,False,False]

def dfs(graph, v, visited):
    ##방문처리
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
        


dfs(graph,1,visited)

    
    


