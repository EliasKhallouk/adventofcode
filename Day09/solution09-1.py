# LECTURE ET STRUCTURATION DU FICHIER
with open('Day09/input.txt', 'r') as file:
    lines = file.read().strip()

lines = [lines[i:i+2] for i in range(0, len(lines), 2)]
s = []
id = 0

# TRAITEMENT DES LIGNES
for l in lines:
    if len(l) == 1:
        a = int(l)
        for _ in range(a):
            s.append(id)
        id += 1
    else:
        a, b = map(int, l)
        for _ in range(a):
            s.append(id)
        id += 1
        for _ in range(b):
            s.append('.')

# RÉORGANISATION DE LA LISTE
l = 0
r = len(s) - 1
while l < r:
    if s[l] != '.':
        l += 1
        continue
    if s[r] == '.':
        r -= 1
        continue
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1

# CALCULER LE SCORE FINAL
cs = 0
for i in range(len(s)):
    if s[i] != '.':
        cs += i * s[i]

# AFFICHER LE SCORE FINAL
print(cs) # --> 6421128769094