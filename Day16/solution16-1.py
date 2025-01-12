import heapq
import sys
from collections import defaultdict

# LECTURE DU FICHIER
with open("Day16/input.txt", 'r') as f:
    a = [list(line.strip()) for line in f.readlines()]

# CHARGEMENT DE LA CARTE
m, n = len(a), len(a[0])

# TROUVER LA POSITION INITIALE DE 'S'
ri, rj = next((i, j) for i, row in enumerate(a) for j, c in enumerate(row) if c == 'S')

# CLASSE POUR REPRÉSENTER UN ÉTAT DANS LA FILE DE PRIORITÉ
class Q:
    def __init__(self, i, j, d, c):
        self.i = i
        self.j = j
        self.d = d
        self.c = c

    def __lt__(self, other):
        return self.c < other.c

# DIRECTIONS : DROITE, BAS, GAUCHE, HAUT
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# FILE DE PRIORITÉ
q = []
heapq.heappush(q, Q(ri, rj, 0, 0))

# COÛTS ET ÉTATS VISITÉS
cost = [[[sys.maxsize] * 4 for _ in range(n)] for _ in range(m)]
visited = [[[False] * 4 for _ in range(n)] for _ in range(m)]

# FONCTION POUR AJOUTER UN ÉTAT DANS LA FILE DE PRIORITÉ
def enqueue(i, j, d, c):
    if not (0 <= i < m and 0 <= j < n):  # VÉRIFIE LES LIMITES
        return
    if a[i][j] == '#':  # VÉRIFIE LES OBSTACLES
        return
    if cost[i][j][d] <= c:  # VÉRIFIE SI LE COÛT EST MEILLEUR
        return
    cost[i][j][d] = c
    heapq.heappush(q, Q(i, j, d, c))

# INITIALISATION
enqueue(ri, rj, 0, 0)

# PARCOURS AVEC DIJKSTRA
while q:
    current = heapq.heappop(q)
    i, j, d, c = current.i, current.j, current.d, current.c

    if visited[i][j][d]:
        continue
    visited[i][j][d] = True

    # SI ON ATTEINT LA CASE 'E', ON AFFICHE LE COÛT ET ON TERMINE
    if a[i][j] == 'E':
        print(c)
        break

    # DÉPLACEMENT DANS LA DIRECTION ACTUELLE
    enqueue(i + di[d], j + dj[d], d, c + 1)

    # ROTATION À DROITE
    enqueue(i, j, (d + 1) % 4, c + 1000)

    # ROTATION À GAUCHE
    enqueue(i, j, (d + 3) % 4, c + 1000)