# LECTURE DU FICHIER
with open("Day15/input.txt", 'r') as f:
    map_data, moves_data = f.read().split("\n\n")

# CONVERTIR LES DONNEES EN TABLEAU 2D
map_data = map_data.splitlines()
moves_data = moves_data.splitlines()

# INITIALISER LA CARTE
a = [[{
    '#': "##",
    'O': "[]",
    '.': "..",
    '@': "@."
}.get(char, ValueError(f"Invalid character: {char}")) for char in line] for line in map_data]

# CONVERTIR LE TABLEAU 2D EN STRUCTURE MUTABLE
a = [list("".join(row)) for row in a]

# TROUVER LA POSITION INITIALE DE '@'
ri, rj = next((i, j) for i, row in enumerate(a) for j, char in enumerate(row) if char == '@')
a[ri][rj] = '.'

# DEPLACER LE PERSONNAGE SELON LES INSTRUCTIONS
for line in moves_data:
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
            raise ValueError(f"Invalid move: {c}")

        k = 1
        if di == 0:
            while a[ri][rj + dj * k] in {'[', ']'}:
                k += 1
            if a[ri][rj + dj * k] == '#':
                continue
            elif a[ri][rj + dj * k] == '.':
                if k > 1:
                    assert k % 2 == 1
                    for t in range(2, k + 1):
                        a[ri][rj + dj * t] = ']' if (t % 2 == 0) == (dj < 0) else '['
                    a[ri + di][rj + dj] = '.'
                ri += di
                rj += dj
            else:
                raise ValueError("Unexpected character!")
        else:
            ms = {ri: {rj}}
            ci = ri
            blocked = False
            while not blocked and ci in ms:
                for j in ms[ci]:
                    next_char = a[ci + di][j]
                    if next_char == '[':
                        ms.setdefault(ci + di, set()).update({j, j + 1})
                    elif next_char == ']':
                        ms.setdefault(ci + di, set()).update({j - 1, j})
                    elif next_char == '#':
                        blocked = True
                        break
                    elif next_char != '.':
                        raise ValueError("Unexpected character!")
                ci += di

            if not blocked:
                ci -= di
                while ci in ms:
                    for j in ms[ci]:
                        a[ci + di][j] = a[ci][j]
                        a[ci][j] = '.'
                    ci -= di
                ri += di

# CALCULER LA SOMME TOTALE
total_sum = sum(100 * i + j for i, row in enumerate(a) for j, char in enumerate(row) if char == '[')

# AFFICHAGE DU RESULTAT
print(total_sum)