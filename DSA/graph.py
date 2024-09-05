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

if __name__ == '__main__':
    g = DirectedGraph(6,[[0,1],[0,2],[1,2],[1,3],[1,4],[2,4],[2,5],[4,3],[4,5]], [1,4,1,1,7,3,1,2,10])
#     0
#   1   2
# 3   4   5

    #bfs(g,0)
    #dfs(g,0)
    #toposort(g)
    #d = dijkstra(g,0)
    #print(d)
    print(prims(g))