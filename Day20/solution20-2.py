import math
from collections import deque

def main():
    # Lecture des données d'entrée
    with open("Day20/input.txt", "r") as f:
        a = [list(line.strip()) for line in f.readlines()]

    m, n = len(a), len(a[0])

    # Trouver les positions de départ ('S') et de fin ('E')
    si, sj = next((i, j) for i, row in enumerate(a) for j, c in enumerate(row) if c == 'S')
    ei, ej = next((i, j) for i, row in enumerate(a) for j, c in enumerate(row) if c == 'E')

    t = 100

    # Calcul des distances depuis le point de départ et le point de fin
    ds = maze_distances(n, m, si, sj, lambda i, j: a[i][j] != '#')
    de = maze_distances(n, m, ei, ej, lambda i, j: a[i][j] != '#')

    d0 = ds[ei][ej]
    assert de[si][sj] == d0

    cnt = 0
    z = 20

    # Parcours pour trouver les configurations valides
    for i in range(n):
        for j in range(m):
            for di in range(-z, z + 1):
                for dj in range(-z, z + 1):
                    if abs(di) + abs(dj) <= z:
                        i1 = i + di
                        j1 = j + dj
                        if 0 <= i1 < n and 0 <= j1 < m:
                            if ds[i][j] + de[i1][j1] + abs(di) + abs(dj) <= d0 - t:
                                cnt += 1

    print(cnt)


def maze_distances(n, m, start_i, start_j, is_valid):
    """
    Calcule les distances dans un labyrinthe depuis une position de départ.
    """
    distances = [[math.inf] * m for _ in range(n)]
    distances[start_i][start_j] = 0
    queue = deque([(start_i, start_j)])

    while queue:
        i, j = queue.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and is_valid(ni, nj) and distances[ni][nj] == math.inf:
                distances[ni][nj] = distances[i][j] + 1
                queue.append((ni, nj))

    return distances


if __name__ == "__main__":
    main()
