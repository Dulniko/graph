import pytest
from utils.matching import Graph


def test_no_edges():
    g = Graph(3, 3)
    assert g.max_matching() == 0


def test_perfect_matching():
    g = Graph(3, 3)
    g.add_edge(0, 0)
    g.add_edge(1, 1)
    g.add_edge(2, 2)
    assert g.max_matching() == 3


def test_some_edges():
    g = Graph(3, 3)
    g.add_edge(0, 0)
    g.add_edge(0, 1)
    g.add_edge(1, 1)
    g.add_edge(2, 2)
    assert g.max_matching() == 3


def test_unbalanced_graph():
    g = Graph(4, 3)
    g.add_edge(0, 0)
    g.add_edge(1, 1)
    g.add_edge(2, 2)
    g.add_edge(3, 1)
    assert g.max_matching() == 3


def test_with_dislikes():
    g = Graph(3, 3)
    g.add_edge(0, 0)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    assert g.max_matching() == 3


def test_complex_case():
    g = Graph(4, 4)
    g.add_edge(0, 0)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    assert g.max_matching() == 4


if __name__ == "__main__":
    pytest.main()
