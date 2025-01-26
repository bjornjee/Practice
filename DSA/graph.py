from typing import List, Tuple
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
class UndirectedGraph:
    def __init__(self, n: int, edges: List[Tuple[int]], weights: List[int]):
        self.adj = defaultdict(list)
        for i in range(n):
            self.adj[i] = []
        self.weights = {}
        for idx in range(len(edges)):
            i,j = edges[idx]
            # non-directed graph
            self.adj[i].append(j)
            self.adj[j].append(i)
            self.weights[(i,j)] = weights[idx]
            self.weights[(j,i)] = weights[idx]
    def __str__(self):
        return str(self.adj)
    
class DirectedGraph:
    def __init__(self, n: int, edges: List[Tuple[int]], weights: List[int]):
        self.adj = defaultdict(list)
        for i in range(n):
            self.adj[i] = []
        self.weights = {}
        self.edges=edges
        self.size=n
        for idx in range(len(edges)):
            i,j = edges[idx]
            # non-directed graph
            self.adj[i].append((j))
            self.weights[(i,j)] = weights[idx]
    def __str__(self):
        return str(self.adj)
    

def bfs(g: DirectedGraph, v: int):
    visited = set()
    q = deque([v])
    visited.add(v)
    while len(q) > 0:
        curr = q.popleft()
        print(curr)
        for n in g.adj[curr]:
            if n not in visited:
                q.append(n)
                visited.add(n)


def dfs(g: DirectedGraph, v: int):
    visited = set()
    q = [v]
    visited.add(v)
    while len(q) > 0:
        curr = q.pop()
        print(curr)
        for n in g.adj[curr]:
            if n not in visited:
                q.append(n)
                visited.add(n)

def toposort(g: DirectedGraph):
    indegree = defaultdict(int)
    for i in g.adj:
        for n in g.adj[i]:
            indegree[n] += 1
    q = deque([])
    for i in g.adj:
        if indegree[i] == 0:
            q.append(i)
    while len(q) > 0:
        curr = q.popleft()
        print(curr)
        for n,_ in g.adj[curr]:
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)

def has_cycles(g: DirectedGraph)->bool:
    # method 1:
    # use toposort, if len(output) < len(graph) then there is a cycle

    # method 2:
    # dfs and keep track of visited node within a pass, if points to ancestor, has cycle
    l=len(g.adj)
    vis=[False]*l
    in_stack=[False]*l
    def dfs(v):
        vis[v]=True
        in_stack[v]=True
        for n in g.adj[v]:
            if not vis[n]:
                if dfs(n):
                    return True
            elif in_stack[n]:
                return True
        in_stack[v]=False
        return False
    for i in range(l):
        if not vis[i]:
            if dfs(i):
                return True
    return False

def dijkstra(g: DirectedGraph, s:int):
    vis = set()
    h = []
    d= {}
    inf = 1<<63-1
    for v in g.adj:
        if v == s:
            h.append((0,v))
            d[v] = 0
        else:
            d[v] = inf
    while len(h)>0:
        _,v = heappop(h)
        vis.add(v)
        for w in g.adj[v]:
            if w not in vis:
                dist = g.weights[(v,w)] + d[v]
                if dist < d[w]:
                    d[w] = dist
                    heappush(h, (dist,w))
    return d


# minimum spanning tree
def prims(g: DirectedGraph):
    edges = []
    h=[(g.weights[i],*i) for i in g.weights]    
    heapify(h)
    vis =set()
    while len(vis)<len(g.adj):
        _,v,u = heappop(h)
        vis.add(v)
        vis.add(u)
        edges.append((v,u))
    return edges

# strongly connected components
def kosaraju(g: DirectedGraph):
    def _dfs(g:DirectedGraph, v:int, vis:set, p_stack:List[int]):
        vis.add(v)
        for n in g.adj[v]:
            if n not in vis:
                _dfs(g,n,vis,p_stack)
        p_stack.append(v)
        
    # step 1: dfs to get priority stack
    priority_stack = []
    vis=set()
    for i in range(len(g.adj)):
        if i not in vis:
            _dfs(g,i,vis,priority_stack)
    # step 2:reverse graph
    g_rev = DirectedGraph(g.size,[[j,i] for i,j in g.edges],[1]*len(g.edges))
    # step 3: dfs on reversed graph
    scc=[]
    vis = set()
    while priority_stack:
        v = priority_stack.pop()
        if v in vis:
            continue
        curr_scc=[]
        _dfs(g_rev,v,vis,curr_scc)
        scc.append(curr_scc)
    return scc

if __name__ == '__main__':
    g = DirectedGraph(6,[[0,1],[0,2],[1,2],[1,3],[1,4],[2,4],[2,5],[4,3],[4,5]], [1,4,1,1,7,3,1,2,10])
    g_cycle = DirectedGraph(6,[[0,1],[0,2],[1,2],[1,3],[1,4],[2,4],[4,3],[4,5],[5,0]], [1,4,1,1,7,3,1,2,1])

    #bfs(g,0)
    #dfs(g,0)
    #toposort(g)
    #d = dijkstra(g,0)
    #print(d)
    #print(prims(g))
    #print(dict(g_cycle.adj))
    #print(has_cycles(g_cycle))
    print(kosaraju(g_cycle))