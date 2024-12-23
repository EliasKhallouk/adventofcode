import re

# LECTURE DU FICHIER
with open('Day13/input.txt', 'r') as file:
    data = file.read().strip().split('\n\n')

# CALCULER LE RESULTAT
sum_result = 0
for entry in data:
    lines = entry.split('\n')
    ax, ay = map(int, re.search(r"Button A: X\+(\d+), Y\+(\d+)", lines[0]).groups())
    bx, by = map(int, re.search(r"Button B: X\+(\d+), Y\+(\d+)", lines[1]).groups())
    px, py = map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", lines[2]).groups())
    
    best = float('inf')
    for a in range(px // ax + 1):
        rx = px - ax * a
        ry = py - ay * a
        if rx >= 0 and ry >= 0:
            b = rx // bx
            if rx == b * bx and ry == b * by:
                c = 3 * a + b
                if c < best:
                    best = c
    if best < float('inf'):
        sum_result += best

# AFFICHAGE DU RESULTAT
print(sum_result) # --> 34787