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

# FONCTION POUR SIMULER LE MOUVEMENT DU GARDE
def simulate_guard(lab_map, guard_pos, guard_dir):
    visited = set()
    current_pos = guard_pos
    current_dir = guard_dir

    while True:
        # ENREGISTRER LA POSITION ACTUELLE ET LA DIRECTION
        state = (current_pos, current_dir)
        if state in visited:
            # DÉTECTION DE BOUCLE
            return True
        visited.add(state)

        # CALCUL DE LA POSITION DEVANT LE GARDE
        dr, dc = directions[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)

        # VÉRIFICATION SI LE GARDE SORT DES LIMITES
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            return False

        # VÉRIFICATION SI LA PROCHAINE POSITION EST UN OBSTACLE
        if lab_map[next_pos[0]][next_pos[1]] == "#":
            # TOURNER À DROITE
            current_index = turn_order.index(current_dir)
            current_dir = turn_order[(current_index + 1) % 4]
        else:
            # AVANCER
            current_pos = next_pos

# TESTER CHAQUE POSITION POUR PLACER UN OBSTACLE
valid_obstruction_positions = 0

for r in range(rows):
    for c in range(cols):
        # IGNORER LES OBSTACLES EXISTANTS ET LA POSITION DE DÉPART DU GARDE
        if lab_map[r][c] != "." or (r, c) == guard_pos:
            continue

        # PLACER UNE OBSTRUCTION HYPOTHÉTIQUE
        lab_map[r][c] = "#"
        if simulate_guard(lab_map, guard_pos, guard_dir):
            valid_obstruction_positions += 1
        # RETIRER L'OBSTRUCTION HYPOTHÉTIQUE
        lab_map[r][c] = "."

# AFFICHAGE DU NOMBRE DE POSITIONS VALIDES POUR LES OBSTRUCTIONS
print(valid_obstruction_positions)  # --> 2143
