from typing import List
from dataclasses import dataclass


@dataclass
class Edge:
    src: int
    dest: int


class Graph:
    def __init__(self, num_front: int, num_back: int):
        self.num_front = num_front
        self.num_back = num_back
        self.V = num_front + num_back
        self.graph: List[List[int]] = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, src: int, dest: int):
        self.graph[src][self.num_front + dest] = 1

    def is_valid_assignment(self, u: int, match: List[int], seen: List[bool]) -> bool:
        for v in range(self.num_front, self.V):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True
                if match[v - self.num_front] == -1 or self.is_valid_assignment(
                    match[v - self.num_front], match, seen
                ):
                    match[v - self.num_front] = u
                    return True
        return False

    def max_matching(self) -> int:
        match = [-1] * self.num_back
        result = 0
        for i in range(self.num_front):
            seen = [False] * self.V
            if self.is_valid_assignment(i, match, seen):
                result += 1
        return result


def main():
    # input
    num_front = int(input("Podaj liczbe tragarzy z rekoma z przodu: "))
    num_back = int(input("Podaj liczbe tragarzy z rekoma z tylu: "))

    g = Graph(num_front, num_back)

    # podawanie stragarzy ktorzy sie lubia
    print(
        "Podaj pary tragarzy, którzy mogą ze sobą współpracować (format: przod tyl, np. 0 1):"
    )
    print("Aby zakończyć, wpisz 'end'.")

    while True:
        pair = input()
        if pair == "end":
            break
        src, dest = map(int, pair.split())
        g.add_edge(src, dest)

    print("Liczba sparowanych tragarzy w maksymalnym skojarzeniu:", g.max_matching())


if __name__ == "__main__":
    main()
