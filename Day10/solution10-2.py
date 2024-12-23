# LECTURE ET STRUCTURATION DU FICHIER
with open('Day10/input.txt', 'r') as file:
    data = file.read()

# PARSE LA CARTE TOPOGRAPHIQUE
def parse_map(input_map):
    return [list(map(int, line.strip())) for line in input_map.splitlines()]

# OBTENIR LES VOISINS VALIDES (HAUT, BAS, GAUCHE, DROITE) DANS LES LIMITES
def get_neighbors(x, y, rows, cols):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny

# COMPTER RECURSIVEMENT LES SENTIERS DISTINCTS A PARTIR DE (X, Y)
def count_trails(x, y, current_height, topographic_map, memo):
    if topographic_map[x][y] == 9:
        return 1  # Atteint une fin valide d'un sentier

    if (x, y, current_height) in memo:
        return memo[(x, y, current_height)]

    rows, cols = len(topographic_map), len(topographic_map[0])
    total_trails = 0

    for nx, ny in get_neighbors(x, y, rows, cols):
        if topographic_map[nx][ny] == current_height + 1:
            total_trails += count_trails(nx, ny, current_height + 1, topographic_map, memo)

    memo[(x, y, current_height)] = total_trails
    return total_trails

# TROUVER LES EVALUATIONS DES POINTS DE DEPART DES SENTIERS
def find_trailhead_ratings(topographic_map):
    rows, cols = len(topographic_map), len(topographic_map[0])
    trailheads = [(x, y) for x in range(rows) for y in range(cols) if topographic_map[x][y] == 0]
    total_rating = 0
    memo = {}

    for trailhead in trailheads:
        x, y = trailhead
        total_rating += count_trails(x, y, 0, topographic_map, memo)

    return total_rating

topographic_map = parse_map(data)
result = find_trailhead_ratings(topographic_map)

# AFFICHAGE DU RESULTAT
print(result) # --> 1120