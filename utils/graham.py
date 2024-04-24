import math
from dataclasses import dataclass
from matplotlib import pyplot as plt


@dataclass
class Point:
    x: int
    y: int


def det(p, q, r):
    """Calculate the determinant of a 3x3 matrix."""
    return p.x * q.y + q.x * r.y + r.x * p.y - r.x * q.y - p.x * r.y - q.x * p.y


def is_point_in_segment(p, q, r):
    """Check if point r is on the line segment p-q."""
    if det(p, q, r) == 0:
        return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(
            p.y, q.y
        )
    return False


def polar_angle(p):
    """Return the polar angle of point p from the origin."""
    return math.atan2(p.y, p.x)


def polar_sorting(points):
    """Sort points by their polar angle from the origin."""
    return sorted(points, key=polar_angle)


def graham_scan(points):
    """Compute the convex hull of a set of 2D points."""
    points = polar_sorting(points)
    hull = [points[0], points[1]]
    for point in points[2:]:
        while len(hull) > 1 and det(hull[-2], hull[-1], point) < 0:
            hull.pop()
        hull.append(point)
    return hull


def visualize_hull(points, hull):
    plt.figure()
    x = [p.x for p in points]
    y = [p.y for p in points]
    plt.plot(x, y, "o", label="Points")
    hull_points = hull + [hull[0]]
    hx = [p.x for p in hull_points]
    hy = [p.y for p in hull_points]
    plt.plot(hx, hy, "r-", label="Convex Hull")

    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("Convex Hull Visualization")
    plt.legend()
    plt.grid(True)
    plt.savefig("convex_hull.png")


# TODO: delete below code
if __name__ == "__main__":
    points = [
        Point(0, 3),
        Point(2, 2),
        Point(1.5, 1),
        Point(2, 1),
        Point(3, 0),
        Point(0, 0),
        Point(3, -3),
    ]
    hull = graham_scan(points)
    print(hull)
    visualize_hull(points, hull)
