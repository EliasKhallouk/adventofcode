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
        bisect.insort(data_left, data[i:i+6])
        i += 8
    else:
        bisect.insort(data_right, data[i:i+6])
        i += 6
    j += 1

# CALCUL DE LA DIFFERENCE
distance = 0
for i in range (len(data_left)):
    distance += abs(int(data_left[i]) - int(data_right[i]))

# AFFICHAGE DE LA DISTANCE TOTAL
print(distance) # --> 1579939