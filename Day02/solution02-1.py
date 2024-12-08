# LECTURE ET STRUCTURATION DU FICHIER
with open('Day02/input.txt', 'r') as file:
    data = file.read()
data = data.split('\n')
data = [[int(num) for num in line.split()] for line in data if line]

# CALCUL DU NOMBRE DE RAPPORT SURS
compteur = 0
for i in range(len(data)):
    variation = 0 # 1 = croissant, 2 = décroissant
    flague = True # True = croissant ou décroissant, False = ni croissant ni décroissant
    old_number = data[i][0]
    for j in range(1,len(data[i])):
        difference = abs(data[i][j] - old_number)
        if data[i][j] > old_number and (variation == 1 or variation == 0) and difference <= 3 and difference >= 1:
            old_number = data[i][j]
            variation = 1
        elif data[i][j] < old_number and (variation == 2 or variation == 0) and difference <= 3 and difference >= 1:
            variation = 1
            old_number = data[i][j]
            variation = 2
        else:
            flague = False
    if flague:
        compteur += 1

# AFFICHAGE DU NOMBRE DE RAPPORT SURS
print(compteur) # --> 341
