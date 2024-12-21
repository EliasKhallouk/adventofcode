# LECTURE DU FICHIER
with open('Day06/input.txt', 'r') as file:
    lab_map = [list(line.strip()) for line in file.readlines()]

# INITIALISATION DES DIRECTIONS ET LEURS DÉPLACEMENTS
directions = {
    "^": (-1, 0),  # HAUT
    ">": (0, 1),   # DROITE
    "v": (1, 0),   # BAS
    "<": (0, -1)   # GAUCHE
}
turn_order = ["^", ">", "v", "<"]  # ORDRE POUR TOURNER À DROITE

# IDENTIFICATION DE LA POSITION ET DIRECTION INITIALE DU GARDE
rows, cols = len(lab_map), len(lab_map[0])
guard_pos = None
guard_dir = None

for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] in directions:
            guard_pos = (r, c)
            guard_dir = lab_map[r][c]
            lab_map[r][c] = "."  # NETTOYAGE DE LA POSITION DE DÉPART
            break
    if guard_pos:
        break

# INITIALISATION DES POSITIONS VISITÉES
visited = set()
visited.add(guard_pos)

# SIMULATION DU DÉPLACEMENT DU GARDE
while True:
    # CALCUL DE LA POSITION DEVANT LE GARDE
    dr, dc = directions[guard_dir]
    next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

    # VÉRIFICATION SI LE GARDE SORT DES LIMITES
    if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
        break

    # VÉRIFICATION SI LA PROCHAINE POSITION EST UN OBSTACLE
    if lab_map[next_pos[0]][next_pos[1]] == "#":
        # TOURNER À DROITE
        current_index = turn_order.index(guard_dir)
        guard_dir = turn_order[(current_index + 1) % 4]
    else:
        # AVANCER
        guard_pos = next_pos
        visited.add(guard_pos)

# AFFICHAGE DU NOMBRE DE POSITIONS DISTINCTES VISITÉES
print(len(visited)) # --> 5305
