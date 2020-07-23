graph={ 0:[1,2], 1:[5,4], 2:[5,6], 3:[5,7], 4:[1,3,5], 5:[4], 6:[2,3],7:[2]}
visited=[]
def bfs(graph,start):
#     visited= []
     queue = [start]
     while queue:
         vertex = queue.pop(0)
         if vertex not in visited:
             visited.append(vertex)
             queue.extend(graph[vertex])
     return visited

bfs(graph, 0)
print(visited)




