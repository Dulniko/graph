from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def abs(x):
    return x if x >= 0 else -x


def sgn(x):
    return 1 if x > 0 else 0 if x == 0 else -1


def det(p, q, r):
    return p.x*q.y + q.x*r.y + r.x*p.y - r.x*q.y - p.x*r.y - q.x*p.y


def isPointInSegment(p, q, r): # p-q -> segment, r -> point
    """
    Function that checks if the point r lies on the segment p-q.
    """
    if det(p, q, r) == 0:
        return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(p.y, q.y)
    else:
        return False


def alfa(p):
    """
    Function that returns the angle between the x-axis and the line connecting the point p with the origin.
    """
    d = abs(p.x) + abs(p.y)
    if p.x >= 0:
        if p.y >= 0:
            return p.y / d
        else:
            return 4 - (abs(p.y) / d)
    else:
        if p.y >= 0:
            return 2 - (p.y / d)
        else:
            return 2 + (abs(p.y) / d)


def polarSorting(points): # points -> array of points
    """
    Function that sorts the points in the array in the polar coordinate system.
    """
    points.sort(key=lambda point: alfa(point))
    return points


def graham(points):
    """
    Function that finds the convex hull of the set of points using the Graham algorithm.
    """
    n = len(points)
    points = polarSorting(points)
    hull = []
    hull.append(points[0])
    hull.append(points[1])
    for i in range(2, n):
        while len(hull) > 1 and det(hull[-2], hull[-1], points[i]) < 0:
            hull.pop()
        hull.append(points[i])

    return hull


points = []
for _ in range(10):
    x = randint(-10, 10)
    y = randint(-10, 10)
    points.append(Point(x, y))

hull = graham(points)
for point in hull:
    print(f'({point.x}, {point.y})')






