# LECTURE DU FICHIER
with open('Day05/input.txt', 'r') as file:
    data = file.read()

# REMPLISSAGE DES LISTES
result=0
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
    nums = [int(num) for num in data[z].split(",")]
    data_vir.append(nums)
    z += 1

# CALCULE DU NOMBRE DE MISES A JOUR CORRECTEMENT ORDONNÉES
flague = False
for i in range(len(data_vir)):
    compteur = 0
    for j in range(len(data_vir[i])):
        sous_compteur = 0
        for l in range(j+1,len(data_vir[i])):
            for k in range(len(data_bar)):
                if data_vir[i][j] == data_bar[k][0] and data_vir[i][l] == data_bar[k][1]:
                    sous_compteur += 1
                    break
        
        if(sous_compteur == len(data_vir[i])-1-j):
            compteur += 1
        
    if(compteur == len(data_vir[i])):
        result += data_vir[i][(len(data_vir[i]))//2]

# AFFICHAGE DU NOMBRE DE XMAS
print(result) # --> 4905