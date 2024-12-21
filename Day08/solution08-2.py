import math

# LECTURE ET STRUCTURATION DU FICHIER
with open('Day08/input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0])

def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)

antinodes = set()
antennas = {}

# COLLECTER LES ANTENNES PAR FRÉQUENCE
for i in range(rows):
    for j in range(cols):
        if grid[i][j] != '.':
            if grid[i][j] in antennas:
                antennas[grid[i][j]].append({'x': i, 'y': j})
            else:
                antennas[grid[i][j]] = [{'x': i, 'y': j}]

# CALCULER LES ANTINŒUDS
for key, values in antennas.items():
    n = len(values)
    if n < 2:
        continue

    # INCLURE TOUTES LES POSITIONS DES ANTENNES COMME ANTINŒUDS
    for val in values:
        antinodes.add(f"{val['x']},{val['y']}")

    for i in range(n - 1):
        for j in range(i + 1, n):
            A = values[i]
            B = values[j]
            dx = B['x'] - A['x']
            dy = B['y'] - A['y']
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # AVANCER À PARTIR DE A
            rr, cc = A['x'] + dx, A['y'] + dy
            while 0 <= rr < rows and 0 <= cc < cols:
                antinodes.add(f"{rr},{cc}")
                rr += dx
                cc += dy

            # RECULER À PARTIR DE A
            rr, cc = A['x'] - dx, A['y'] - dy
            while 0 <= rr < rows and 0 <= cc < cols:
                antinodes.add(f"{rr},{cc}")
                rr -= dx
                cc -= dy

# AFFICHER LE NOMBRE D'ANTINŒUDS
print(len(antinodes))
