import matplotlib.pyplot as plt

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2  

def convexHull(points):
    n = len(points)
    if n < 3:
        return []
    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    return hull

if __name__ == "__main__":
    points =[[0, 3],
            [2, 2],
            [1.5, 1],
            [2, 1],
            [0, 0],
            [3, 0],
            [3, -3]]

    hull_points = convexHull(points)
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, 'ro')

    for i in range(len(hull_points)):
        plt.plot((hull_points[i][0], hull_points[(i + 1) % len(hull_points)][0]),
                (hull_points[i][1], hull_points[(i + 1) % len(hull_points)][1]), 'b-')
        
    plt.title('Convex Hull')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig('convex_hull.png')