from collections import deque
from matplotlib import pyplot as plt
import networkx as nx


class EdmondsKarp:
    def __init__(self, graph):
        """
        Initializes the EdmondsKarp instance with a graph.

        As parameter it takes graph (list of list of int).
        """
        self.ROW = len(graph)
        self.flow = [[0] * self.ROW for _ in range(self.ROW)]
        self.graph = [[0] * self.ROW for _ in range(self.ROW)]
        for i in range(self.ROW):
            for j in range(self.ROW):
                self.graph[i][j] = graph[i][j]

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
        graph = self.graph

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                v = parent[v]

        flow_graph = [[0] * self.ROW for _ in range(self.ROW)]
        for u in range(self.ROW):
            for v in range(self.ROW):
                if self.flow[u][v] > 0:
                    flow_graph[u][v] = self.flow[u][v]
        self.flow = flow_graph

        return max_flow

    def graph_visualize(self, graph, buf):
        """
        Visualize the convex hull of a set of 2D points.

        As parameter it takes the graph as a list of lists and a String, that will be a name of output file.

        If no parameter, it sets files name as 'visualization.png'
        """
        G = nx.DiGraph()
        for ind in range(len(graph)):
            G.add_node(ind + 1)

        for node in range(len(graph)):
            for directed_node in range(len(graph)):
                if graph[node][directed_node] != 0:
                    G.add_edge(
                        node + 1,
                        directed_node + 1,
                        weight=graph[node][directed_node],
                    )

        pos = nx.shell_layout(G)

        nx.draw_networkx_nodes(G, pos)

        edges = nx.draw_networkx_edges(
            G, pos, arrowstyle="->", arrowsize=10, edge_color="black"
        )

        nx.draw_networkx_labels(
            G, pos, font_size=12, font_color="white", font_weight="bold"
        )

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Weighted Digraph")
        plt.savefig(buf, format="png")
        plt.close()

        return graph
