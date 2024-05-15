from collections import deque


class EdmondsKarp:
    def __init__(self, graph):
        """
        Initializes the EdmondsKarp instance with a graph.

        As parameter it takes graph (list of list of int).
        """
        self.graph = graph
        self.ROW = len(graph)

    def bfs(self, s, t, parent):
        """
        Performs a Breadth-First Search (BFS) to find an augmenting path.

        Returns True if there is an augmenting path from source to sink, False otherwise.
        """
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
        """
        Computes the maximum flow from source to sink using the Edmonds-Karp algorithm.

        Returns the maximum flow from source to sink.
        """
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
