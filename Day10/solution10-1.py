from collections import deque

# LECTURE ET STRUCTURATION DU FICHIER
with open('Day10/input.txt', 'r') as file:
    data = file.read()


# FONCTION POUR PARSER LA CARTE
def parse_map(input_map):
    return [list(map(int, line.strip())) for line in input_map.splitlines()]

# FONCTION POUR OBTENIR LES VOISINS VALIDES
def get_neighbors(x, y, rows, cols):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny

# FONCTION POUR TROUVER LES SCORES DES POINTS DE DÉPART
def find_trailhead_scores(topographic_map):
    rows, cols = len(topographic_map), len(topographic_map[0])
    trailheads = [(x, y) for x in range(rows) for y in range(cols) if topographic_map[x][y] == 0]
    total_score = 0

    for trailhead in trailheads:
        queue = deque([trailhead])
        visited = set()
        reachable_nines = set()

        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in get_neighbors(x, y, rows, cols):
                if (nx, ny) in visited:
                    continue
                height_diff = topographic_map[nx][ny] - topographic_map[x][y]
                if height_diff == 1:
                    queue.append((nx, ny))
                    if topographic_map[nx][ny] == 9:
                        reachable_nines.add((nx, ny))

        total_score += len(reachable_nines)

    return total_score



topographic_map = parse_map(data)

# CALCUL DU SCORE TOTAL
result = find_trailhead_scores(topographic_map)

# AFFICHAGE DU RESULTAT
print(result) # --> 496