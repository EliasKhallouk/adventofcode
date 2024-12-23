from collections import deque

# LECTURE DU FICHIER
with open('Day11/input.txt', 'r') as file:
    initial_stones = list(map(int, file.read().strip().split()))

# APPLIQUER LES REGLES DE TRANSFORMATION A UNE SEULE PIERRE
def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        left = int(str(stone)[:mid])
        right = int(str(stone)[mid:])
        return [left, right]
    else:
        return [stone * 2024]

# UTILISER UNE DEQUE POUR UN POP ET UN APPEND EFFICACE
stones_queue = deque(initial_stones)

# OUVRIR LE FICHIER DE SORTIE
for _ in range(75):
    next_stones = deque()
    while stones_queue:
        stone = stones_queue.popleft()
        next_stones.extend(process_stone(stone))
    stones_queue = next_stones


# AFFICHAGE DU NOMBRE DE PIERRES RESTANTES
print(len(stones_queue)) # -->