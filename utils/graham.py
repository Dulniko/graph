import math
from dataclasses import dataclass
from matplotlib import pyplot as plt


@dataclass
class Point:
    x: int
    y: int


class Graham:
    def __init__(self, points):
        """
        Initializes the Graham instance with a list of points.

        Args:
            points (list of Point): The list of points to be processed.
        """
        self.points = points

    def det(self, p, q, r):
        """Calculate the determinant of a 3x3 matrix."""
        return p.x * q.y + q.x * r.y + r.x * p.y - r.x * q.y - p.x * r.y - q.x * p.y

    def lowest_point(self):
        """Return a point which has the lowest y. If points have the same y, return point with the lowest x"""
        least_y = self.points[0].y
        lowest_p = self.points[0]
        for p in self.points:
            if p.y < least_y:
                lowest_p = p
                least_y = p.y

        least_x = lowest_p.x
        for p in self.points:
            if p.y == least_y:
                if p.x < least_x:
                    lowest_p = p
                    least_x = p.x

        return lowest_p

    def polar_angle(self, p, start_p):
        """Return the polar angle of point p from the origin."""
        return math.atan2(p.y - start_p.y, p.x - start_p.x)

    def polar_sorting(self, points, start_p):
        """Sort points by their polar angle from the origin."""
        return sorted(points, key=lambda angle: self.polar_angle(angle, start_p))

    def scan(self):
        """Compute the convex hull of a set of 2D points."""
        start_p = self.lowest_point()
        sorted_points = self.polar_sorting(self.points, start_p)
        hull = [sorted_points[0], sorted_points[1]]
        for point in sorted_points[2:]:
            while len(hull) > 1 and self.det(hull[-2], hull[-1], point) < 0:
                hull.pop()
            hull.append(point)
        return hull

    def visualize_hull(self, buf="visualization.png"):
        """
        Visualize the convex hull of a set of 2D points.

        As parameter it takes a String, that will be a name of output file. If no parameter, it sets files name as 'visualization.png'
        """
        hull = self.scan()
        plt.figure()
        x = [p.x for p in self.points]
        y = [p.y for p in self.points]
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
        plt.savefig(buf, format="png")
        plt.close()
