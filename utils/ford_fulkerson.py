class FordFulkerson:
    def __init__(self, graph):
        """
        Initializes the FordFulkerson instance with a graph.

        As parameter it takes graph (list of list of int).
        """
        self.graph = graph
        self.ROW = len(graph)

    def dfs(self, s, t, parent):
        """
        Performs a Depth-First Search (DFS) to find an augmenting path.

        Returns True if there is an augmenting path from source to sink, False otherwise.
        """
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

    def ford_fulkerson(self, source, sink):
        """
        Computes the maximum flow from source to sink using the Ford-Fulkerson algorithm.

        Returns the maximum flow from source to sink.
        """
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
