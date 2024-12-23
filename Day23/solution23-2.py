from collections import defaultdict

# LECTURE DU FICHIER ET CONSTRUCTION DU GRAPHE
graph = defaultdict(set)
with open('Day23/input.txt', 'r') as f:
    for line in f:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

# UTILISATION DE L'ALGORITHME DE BRON-KERBOSCH POUR TROUVER TOUTES LES CLIQUES
def bron_kerbosch(r, p, x):
    if not p and not x:
        cliques.append(r)
        return
    for v in list(p):
        bron_kerbosch(r | {v}, p & graph[v], x & graph[v])
        p.remove(v)
        x.add(v)

cliques = []
bron_kerbosch(set(), set(graph.keys()), set())

largest_clique = max(cliques, key=len)
mdp = ",".join(sorted(largest_clique))

# AFFICHAGE DU MOT DE PASSE
print(mdp)