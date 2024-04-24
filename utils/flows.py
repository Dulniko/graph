from collections import deque


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def dfs(self, s, t, parent):
        visited = [False] * self.ROW
        stack = [s]

        while stack:
            u = stack.pop()

            if not visited[u]:
                visited[u] = True
                for ind, val in enumerate(self.graph[u]):
                    if not visited[ind] and val > 0:
                        stack.append(ind)
                        parent[ind] = u

        return visited[t]

    def ford_fulkerson_dfs(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.dfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()

            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


vertex_indices = {"s": 0, "x": 1, "y": 2, "u": 3, "w": 4, "e": 5, "t": 6}

graph = [
    [0, 20, 50, 0, 0, 0, 0],
    [0, 0, 10, 50, 0, 0, 0],
    [0, 0, 0, 0, 30, 0, 0],
    [0, 0, 0, 0, 0, 80, 40],
    [0, 0, 0, 60, 0, 0, 20],
    [0, 0, 0, 0, 0, 0, 40],
    [0, 0, 0, 0, 0, 0, 0],
]

g = Graph(graph)

source = vertex_indices["s"]
sink = vertex_indices["t"]

op = int(input("1. Ford-Fulkerson\n2. Edmonds-Karp\n"))

if op == 1:
    print("Max Flow (Ford-Fulkerson):", g.ford_fulkerson_dfs(source, sink))
else:
    print("Max Flow (Edmonds-Karp):", g.edmonds_karp(source, sink))
