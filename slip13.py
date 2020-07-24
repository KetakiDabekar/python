graph={ 0:[1,2], 1:[5,4], 2:[5,6], 3:[5,7], 4:[1,3,5], 5:[4], 6:[2,3],7:[2]}

visited = []

def dfs(graph,node):
#    global visited
     if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)
            
dfs(graph,0)
print(visited)
