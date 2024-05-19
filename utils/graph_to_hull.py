from matplotlib import pyplot as plt
from collections import deque
import networkx as nx
from utils.edmonds_karp import EdmondsKarp
from utils.graham import Graham, Point
import numpy as np

class GraphToHull:
    def __init__(self, graph, source, sink, points):
        self.points = points
        self.graham = Graham(points)
        self.hull = self.graham.scan()

        self.ek = EdmondsKarp(graph)
        self.ek.edmonds_karp(source, sink)
        self.flow_graph = self.ek.flow_graph_fixed()

    def visualization(self, buf):
        plt.figure()

        #Hull
        points = self.points
        hull = self.hull
        x = [p.x for p in points]
        y = [p.y for p in points]
        plt.plot(x, y, "o", label="Points")
        hull_points = hull + [hull[0]]
        hx = [p.x for p in hull_points]
        hy = [p.y for p in hull_points]
        plt.plot(hx, hy, "r-", label="Convex Hull")

        #Graph
        graph = self.flow_graph
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

        plt.title("elo benc")
        plt.savefig(buf, format="png")
        plt.close()
        


points = [Point(0, 0), Point(4, 1), Point(5, 2), Point(4, 4), Point(1, 5), Point(0, 5), Point(-1, 3)]
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

gh = GraphToHull(graph, 0, 5, points)
gh.visualization("hull_graph.png")