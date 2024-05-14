import pytest
from utils.edmonds_karp import EdmondsKarp


@pytest.mark.parametrize(
    "graph, source, sink, expected",
    [
        (
            [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]
            ],
            0,
            5,
            23
        ),
        # TODO: Add more test cases
    ],
)
def test_edmonds_karp(graph, source, sink, expected):
    ek = EdmondsKarp(graph)
    flow = ek.edmonds_karp(source, sink)
    assert flow == expected
