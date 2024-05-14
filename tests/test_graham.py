import pytest
from utils.graham import Graham, Point


@pytest.mark.parametrize(
    "points, expected",
    [
        (
            [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)],
            [Point(0, 0), Point(3, 1), Point(4, 4), Point(0, 3)],
        ),
        # TODO: Add more test cases
    ],
)
def test_graham_scan(points, expected):
    graham = Graham(points)
    hull = graham.graham_scan()
    assert hull == expected
