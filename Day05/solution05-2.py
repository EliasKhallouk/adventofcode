# LECTURE DU FICHIER
with open('Day05/input.txt', 'r') as file:
    data = file.read()

# REMPLISSAGE DxES LISTES
result_part2 = 0
data = data.split("\n")

data_bar = []
z = 0
while z < len(data):
    if data[z] != "":
        nums = [int(num) for num in data[z].split("|")]
        data_bar.append(nums)
    else:
        z += 1
        break
    z += 1

data_vir = []
while z < len(data):
    if data[z] != "":
        nums = [int(num) for num in data[z].split(",")]
        data_vir.append(nums)
    z += 1

# Fonction pour vérifier si une mise à jour est correctement ordonnée
def is_correctly_ordered(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if [update[i], update[j]] in rules:
                continue
            elif [update[j], update[i]] in rules:
                return False
    return True

# Fonction pour trier une mise à jour selon les règles
def sort_update(update, rules):
    graph = {page: [] for page in update}
    for x, y in rules:
        if x in graph and y in graph:
            graph[x].append(y)

    # Algorithme de tri topologique
    visited = set()
    stack = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            visit(neighbor)
        stack.append(node)

    for node in graph:
        visit(node)

    return stack[::-1]

# CALCUL DES RÉSULTATS
for update in data_vir:
    if not is_correctly_ordered(update, data_bar):
        sorted_update = sort_update(update, data_bar)
        result_part2 += sorted_update[len(sorted_update) // 2]

# AFFICHAGE DES RÉSULTATS
print(result_part2) # --> 6204
