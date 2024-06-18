import pytest
from utils.graham import Graham, Point


@pytest.mark.parametrize(
    "points, expected",
    [
        (
            [
                Point(0, 3),
                Point(1, 1),
                Point(2, 2),
                Point(4, 4),
                Point(0, 0),
                Point(1, 2),
                Point(3, 1),
                Point(3, 3),
            ],
            [
                Point(0, 0),
                Point(3, 1),
                Point(4, 4),
                Point(0, 3),
            ],
        ),
        (
            [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 0), Point(1, -1)],
            [
                Point(0, 0),
                Point(1, -1),
                Point(3, 0),
                Point(2, 2),
            ],
        ),
        (
            [
                Point(0, 0),
                Point(2, 2),
                Point(1, 1),
                Point(2, 0),
                Point(3, 3),
                Point(4, 2),
            ],
            [
                Point(0, 0),
                Point(2, 0),
                Point(4, 2),
                Point(3, 3),
            ],
        ),
        (
            [
                Point(0, 0),
                Point(1, 1),
                Point(2, 2),
                Point(3, 3),
                Point(4, 4),
                Point(5, 5),
                Point(0, 5),
                Point(5, 0),
            ],
            [
                Point(0, 0),
                Point(5, 0),
                Point(5, 5),
                Point(0, 5),
            ],
        ),
        (
            [
                Point(0, 0),
                Point(1, 2),
                Point(2, 4),
                Point(3, 1),
                Point(4, 4),
                Point(2, 2),
                Point(1, 1),
                Point(5, 3),
                Point(3, 3),
                Point(0, 4),
            ],
            [
                Point(0, 0),
                Point(3, 1),
                Point(5, 3),
                Point(4, 4),
                Point(2, 4),
                Point(0, 4),
            ],
        ),
        (
            [
                Point(1, 1),
                Point(2, 2),
                Point(3, 3),
                Point(4, 4),
                Point(5, 5),
                Point(6, 6),
                Point(7, 7),
                Point(8, 8),
                Point(9, 9),
                Point(0, 0),
            ],
            [
                Point(0, 0),
                Point(1, 1),
                Point(2, 2),
                Point(3, 3),
                Point(4, 4),
                Point(5, 5),
                Point(6, 6),
                Point(7, 7),
                Point(8, 8),
                Point(9, 9),
            ],
        ),
        (
            [
                Point(0, 3),
                Point(1, 1),
                Point(2, 2),
                Point(3, 3),
                Point(4, 0),
                Point(5, 3),
                Point(6, 2),
                Point(7, 1),
                Point(8, 4),
                Point(4, 5),
            ],
            [
                Point(0, 3),
                Point(1, 1),
                Point(4, 0),
                Point(7, 1),
                Point(8, 4),
                Point(4, 5),
            ],
        ),
        (
            [
                Point(0, 0),
                Point(2, 1),
                Point(1, 3),
                Point(3, 5),
                Point(4, 4),
                Point(5, 2),
                Point(6, 1),
                Point(7, 3),
                Point(8, 0),
                Point(9, 2),
                Point(10, 5),
            ],
            [
                Point(0, 0),
                Point(8, 0),
                Point(9, 2),
                Point(10, 5),
                Point(3, 5),
                Point(1, 3),
            ],
        ),
        (
            [
                Point(0, 0),
                Point(2, 0),
                Point(1, 1),
                Point(3, 1),
                Point(4, 2),
                Point(2, 2),
                Point(0, 3),
                Point(1, 4),
                Point(3, 4),
                Point(4, 3),
            ],
            [
                Point(0, 0),
                Point(2, 0),
                Point(3, 1),
                Point(4, 2),
                Point(4, 3),
                Point(3, 4),
                Point(1, 4),
                Point(0, 3),
            ],
        ),
        # TODO: Add more test cases
    ],
)
def test_graham_scan(points, expected):
    graham = Graham(points)
    hull = graham.scan()

    for p, e in zip(hull, expected):
        assert p.x == e.x
        assert p.y == e.y
