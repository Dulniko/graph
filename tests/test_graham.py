import pytest
from utils.graham import Graham, Point


@pytest.mark.parametrize(
    "points, expected",
    [
        (
            [
                Point(0, 3, uuid=1),
                Point(1, 1, uuid=2),
                Point(2, 2, uuid=3),
                Point(4, 4, uuid=4),
                Point(0, 0, uuid=5),
                Point(1, 2, uuid=6),
                Point(3, 1, uuid=7),
                Point(3, 3, uuid=8),
            ],
            [
                Point(0, 0, uuid=5), 
                Point(3, 1, uuid=7), 
                Point(4, 4, uuid=4), 
                Point(0, 3, uuid=1),
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
        assert p.uuid == e.uuid
