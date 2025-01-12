import heapq
from collections import deque
import sys

# Lecture des données d'entrée
def read_input(file_name):
    with open(file_name, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def main():
    # Chargement de la carte
    a = read_input("Day16/input.txt")
    m, n = len(a), len(a[0])

    # Trouver la position initiale de 'S'
    ri, rj = next((i, j) for i, row in enumerate(a) for j, c in enumerate(row) if c == 'S')

    # Classe pour représenter un état dans la file de priorité
    class Q:
        def __init__(self, i, j, d, c):
            self.i = i
            self.j = j
            self.d = d
            self.c = c

        def __lt__(self, other):
            return self.c < other.c

    # Directions : Droite, Bas, Gauche, Haut
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # File de priorité
    pq = []
    heapq.heappush(pq, Q(ri, rj, 0, 0))

    # Coûts et états visités
    cost = [[[sys.maxsize] * 4 for _ in range(n)] for _ in range(m)]
    visited = [[[False] * 4 for _ in range(n)] for _ in range(m)]

    # Fonction pour ajouter un état dans la file de priorité
    def enq_dist(i, j, d, c):
        if not (0 <= i < m and 0 <= j < n):  # Vérifie les limites
            return
        if a[i][j] == '#':  # Vérifie les obstacles
            return
        if cost[i][j][d] <= c:  # Vérifie si le coût est meilleur
            return
        cost[i][j][d] = c
        heapq.heappush(pq, Q(i, j, d, c))

    # Initialisation
    enq_dist(ri, rj, 0, 0)

    # Parcours avec Dijkstra
    best = sys.maxsize
    while pq:
        current = heapq.heappop(pq)
        i, j, d, c = current.i, current.j, current.d, current.c

        if visited[i][j][d]:
            continue
        visited[i][j][d] = True

        # Si on atteint la case 'E', on met à jour le meilleur coût
        if a[i][j] == 'E':
            best = min(best, c)

        # Déplacement dans la direction actuelle
        enq_dist(i + di[d], j + dj[d], d, c + 1)

        # Rotation à droite
        enq_dist(i, j, (d + 1) % 4, c + 1000)

        # Rotation à gauche
        enq_dist(i, j, (d + 3) % 4, c + 1000)

    # Trouver la position de 'E'
    ei, ej = next((i, j) for i, row in enumerate(a) for j, c in enumerate(row) if c == 'E')

    # Exploration inversée pour compter les cases atteignables
    visited_u = [[False] * n for _ in range(m)]
    q = deque()
    cnt = 0

    def enq(i, j, d, c):
        if not (0 <= i < m and 0 <= j < n):  # Vérifie les limites
            return
        if cost[i][j][d] != c:  # Vérifie si le coût correspond
            return
        if not visited_u[i][j]:
            visited_u[i][j] = True
            nonlocal cnt
            cnt += 1
        q.append((i, j, d, c))

    # Initialisation de l'exploration inversée
    for d in range(4):
        if cost[ei][ej][d] == best:
            enq(ei, ej, d, best)

    while q:
        i, j, d, c = q.popleft()

        # Déplacement dans la direction opposée
        enq(i - di[d], j - dj[d], d, c - 1)

        # Rotation à droite
        enq(i, j, (d + 1) % 4, c - 1000)

        # Rotation à gauche
        enq(i, j, (d + 3) % 4, c - 1000)

    # Résultat final
    print(cnt)

if __name__ == "__main__":
    main()
