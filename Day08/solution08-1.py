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

# CALCULER LES ANTINEUDS
for key, values in antennas.items():
    n = len(values)
    for i in range(n - 1):
        for j in range(i + 1, n):
            A = values[i]
            B = values[j]

            # ANTINEUD SUR A
            A_x = 2 * A['x'] - B['x']
            A_y = 2 * A['y'] - B['y']
            if 0 <= A_x < rows and 0 <= A_y < cols:
                antinodes.add(f"{A_x},{A_y}")

            # ANTINEUD SUR B
            B_x = 2 * B['x'] - A['x']
            B_y = 2 * B['y'] - A['y']
            if 0 <= B_x < rows and 0 <= B_y < cols:
                antinodes.add(f"{B_x},{B_y}")

# AFFICHER LE NOMBRE D'ANTINŒUDS
print(len(antinodes))
