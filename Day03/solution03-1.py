# LECTURE DU FICHIER
with open('Day03/input.txt', 'r') as file:
    data = file.read()

# CALCULE DU RESULTAT DE LA MULTIPLICATION
data = data.split('mul(')
result=0
for i in range(len(data)):
    try:
        data[i] = data[i].split(',')
        data[i][1] = data[i][1].split(')')
        if(0<int(data[i][0])<1000 and 0<int(data[i][1][0])<1000 and ' ' not in data[i][0] and ' ' not in data[i][1][0] and len(data[i][1])>1):
            result+=int(data[i][0])*int(data[i][1][0])
    except:
        pass

# AFFICHAGE DU RESULTAT DE LA MULTIPLICATION
print(result) # --> 175615763