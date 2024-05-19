from typing import List
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Guard:
    uuid: uuid4
    energy: int


@dataclass
class Point:
    x: int
    y: int
    brightness: int


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
