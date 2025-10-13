def dfsOfGraph(n, edges):
    adj = [[] for _ in range(n)]
    visited = [False] * n
    lst = []

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node):
        if visited[node] == True:
            return 
        else:
            visited[node] = True
            lst.append(node)
        for neigh in adj[node]:
            dfs(neigh)
            
    for i in range(n):
        if visited[i] == False:
            dfs(i)
    
    return lst
