import pytest
from utils.guards import patrol_route, Stop, Point


@pytest.mark.parametrize(
    "points, max_steps, expected",
    [
        (
            [
                Point(0, 0, 10),
                Point(1, 3, 15),
                Point(3, 2, 11),
                Point(2, 4, 8),
                Point(7, 5, 20),
                Point(-1, 0, 21),
            ],
            2,
            [
                Stop(Point(3, 2, 11), False),
                Stop(Point(2, 4, 8), False),
                Stop(Point(-1, 0, 21), True),
            ],
        ),
    ],
)
def test_patrol_route(points, max_steps, expected):
    assert patrol_route(points, max_steps) == expected
