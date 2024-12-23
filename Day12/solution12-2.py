# LECTURE DU FICHIER
with open('Day12/input.txt', 'r') as file:
    data = file.read().splitlines()

# CONVERTIR LES DONNEES EN TABLEAU 2D
a = [list(line) for line in data]
m, n = len(a), len(a[0])
f = [[0] * n for _ in range(m)]
q = []
block = 0

# FONCTION POUR ENFILER LES COORDONNEES
def enq(i, j, c):
    if not (0 <= i < m and 0 <= j < n):
        return
    if f[i][j] != 0 or a[i][j] != c:
        return
    f[i][j] = block
    q.append((i, j))

# DIRECTIONS RDLU
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
sum_result = 0

# PARCOURIR CHAQUE CELLULE
for i0 in range(m):
    for j0 in range(n):
        if f[i0][j0] == 0:
            block += 1
            q.clear()
            c = a[i0][j0]
            enq(i0, j0, c)
            h = 0
            while h < len(q):
                i, j = q[h]
                h += 1
                for k in range(4):
                    enq(i + di[k], j + dj[k], c)
            g = [[] for _ in range(4)]
            for i, j in q:
                for k in range(4):
                    i1, j1 = i + di[k], j + dj[k]
                    if not (0 <= i1 < m and 0 <= j1 < n) or f[i1][j1] != block:
                        g[k].append((i1, j1))
            p = 0
            for k in range(4):
                ii = di[(k + 1) % 4]
                if ii == 0:
                    gr = {}
                    for pt in g[k]:
                        if pt[0] not in gr:
                            gr[pt[0]] = []
                        gr[pt[0]].append(pt)
                    sel = lambda pt: pt[1]
                else:
                    gr = {}
                    for pt in g[k]:
                        if pt[1] not in gr:
                            gr[pt[1]] = []
                        gr[pt[1]].append(pt)
                    sel = lambda pt: pt[0]
                for row in gr.values():
                    prev = float('-inf')
                    for pt in sorted(row, key=sel):
                        cur = sel(pt)
                        if cur > prev + 1:
                            p += 1
                        prev = cur
            sum_result += p * len(q)

# AFFICHAGE DU RESULTAT
print(sum_result) # --> 834828