def main():
    # LECTURE DES DONNÉES D'ENTRÉE
    with open("Day18/input.txt", "r") as f:
        data = f.read().strip().split("\n")

    # EXTRACTION DES COORDONNÉES
    a = [tuple(map(int, line.split(","))) for line in data]

    n = 71

    # INITIALISATION DE LA GRILLE
    c = [[False] * n for _ in range(n)]

    # FONCTION POUR CALCULER LES DISTANCES DANS LE LABYRINTHE
    def maze_distances(rows, cols, start_i, start_j, inf, is_accessible):
        from collections import deque

        dist = [[inf] * cols for _ in range(rows)]
        queue = deque([(start_i, start_j)])
        dist[start_i][start_j] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # DROITE, BAS, GAUCHE, HAUT

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx][ny] == inf and is_accessible(nx, ny):
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        return dist

    # PARCOURS DES COORDONNÉES ET MISE À JOUR DE LA GRILLE
    inf = float('inf')
    for ic, jc in a:
        c[ic][jc] = True
        dist = maze_distances(n, n, 0, 0, inf, lambda i, j: not c[i][j])
        if dist[n - 1][n - 1] == inf:
            print(f"{ic},{jc}")
            break

if __name__ == "__main__":
    main()