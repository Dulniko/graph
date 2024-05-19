from matplotlib import pyplot as plt
from collections import deque
import networkx as nx
from utils.edmonds_karp import EdmondsKarp
from utils.graham import Graham, Point
import numpy as np
from scipy.spatial import ConvexHull, distance

class GraphToHull:
    def __init__(self, graph, source, sink, points):
        self.points = points
        self.graham = Graham(points)
        self.hull = self.graham.scan()

        self.ek = EdmondsKarp(graph)
        self.source = source
        self.sink = sink
        self.ek.edmonds_karp(source, sink)
        self.flow_graph = self.ek.flow

    def get_bounding_box(self, points, padding=0.1):
        min_x = min(p.x for p in points)
        max_x = max(p.x for p in points)
        min_y = min(p.y for p in points)
        max_y = max(p.y for p in points)

        x_range = max_x - min_x
        y_range = max_y - min_y
        min_x -= x_range * padding
        max_x += x_range * padding
        min_y -= y_range * padding
        max_y += y_range * padding

        return min_x, max_x, min_y, max_y

    def normalize_positions(self, pos, min_x, max_x, min_y, max_y):
        pos_x = [p[0] for p in pos.values()]
        pos_y = [p[1] for p in pos.values()]
        pos_min_x = min(pos_x)
        pos_max_x = max(pos_x)
        pos_min_y = min(pos_y)
        pos_max_y = max(pos_y)

        scale_x = (max_x - min_x) / (pos_max_x - pos_min_x)
        scale_y = (max_y - min_y) / (pos_max_y - pos_min_y)
        scale = min(scale_x, scale_y)

        for key in pos:
            pos[key] = (
                min_x + (pos[key][0] - pos_min_x) * scale,
                min_y + (pos[key][1] - pos_min_y) * scale,
            )
        return pos
    
    def is_point_inside_hull(self, point, hull_points):
        hull = ConvexHull(hull_points)
        new_points = np.vstack((hull_points, point))
        new_hull = ConvexHull(new_points)
        return list(hull.vertices) == list(new_hull.vertices)

    def adjust_positions_within_hull(self, pos, hull_points):
        adjusted_pos = {}
        for key, (x, y) in pos.items():
            if not self.is_point_inside_hull((x, y), hull_points):
                center_x = np.mean(hull_points[:, 0])
                center_y = np.mean(hull_points[:, 1])
                x = (x + center_x) / 2
                y = (y + center_y) / 2
            adjusted_pos[key] = (x, y)
        return adjusted_pos

    def visualization(self, buf):
        plt.figure()

        points = self.points
        hull = self.hull
        x = [p.x for p in points]
        y = [p.y for p in points]
        plt.plot(x, y, "o", label="Points")
        hull_points = hull + [hull[0]]
        hx = [p.x for p in hull_points]
        hy = [p.y for p in hull_points]
        plt.plot(hx, hy, "r-", label="Convex Hull")

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

        min_x, max_x, min_y, max_y = self.get_bounding_box(hull_points, 0.01)

        pos = nx.shell_layout(G)
        pos = self.normalize_positions(pos, min_x, max_x, min_y, max_y)
        pos = self.adjust_positions_within_hull(pos, np.array([[p.x, p.y] for p in hull]))

        nx.draw_networkx_nodes(G, pos, node_color='blue')
        nx.draw_networkx_nodes(G, pos, nodelist=[self.sink+1], node_color='green')
        nx.draw_networkx_nodes(G, pos, nodelist=[self.source+1], node_color='#46c741')

        edges = nx.draw_networkx_edges(
            G, pos, arrowstyle="->", arrowsize=10, edge_color="black"
        )
        nx.draw_networkx_labels(
            G, pos, font_size=12, font_color="white", font_weight="bold"
        )
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph within Convex Hull")
        plt.savefig(buf, format="png")
        plt.close()
