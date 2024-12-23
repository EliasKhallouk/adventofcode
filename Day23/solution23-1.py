from collections import defaultdict

# LECTURE DU FICHIER
graph = defaultdict(set)
with open('Day23/input.txt', 'r') as f:
    for line in f:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

# TROUVER LES TRIANGLES
triangles = set()
for node in graph:
    neighbors = graph[node]
    for neighbor1 in neighbors:
        for neighbor2 in neighbors:
            if neighbor1 < neighbor2 and neighbor2 in graph[neighbor1]:
                # TROUVER UN TRIANGLE, L'AJOUTER TRIE POUR ASSURER L'UNICITE
                triangle = tuple(sorted([node, neighbor1, neighbor2]))
                triangles.add(triangle)

# FILTRER LES TRIANGLES AVEC AU MOINS UN "T"
triangles_with_t = [t for t in triangles if any(comp.startswith('t') for comp in t)]

# AFFICHAGE DU NOMBRE DE TRIANGLES AVEC AU MOINS UN "T"
print(len(triangles_with_t)) # --> 7