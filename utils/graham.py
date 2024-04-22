from dataclasses import dataclass
import math

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
        return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(p.y, q.y)
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
