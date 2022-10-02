#DFS


graph = {
      '5':['3','7'],
      '3':['2','4'],
      '7':['8'],
      '2':[],
      '4':['8'],
      '8':[]
     }
visited = set() #set to keep track of visted node graph
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("Depth first search")
dfs(visited,graph,'5')
