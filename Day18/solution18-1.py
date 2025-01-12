def main():
    # Lecture des données d'entrée
    with open("Day18/input.txt", "r") as f:
        data = f.read().strip().split("\n")

    # Extraction des coordonnées
    a = [tuple(map(int, line.split(","))) for line in data]

    n = 71
    count = 1024

    # Initialisation de la grille
    c = [[False] * n for _ in range(n)]
    for i, j in a[:count]:
        c[i][j] = True

    # Fonction pour calculer les distances dans le labyrinthe
    def maze_distances(rows, cols, start_i, start_j, is_accessible):
        from collections import deque

        dist = [[-1] * cols for _ in range(rows)]
        queue = deque([(start_i, start_j)])
        dist[start_i][start_j] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Droite, Bas, Gauche, Haut

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx][ny] == -1 and is_accessible(nx, ny):
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        return dist

    # Calcul des distances
    dist = maze_distances(n, n, 0, 0, lambda i, j: not c[i][j])

    # Affichage de la distance finale
    print(dist[n - 1][n - 1])


if __name__ == "__main__":
    main()
