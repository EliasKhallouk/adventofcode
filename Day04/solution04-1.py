# LECTURE DU FICHIER
with open('Day04/input.txt', 'r') as file:
    data = file.read()

# CALCULE DU NOMBRE DU XMAS
result=0
data = data.split("\n")
for i in range(len(data)):
    for j in range(len(data[i])):
        if j + 3 < len(data[i]) and data[i][j] == "X" and data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S": # Vérification horizontale
            result+=1
        if i + 3 < len(data) and data[i][j] == "X" and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S": # Vérification verticale
            result+=1
        if i + 3 < len(data) and j + 3 < len(data[i]) and data[i][j] == "X" and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S": #  Vérification diagonale Haut-Droite
            result+=1
        if i + 3 < len(data) and j - 3 >= 0 and data[i][j] == "X" and data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S": #  Vérification diagonale Haut-Gauche
            result+=1
        if i - 3 >= 0 and j + 3 < len(data[i]) and data[i][j] == "X" and data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S": #  Vérification diagonale Bas-Droite
            result+=1
        if i - 3 >= 0 and j - 3 >= 0 and data[i][j] == "X" and data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S": #  Vérification diagonale Bas-Gauche
            result+=1
        if j - 3 >= 0 and data[i][j] == "X" and data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S": # Vérification horizontale inverse
            result+=1
        if i - 3 >= 0 and data[i][j] == "X" and data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S": # Vérification verticale inverse
            result+=1

# AFFICHAGE DU NOMBRE DE XMAS
print(result) # --> 2458