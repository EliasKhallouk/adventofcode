import bisect

# LECTURE DU FICHIER
with open('Day01/input.txt', 'r') as file:
    data = file.read()

# REMPLISSAGE DES TABLEAUX
data_left = []
data_right = []
i = 0
j = 0
while i < len(data):
    if j % 2 == 0:
        data_left.append(int(data[i:i+6]))
        i += 8
    else:
        data_right.append(int(data[i:i+6]))
        i += 6
    j += 1

# CALCUL DE LA SIMILARITE
similaire = 0
for i in data_left:
    compteur = 0
    for j in data_right:
        if i == j:
            compteur += 1
    similaire += i * compteur

# AFFICHAGE DE LA SIMILARITE
print(similaire)