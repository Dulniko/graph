import numpy as np
from graphviz import Digraph, Graph

edges_directed = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 3)]
edges_undirected = [('A', 'B', 1), ('B', 'A', 1), ('B', 'C', 2), ('C', 'B', 2), ('A', 'C', 3), ('C', 'A', 3)]
vertices = sorted({v for edge in edges_directed for v in edge[:2]})

def adjacency_matrix(vertices, edges, is_directed=True):
    matrix = np.zeros((len(vertices), len(vertices)), dtype=int)
    for start, end, weight in edges:
        i, j = vertices.index(start), vertices.index(end)
        matrix[i][j] = weight
        if not is_directed:
            matrix[j][i] = weight
    return matrix

def adjacency_list(edges, is_directed=True):
    adj_list = {vertex: [] for vertex in vertices}
    for start, end, weight in edges:
        adj_list[start].append((end, weight))
        if not is_directed:
            adj_list[end].append((start, weight))
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

# directed
matrix_directed = adjacency_matrix(vertices, edges_directed)
adj_list_directed = adjacency_list(edges_directed)
edge_array_directed, weight_array_directed = arrays_representation(edges_directed)

# undirected
matrix_undirected = adjacency_matrix(vertices, edges_undirected, is_directed=False)
adj_list_undirected = adjacency_list(edges_undirected, is_directed=False)
edge_array_undirected, weight_array_undirected = arrays_representation(edges_undirected)

directed_graph_viz = visualize_directed_graph(vertices, edges_directed)
undirected_graph_viz = visualize_undirected_graph(vertices, edges_directed)

save_graph(directed_graph_viz, 'directed_weighted_graph')
save_graph(undirected_graph_viz, 'undirected_weighted_graph')

print("Macierz sąsiedztwa grafu skierownego:")
print(matrix_directed)
print("\nLista sąsiadów grafu skierownego:")
print(adj_list_directed)
print("\nDwie tablice grafu skierownego:")
print("Tablica krawędzi:", edge_array_directed)
print("Tablica wag:", weight_array_directed)

print("\nMacierz sąsiedztwa grafu nieskierowanego:")
print(matrix_undirected)
print("\nLista sąsiadów grafu nieskierowanego:")
print(adj_list_undirected)
print("\nDwie tablice grafu nieskierowanego:")
print("Tablica krawędzi:", edge_array_undirected)
print("Tablica wag:", weight_array_undirected)