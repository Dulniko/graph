
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
    if det(p, q, r) == 0:
        return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(p.y, q.y)
    else:
        return False


def alfa(p):
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
    points.sort(key=lambda point: alfa(point))
    return points


# # example of usage
# punkt1 = Point(2, 3)
# punkt2 = Point(4, 5)
# punkt3 = Point(6, 1)
# punkt4 = Point(3, 4)
# punkt5 = Point(1, 3)
# print(det(punkt1, punkt2, punkt3))
# print(isPointInSegment(punkt1, punkt2, punkt3))
#
# arr = polarSorting([punkt1, punkt2, punkt3, punkt4, punkt5])
#
# for point in arr:
#     print(point.x, point.y, ": ", alfa(point))
