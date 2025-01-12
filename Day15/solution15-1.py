import re

class P2:
    def __init__(self, x, y):
        self.x = x
        self.y = y



# DEPLACER LE PERSONNAGE SUR LA CARTE
def deplacer_personnage(map_data, moves_data):
    a = [list(row) for row in map_data.split("\n")]
    ri, rj = next((i, j) for i, row in enumerate(a) for j, c in enumerate(row) if c == '@')
    a[ri][rj] = '.'

    for line in moves_data.split("\n"):
        for c in line:
            di, dj = 0, 0
            if c == '<':
                dj = -1
            elif c == 'v':
                di = 1
            elif c == '>':
                dj = 1
            elif c == '^':
                di = -1
            else:
                raise ValueError(f"Unexpected character: {c}")

            k = 1
            while a[ri + di * k][rj + dj * k] == 'O':
                k += 1

            if a[ri + di * k][rj + dj * k] == '#':
                continue
            elif a[ri + di * k][rj + dj * k] == '.':
                if k > 1:
                    a[ri + di * k][rj + dj * k] = 'O'
                    a[ri + di][rj + dj] = '.'
                ri += di
                rj += dj
            else:
                raise ValueError("Unexpected state encountered")

    return a

# CALCULER LA SOMME TOTALE
def calculer_somme_totale(a):
    total_sum = 0
    for i, row in enumerate(a):
        for j, c in enumerate(row):
            if c == 'O':
                total_sum += 100 * i + j
    return total_sum


# LECTURE DU FICHIER
with open("Day15/input.txt", "r") as file:
    map_data, moves_data = file.read().strip().split("\n\n")
a = deplacer_personnage(map_data, moves_data)
total_sum = calculer_somme_totale(a)
print(total_sum)
