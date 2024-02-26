import numpy as np
from graphviz import Digraph, Graph

edges_directed = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 3)]
vertices = sorted({v for edge in edges_directed for v in edge[:2]})

def adjacency_matrix(vertices, edges):
    matrix = np.zeros((len(vertices), len(vertices)), dtype=int)
    for start, end, weight in edges:
        i, j = vertices.index(start), vertices.index(end)
        matrix[i][j] = weight
    return matrix

def adjacency_list(edges):
    adj_list = {vertex: [] for vertex in vertices}
    for start, end, weight in edges:
        adj_list[start].append((end, weight))
    return adj_list

def arrays_representation(edges):
    edge_array = [(start, end) for start, end, _ in edges]
    weight_array = [weight for _, _, weight in edges]
    return edge_array, weight_array

def visualize_directed_graph(vertices, edges):
    dot = Digraph()
    for v in vertices:
        dot.node(v)
    for start, end, weight in edges:
        dot.edge(start, end, label=str(weight))
    return dot

def visualize_undirected_graph(vertices, edges):
    dot = Graph()
    for v in vertices:
        dot.node(v)
    for start, end, weight in edges:
        if start <= end:
            dot.edge(start, end, label=str(weight))
    return dot

def save_graph(graph, filename, format='png'):
    graph.render(filename, view=False, format=format)

matrix = adjacency_matrix(vertices, edges_directed)
adj_list = adjacency_list(edges_directed)
edge_array, weight_array = arrays_representation(edges_directed)

directed_graph_viz = visualize_directed_graph(vertices, edges_directed)
undirected_graph_viz = visualize_undirected_graph(vertices, edges_directed)

save_graph(directed_graph_viz, 'directed_weighted_graph')
save_graph(undirected_graph_viz, 'undirected_weighted_graph')

print("Macierz sąsiedztwa:")
print(matrix)
print("\nLista sąsiadów:")
print(adj_list)
print("\nDwie tablice:")
print("Tablica krawędzi:", edge_array)
print("Tablica wag:", weight_array)
