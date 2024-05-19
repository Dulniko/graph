from utils.edmonds_karp import EdmondsKarp

graph = [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 0, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ]

ek = EdmondsKarp(graph)
ek.graph_visualize(ek.graph, "temp.png")
max_flow = ek.edmonds_karp(0, 5)
ek.graph_visualize(ek.flow_graph_fixed(), "temp3.png")