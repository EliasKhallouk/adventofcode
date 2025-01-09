import re

class P2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# LECTURE DU FICHIER
with open("Day14/input.txt", "r") as file:
    input_data = file.read().strip().split("\n")

# CONSTANTES
m = 101
n = 103
k = 100

# PARSER LES DONNEES D'ENTREE
p = []
for s in input_data:
    match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", s)
    if match:
        x, y, vx, vy = map(int, match.groups())
        p.append(P2((x + vx * k) % m, (y + vy * k) % n))

# COMPTER LES POINTS DANS CHAQUE QUADRANT
c = [0] * 4
for point in p:
    x, y = point.x, point.y
    if x < m // 2:
        xi = 0
    elif x > m // 2:
        xi = 1
    else:
        continue

    if y < n // 2:
        yi = 0
    elif y > n // 2:
        yi = 1
    else:
        continue

    c[xi * 2 + yi] += 1

# CALCULER LE RESULTAT
ans = 1
for count in c:
    ans *= count

# AFFICHAGE DU RESULTAT
#print(" ".join(map(str, c)))
print(ans)
