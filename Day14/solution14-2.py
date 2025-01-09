import re

class P2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# LECTURE DU FICHIER
with open('Day14/input.txt', 'r') as file:
    input_data = file.read().strip().split('\n')

# CONSTANTES
m = 101
n = 103

class RD:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

# PARSER LES DONNEES D'ENTREE
rd = []
for s in input_data:
    match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", s)
    if match:
        x, y, vx, vy = map(int, match.groups())
        rd.append(RD(x, y, vx, vy))

# INITIALISATION DES VARIABLES
c = [[0] * m for _ in range(n)]
best = 0
best_k = -1
q = []

# FONCTION POUR ENFILER LES COORDONNEES
def enqueue(x, y):
    if not (0 <= x < m and 0 <= y < n):
        return
    if c[y][x] <= 0:
        return
    c[y][x] = -1
    q.append(P2(x, y))

# CALCULER LE MEILLEUR K
for k in range(1, m * n + 1):
    p = [P2((x.x + x.vx * k) % m, (x.y + x.vy * k) % n) for x in rd]
    for point in p:
        c[point.y][point.x] += 1

    for x0 in range(m):
        for y0 in range(n):
            if c[y0][x0] > 0:
                q.clear()
                h = 0
                enqueue(x0, y0)
                while h < len(q):
                    current = q[h]
                    h += 1
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            enqueue(current.x + dx, current.y + dy)

                if len(q) > best:
                    best = len(q)
                    best_k = k

    for point in p:
        c[point.y][point.x] = 0

# AFFICHAGE DU MEILLEUR K
print(best_k)