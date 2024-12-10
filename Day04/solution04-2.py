# LECTURE DU FICHIER
with open('Day04/input.txt', 'r') as file:
    data = file.read()

# CALCULE DU NOMBRE DU XMAS
result=0
data = data.split("\n")
for i in range(len(data)):
    for j in range(len(data[i])):
        if(i-1>=0 and i+1<len(data) and j-1>=0 and j+1<len(data[i]) and data[i][j]=="A" and ( (data[i+1][j+1]=="M" and data[i-1][j-1]=="S") or (data[i+1][j+1]=="S" and data[i-1][j-1]=="M") ) and ( (data[i+1][j-1]=="M" and data[i-1][j+1]=="S") or (data[i+1][j-1]=="S" and data[i-1][j+1]=="M") )):
            result+=1

# AFFICHAGE DU NOMBRE DE XMAS
print(result) # --> 1945