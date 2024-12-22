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

totalFiles = id
for currID in range(totalFiles - 1, -1, -1):
    start = -1
    end = -1
    for i in range(len(s)):
        if s[i] == currID:
            if start == -1:
                start = i
            end = i
        elif start != -1:
            break

    if start == -1:
        continue

    length = end - start + 1
    bestStart = -1
    for i in range(start - length + 1):
        if all(s[j] == '.' for j in range(i, i + length)):
            bestStart = i
            break

    if bestStart != -1:
        blocks = s[start:end + 1]
        for i in range(start, end + 1):
            s[i] = '.'
        for i in range(len(blocks)):
            s[bestStart + i] = blocks[i]

# CALCULER LE SCORE FINAL
cs = 0
for i in range(len(s)):
    if s[i] != '.':
        cs += i * s[i]

# AFFICHER LE SCORE FINAL
print(cs) # --> 6448168620520