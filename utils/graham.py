from matplotlib import pyplot as plt
from uuid import uuid4


class Point:
    def __init__(self, x, y, brightness=0, uuid=str(uuid4())):
        self.x = x
        self.y = y
        self.brightness = brightness
        self.uuid = uuid


class Graham:
    def __init__(self, points):
        """
        Initializes the Graham instance with a list of points.

        Args:
            points (list of Point): The list of points to be processed.
        """
        self.points = points

    def lowest_point(self):
        """Return an index of point which has the lowest y. If points have the same y, return point with the lowest x"""
        min_point = self.points[0]
        for point in self.points:
            if point.x < min_point.x:
                min_point = point
            elif point.x == min_point.x:
                if point.y > min_point.y:
                    min_point = point
        return self.points.index(min_point)

    def orientation(self, p, q, r):
        """Return the position of the point r relative to the vector pq.

        0 if 'r' is on 'pq' vector

        1 if 'r' is on the right side relative to 'pq' vector

        2 if 'r' is on the left side relative to 'pq' vector
        """
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def scan(self):
        """Compute the convex hull of a set of 2D points."""
        num_points = len(self.points)
        if num_points < 3:
            return []

        l = self.lowest_point()

        hull = []

        p = l
        q = 0
        while True:
            hull.append(p)
            q = (p + 1) % num_points

            for i in range(num_points):
                if (
                    self.orientation(self.points[p], self.points[i], self.points[q])
                    == 2
                ):
                    q = i
            p = q
            if p == l:
                break

        return [self.points[ind] for ind in hull]

    def visualize_hull(self, only_hull=False, buf="visualization.png"):
        """
        Visualize the convex hull of a set of 2D points.

        As parameter it takes a String, that will be a name of output file. If no parameter, it sets files name as 'visualization.png'
        """
        if len(self.points) < 3:
            raise ValueError("Not enough points to plot a convex hull")

        hull = self.scan()
        plt.figure()
        if not only_hull:
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
