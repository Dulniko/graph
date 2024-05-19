from typing import List
from dataclasses import dataclass
from uuid import uuid4
from utils.graham import Point
from matplotlib import pyplot as plt


@dataclass
class Guard:
    uuid: uuid4
    energy: int


@dataclass
class Stop:
    point: Point
    forced: bool


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(
                self.tree[i * 2], self.tree[i * 2 + 1], key=lambda guard: guard.energy
            )

    def update(self, index, value):
        pos = self.n + index
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(
                self.tree[2 * pos],
                self.tree[2 * pos + 1],
                key=lambda guard: guard.energy,
            )

    def range_query(self, left, right):
        result = Guard(-1, float("-inf"))
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result = max(result, self.tree[left], key=lambda guard: guard.energy)
                left += 1
            if right % 2:
                right -= 1
                result = max(result, self.tree[right], key=lambda guard: guard.energy)
            left //= 2
            right //= 2
        return result


def patrol_route(points: List[Point], max_steps: int) -> List[Stop]:
    # TODO: coś tu nie działa
    stops = []
    step_counter = 1

    for i in range(1, len(points)):
        if step_counter >= max_steps:
            stops.append(Stop(points[i], forced=True))
            step_counter = 1
        elif points[i].brightness < points[i - 1].brightness:
            stops.append(Stop(points[i], forced=False))
            step_counter = 1
        else:
            step_counter += 1
    return stops


def visualize_route(hull: List[Point], stops: List[Stop], buf):
    """
    Visualize the route of a guard based on stops and the convex hull.
    """
    plt.figure()

    x_hull = [point.x for point in hull]
    y_hull = [point.y for point in hull]

    stop_coords = {
        (stop.point.x, stop.point.y): ("red" if stop.forced else "blue")
        for stop in stops
    }

    plt.scatter(x_hull, y_hull, c="grey", label="Hull Points")

    for i in range(len(hull)):
        next_i = (i + 1) % len(hull)
        plt.plot([hull[i].x, hull[next_i].x], [hull[i].y, hull[next_i].y], "k-")

    for point in hull:
        color = stop_coords.get((point.x, point.y), "grey")
        if color == "red":
            plt.scatter(point.x, point.y, c=color, label="Stop (Forced)")
        elif color == "blue":
            plt.scatter(point.x, point.y, c=color, label="Stop (Not Forced)")
        plt.text(point.x, point.y, f"{point.brightness}", fontsize=12, ha="right")

    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("Guard Route Visualization")
    plt.grid(True)
    plt.legend()

    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
