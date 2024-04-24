import pytest
from utils.graham import graham_scan, Point

@pytest.mark.parametrize('points, expected', [
    ([
        (0, 3), (2, 2), (1, 1), (2, 1),
        (3, 1), (0, 1), (3, 3)
    ], [
        (3, 1), (2, 2), (1, 1), (3, 3),
        (0, 3), (0, 1)
    ]),
    # TODO: Add more test cases
])
def test_graham_scan(points, expected):
    points = [Point(x, y) for x, y in points]
    hull = graham_scan(points)
    assert hull == [Point(x, y) for x, y in expected]
