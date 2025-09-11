def bfsOfGraph(n, edges, src):
    adj = [[] for _ in range(n)]
    
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False]*n
    q = deque()
    bfs = []

    q.append(src)
    visited[src] = True

    while len(q) > 0:
        val = q.popleft()
        bfs.append(val)

        for neighbour in adj[val]:
            if visited[neighbour] == False:
                q.append(neighbour)
                visited[neighbour] = True
    
    return bfs
